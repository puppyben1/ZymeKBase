# views/assistant.py
from __future__ import annotations

import logging

from flask import Blueprint, current_app, jsonify, render_template, request
from openai import OpenAI, OpenAIError

bp = Blueprint("assistant", __name__, url_prefix="/assistant")

SYSTEM_PROMPT = (
    "You are Nanozyme-lite's bilingual research assistant. "
    "Help users reason about nanozymes, catalytic activity, datasets, "
    "and visualization workflows. When unsure, admit it instead of fabricating answers."
)


def _build_client(api_key: str, base_url: str) -> OpenAI:
    """
    Create a scoped OpenAI-compatible client for DeepSeek.
    """
    return OpenAI(api_key=api_key, base_url=base_url.rstrip("/"))


@bp.route("/")
def assistant_home():
    ready = bool(current_app.config.get("DEEPSEEK_API_KEY"))
    return render_template("assistant.html", api_ready=ready)


@bp.post("/api")
def assistant_api():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Question is required."}), 400

    api_key = current_app.config.get("DEEPSEEK_API_KEY")
    if not api_key:
        return jsonify({"error": "Assistant API key is not configured."}), 503

    base_url = current_app.config.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = data.get("model") or "deepseek-chat"
    temperature = data.get("temperature", 0.2)

    client = _build_client(api_key, base_url)

    try:
        completion = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
        )
    except OpenAIError as exc:
        current_app.logger.exception("DeepSeek(OpenAI) request failed: %s", exc)
        return jsonify({"error": "Assistant upstream error."}), 502

    choice = completion.choices[0] if completion.choices else None
    answer = (choice.message.content.strip() if choice and choice.message and choice.message.content else "")
    if not answer:
        answer = "I could not generate an answer. Please try rephrasing the question."

    usage = getattr(completion, "usage", None)
    usage_dict = usage.model_dump() if hasattr(usage, "model_dump") else (usage or {})

    return jsonify({"answer": answer, "usage": usage_dict})
