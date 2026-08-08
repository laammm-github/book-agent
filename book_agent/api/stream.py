"""Streaming response helpers for future chat streaming."""

from typing import Iterator


def stream_text(text: str) -> Iterator[str]:
    """Yield response chunks for UI streaming."""
    for part in text.split():
        yield part
