from .routes import chat_endpoint, books_endpoint


def create_app():
    return {
        "name": "book-agent-api",
        "routes": [chat_endpoint, books_endpoint],
    }


app = create_app()
