FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -e . || true

CMD ["python", "-m", "book_agent.cli.main"]
