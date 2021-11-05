import os

import click

from scripts.base import _call


@click.command()
@click.option("-p", "--prefix", help="Run tests preceding with this prefix")
def test(prefix) -> None:
    os.environ["IV_ENVIRONMENT"] = "test"
    prefix = f" -k {prefix}" if prefix else ""
    _call(f"pytest --disable-pytest-warnings -v -s{prefix}")
