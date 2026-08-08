"""Generate structured reading notes."""


class NoteGenerator:
    def generate(self, title, summary, insights=None):
        return {
            "title": title,
            "summary": summary,
            "insights": insights or [],
        }
