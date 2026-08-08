from ..models.book import Chapter


class ChapterParser:
    def parse(self, content: str) -> list[Chapter]:
        sections = [item.strip() for item in content.split("\n\n") if item.strip()]
        return [Chapter(title=f"Chapter {i + 1}", content=text, index=i)
                for i, text in enumerate(sections)]
