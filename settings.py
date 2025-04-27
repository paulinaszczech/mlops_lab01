from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str  # Zmienna środowiskowa
    APP_NAME: str  # Nazwa aplikacji

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        allowed_values = {"dev", "test", "prod"}
        if value not in allowed_values:
            raise ValueError(
                f"Invalid ENVIRONMENT value: {value}. Must be one of {allowed_values}."
            )
        return value
