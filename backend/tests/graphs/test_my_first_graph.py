import pytest  # noqa: F401

from backend.app.graphs import my_first_graph
from backend.app.util.decorators import GRAPH_REGISTRY


def test_decorator() -> None:
    assert isinstance(my_first_graph.my_first_graph(), str)
    assert isinstance(GRAPH_REGISTRY["my_first_graph"](), str)
