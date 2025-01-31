from pydantic_settings import BaseSettings, SettingsConfigDict

class BotSettings(BaseSettings):
    api_token: str

    model_config = SettingsConfigDict(env_prefix="bot_", env_file=".env")