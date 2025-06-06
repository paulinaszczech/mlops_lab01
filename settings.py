from pydantic_settings import BaseSettings
from pydantic import field_validator
import os
import yaml


class Settings(BaseSettings):
    ENVIRONMENT: str  # Zmienna środowiskowa
    APP_NAME: str  # Nazwa aplikacji

    @field_validator("ENVIRONMENT")
    def validate_environment(cls, value):
        allowed_values = {"dev", "test", "prod"}
        if value not in allowed_values:
            raise ValueError(
                f"Invalid ENVIRONMENT value: {value}. Must be one of {allowed_values}."
            )
        return value


with open("secrets.yaml", "r") as file:
    secrets = yaml.safe_load(file)

# Załadowanie wartości do zmiennych środowiskowych
os.environ["API_KEY"] = secrets["api_key"]

print(f"API Key: {os.environ['API_KEY']}")
