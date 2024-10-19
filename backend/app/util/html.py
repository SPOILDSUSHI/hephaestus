from typing import Any

import plotly.io as pio


def output_html(fig=Any, div_id=str) -> str:

    return pio.to_html(
        fig=fig,
        full_html=False,
        include_plotlyjs=False,
        div_id=div_id,
    )
