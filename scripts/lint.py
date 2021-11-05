from scripts.base import _call

files = ["src/", "scripts/"]


def lint() -> None:
    _call("black --check", files)


def fix() -> None:
    _call("isort", files)
    _call("black", files)
