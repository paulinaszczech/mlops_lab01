# ruff: noqa: E402

import sys
import os
from dotenv import load_dotenv


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from settings import Settings

load_dotenv(dotenv_path=".env.test")


def test_settings_load_correctly():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MyAppTest"
