import functools
from collections.abc import Callable
from typing import Any

import plotly.io as pio

from ..graphs import GRAPH_REGISTRY


def output_html[**P, T](func: Callable[P, T]) -> Callable[P, str]:
    @functools.wraps(func)
    def wrapper_output_html(*args: P.args, **kwargs: P.kwargs) -> str:
        div_id = func.__name__.replace("_", "-")
        return pio.to_html(
            fig=func(*args, **kwargs),
            full_html=False,
            include_plotlyjs=False,
            div_id=div_id,
        )

    return wrapper_output_html


def register[F: Callable[..., Any]](func: F) -> F:
    GRAPH_REGISTRY[func.__name__] = func
    return func


def graph[F: Callable[..., Any]](func: F) -> Callable[..., str]:
    return register(output_html(func))
