from pydantic_settings import BaseSettings ,SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION :str
    OPENAI_API_KEY :str
    FIle_MAX_SIZE : int
    FILE_ALLOWED_TYPES: list
    class config:
        env_file=".env"


#get setting function return odject from Settings

def get_settings():
    return Settings()