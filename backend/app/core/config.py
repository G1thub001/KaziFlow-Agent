from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "KaziFlow Agent API"
    APP_VERSION: str = "0.1.0"

    DEBUG: bool = False

    DATABASE_URL: str
    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

    OPENROUTER_API_KEY: str

    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    MODEL_NAME: str = "openai/gpt-4.1-mini"


settings = Settings()