from pydantic_settings import BaseSettings
from pydantic import validator, ValidationError


class Settings(BaseSettings):
    ENVIRONMENT: str  # Zmienna środowiskowa
    APP_NAME: str  # Nazwa aplikacji

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        allowed_values = {"dev", "test", "prod"}
        if value not in allowed_values:
            raise ValidationError(
                f"Nieprawidłowa wartość dla ENVIRONMENT: '{value}'. "
                f"Dozwolone wartości to {allowed_values}."
            )
        return value
