"""Application configuration."""


class Settings:
    app_name = "Book Agent"
    version = "0.1.0"
    llm_provider = "mock"
    vector_store = "memory"


settings = Settings()
