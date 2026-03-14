"""
core/llm.py
Unified LLM caller for Tobias.

Per-agent model env vars:
  ANALYST_MODEL, SCOUT_MODEL, COMMIT_MODEL, SETTLER_MODEL
  LLM_PROVIDER, CLAUDE_MODEL, GEMINI_MODEL  (global fallbacks)

Valid models:
  claude-opus-4-6              most capable, ~5x Sonnet
  claude-sonnet-4-6            best balance, default
  claude-haiku-4-5-20251001    fastest/cheapest
  gemini-3.1-flash-lite-preview  free tier, fast
"""

import os
import re
import logging

log = logging.getLogger(__name__)

CLAUDE_OPUS    = "claude-opus-4-6"
CLAUDE_SONNET  = "claude-sonnet-4-6"
CLAUDE_HAIKU   = "claude-haiku-4-5-20251001"
GEMINI_DEFAULT = "gemini-3.1-flash-lite-preview"

AGENT_MODEL_ENV = {
    "analyst": "ANALYST_MODEL",
    "scout":   "SCOUT_MODEL",
    "commit":  "COMMIT_MODEL",
    "settler": "SETTLER_MODEL",
}

# ── Pricing table (USD per million tokens) ────────────────────────────────────
# Used for cost estimation in audit logs
MODEL_PRICING = {
    "claude-opus-4-6":             {"in": 15.00, "out": 75.00},
    "claude-sonnet-4-6":           {"in":  3.00, "out": 15.00},
    "claude-haiku-4-5-20251001":   {"in":  0.80, "out":  4.00},
    "gemini-3.1-flash-lite-preview": {"in": 0.15, "out":  0.60},
    "gemini-2.0-flash-lite":       {"in":  0.075,"out":  0.30},
    "gemini-2.0-flash":            {"in":  0.10, "out":  0.40},
}


def _resolve_model(agent=None):
    """Returns (provider, model_name) for the given agent."""
    if agent and agent in AGENT_MODEL_ENV:
        per_agent = os.getenv(AGENT_MODEL_ENV[agent], "").strip()
        if per_agent:
            provider = "gemini" if "gemini" in per_agent.lower() else "claude"
            return provider, per_agent
    provider = os.getenv("LLM_PROVIDER", "claude").lower()
    if provider == "gemini":
        return "gemini", os.getenv("GEMINI_MODEL", GEMINI_DEFAULT)
    return "claude", os.getenv("CLAUDE_MODEL", CLAUDE_SONNET)


def estimate_cost(model: str, tokens_in: int, tokens_out: int) -> float:
    """Return estimated USD cost for a call given token counts."""
    pricing = MODEL_PRICING.get(model, {"in": 3.0, "out": 15.0})
    return round(
        (tokens_in  / 1_000_000) * pricing["in"] +
        (tokens_out / 1_000_000) * pricing["out"],
        6
    )


class LLMResult:
    """Wraps an LLM response with token usage and cost metadata."""
    def __init__(self, text: str, model: str, tokens_in: int, tokens_out: int):
        self.text       = text
        self.model      = model
        self.tokens_in  = tokens_in
        self.tokens_out = tokens_out
        self.cost_usd   = estimate_cost(model, tokens_in, tokens_out)

    def to_audit_dict(self) -> dict:
        return {
            "model":      self.model,
            "tokens_in":  self.tokens_in,
            "tokens_out": self.tokens_out,
            "cost_usd":   self.cost_usd,
        }


def call_llm(system: str, user: str,
             max_tokens: int = 4096,
             agent: str = None) -> str:
    """
    Call the LLM for the given agent. Returns raw text string.
    Use call_llm_full() if you need token counts and cost in the audit log.
    """
    return call_llm_full(system, user, max_tokens, agent).text


def call_llm_full(system: str, user: str,
                  max_tokens: int = 4096,
                  agent: str = None) -> LLMResult:
    """
    Call the LLM and return an LLMResult with text + token counts + cost.
    Agents should use this for audit logging.
    """
    provider, model = _resolve_model(agent)
    log.info(f"LLM dispatch: agent={agent or 'global'} → {provider}/{model}")

    if provider == "gemini":
        return _call_gemini(system, user, max_tokens, model)
    return _call_claude(system, user, max_tokens, model)


def _call_claude(system: str, user: str, max_tokens: int, model: str) -> LLMResult:
    import anthropic
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set")

    client = anthropic.Anthropic(api_key=api_key)
    log.info(f"Claude ({model}): {len(user)} char prompt")

    msg = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    tokens_in  = msg.usage.input_tokens
    tokens_out = msg.usage.output_tokens
    cost       = estimate_cost(model, tokens_in, tokens_out)
    log.info(f"Claude: in={tokens_in} out={tokens_out} tokens | cost=${cost:.4f}")
    return LLMResult(msg.content[0].text, model, tokens_in, tokens_out)


def _call_gemini(system: str, user: str, max_tokens: int, model_name: str) -> LLMResult:
    import google.generativeai as genai
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system,
    )
    log.info(f"Gemini ({model_name}): {len(user)} char prompt")

    resp = model.generate_content(
        user,
        generation_config=genai.types.GenerationConfig(max_output_tokens=max_tokens),
    )
    # Gemini token counts via usage_metadata
    usage   = getattr(resp, "usage_metadata", None)
    tok_in  = getattr(usage, "prompt_token_count",     0) if usage else 0
    tok_out = getattr(usage, "candidates_token_count", 0) if usage else 0
    cost    = estimate_cost(model_name, tok_in, tok_out)
    log.info(f"Gemini: in={tok_in} out={tok_out} tokens | cost=${cost:.4f}")
    return LLMResult(resp.text, model_name, tok_in, tok_out)


# ── XML tag extraction ─────────────────────────────────────────────────────────

def extract_tag(text: str, tag: str):
    m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
    return m.group(1).strip() if m else None


def extract_all_tags(text: str, tag: str):
    return [m.group(1).strip()
            for m in re.finditer(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)]


def agent_model_name(agent: str) -> str:
    _, model = _resolve_model(agent)
    return model


def current_provider_name() -> str:
    _, model = _resolve_model(None)
    return model
