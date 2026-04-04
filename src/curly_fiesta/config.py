from dotenv import load_dotenv
import os

load_dotenv()


def get(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)
