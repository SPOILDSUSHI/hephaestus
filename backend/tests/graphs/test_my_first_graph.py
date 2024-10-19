import pytest  # noqa: F401

from backend.app.graphs import my_first_graph


def test_output() -> None:
    assert isinstance(my_first_graph.main(), str)
