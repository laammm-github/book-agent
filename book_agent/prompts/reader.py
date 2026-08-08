def build_reader_prompt(task: str, book: str | None = None) -> str:
    return f"""You are a professional reading mentor.

Book:
{book or 'Unknown'}

Question:
{task}

Please provide:
1. Core ideas
2. Important concepts
3. Further thinking questions
"""
