import os

import plotly.graph_objects as go

from ..util.html import output_html


def main() -> str:
    """
    1. Get the data
    2. manipulate/format into x vs y
    3. create the graph
    """
    x = [1, 6, 3, 2, 5, 9]
    y = [4, 3, 2, 2, 5, 6]
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=y,
            )
        ]
    )

    fig.update_layout(title="My first chart")

    return output_html(fig=fig, div_id=os.path.basename(__file__).removesuffix(".py"))
