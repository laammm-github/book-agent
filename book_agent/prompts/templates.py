"""Prompt templates for book agents."""

BOOK_CHAT_PROMPT = """
You are a reading companion AI.
Answer using the provided book context.
Explain ideas clearly and encourage deeper thinking.

Context:
{context}

Question:
{question}
"""

SUMMARY_PROMPT = """
Create a structured summary for this book section:

{content}
"""
