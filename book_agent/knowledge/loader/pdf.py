from pathlib import Path

from .base import BookLoader
from ..models.book import Book, Chapter


class PDFLoader(BookLoader):
    """Load PDF books and extract text chapters.

    Uses pypdf when available. The loader keeps metadata even when
    extraction dependencies are unavailable.
    """

    def load(self, path: str) -> Book:
        source = Path(path)
        chapters = []

        try:
            from pypdf import PdfReader

            reader = PdfReader(str(source))
            for index, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                if text.strip():
                    chapters.append(
                        Chapter(
                            title=f"Page {index + 1}",
                            content=text,
                            index=index,
                        )
                    )
        except ImportError:
            pass

        return Book(
            title=source.name,
            chapters=chapters,
            metadata={
                "format": "pdf",
                "source": str(source),
                "pages": len(chapters),
            },
        )
