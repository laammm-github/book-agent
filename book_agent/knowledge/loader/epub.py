from pathlib import Path
import zipfile
from html.parser import HTMLParser

from .base import BookLoader
from ..models.book import Book, Chapter


class _HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        if data.strip():
            self.parts.append(data.strip())

    def text(self):
        return " ".join(self.parts)


class EPUBLoader(BookLoader):
    """Load EPUB files by extracting XHTML content."""

    def load(self, path: str) -> Book:
        source = Path(path)
        chapters = []

        try:
            with zipfile.ZipFile(source) as archive:
                documents = [
                    name for name in archive.namelist()
                    if name.endswith((".xhtml", ".html", ".htm"))
                ]

                for index, name in enumerate(documents):
                    parser = _HTMLTextExtractor()
                    parser.feed(archive.read(name).decode("utf-8", errors="ignore"))
                    text = parser.text()
                    if text:
                        chapters.append(
                            Chapter(
                                title=Path(name).stem,
                                content=text,
                                index=index,
                            )
                        )
        except (FileNotFoundError, zipfile.BadZipFile):
            pass

        return Book(
            title=source.name,
            chapters=chapters,
            metadata={
                "format": "epub",
                "source": str(source),
                "chapters": len(chapters),
            },
        )
