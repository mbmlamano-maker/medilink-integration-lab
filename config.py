import os


def get_api_key() -> str:
    return os.getenv("MEDILINK_API_KEY", "local-demo-key")


def get_request_timeout() -> int:
    raw = os.getenv("REQUEST_TIMEOUT", "5")
    value = int(raw)
    if value <= 0:
        raise ValueError("REQUEST_TIMEOUT must be greater than zero")
    return value
