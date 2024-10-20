import functools
from collections.abc import Callable
from typing import Any

import plotly.io as pio


def output_html[F: Callable[..., Any]](func: F) -> F:
    @functools.wraps(func)
    def wrapper_output_html(*args, **kwargs) -> str:
        div_id = func.__name__.replace("_", "-")
        return pio.to_html(
            fig=func(*args, **kwargs),
            full_html=False,
            include_plotlyjs=False,
            div_id=div_id,
        )

    return wrapper_output_html
