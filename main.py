import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file = f".env.{environment}"
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Plik {env_file} nie istnieje.")
    load_dotenv(env_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Wczytaj zmienne środowiskowe z odpowiedniego pliku .env."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="Środowisko do wczytania (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
