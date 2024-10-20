import pytest  # noqa: F401

from backend.app.graphs import GRAPH_REGISTRY
from backend.app.graphs import my_first_graph


def test_decorator() -> None:
    assert isinstance(my_first_graph.my_first_graph(), str)
    assert isinstance(GRAPH_REGISTRY["my_first_graph"](), str)
