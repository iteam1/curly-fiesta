import os
from curly_fiesta.config import get


def test_get_existing_key(monkeypatch):
    monkeypatch.setenv("APP_NAME", "curly-fiesta")
    assert get("APP_NAME") == "curly-fiesta"


def test_get_missing_key_with_default():
    assert get("NON_EXISTENT_KEY", "fallback") == "fallback"


def test_get_missing_key_no_default():
    assert get("NON_EXISTENT_KEY") is None
