"""Generate review cards from reading notes."""


class FlashcardGenerator:
    def generate(self, notes: dict) -> list[dict[str, str]]:
        summary = notes.get("summary", "")
        return [
            {
                "question": "What is the key idea?",
                "answer": summary,
            }
        ]
