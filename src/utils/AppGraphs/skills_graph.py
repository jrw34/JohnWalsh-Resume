"""Module Containing Skills Graph sunburst plot."""

import plotly.express as px  # type: ignore[import-untyped]
import pandas as pd


# Def function to display skills data in a px sunburst chart
def skills_graph(skills_df: pd.DataFrame) -> px.sunburst:
    """
    Display skills using an interactive sunburst chart.

    Input:
    -----
    skills_df: pd.DataFrame containing columns: ['type', 'category', 'skill', 'value']

    Returns
    -------
    skills_fig : px.sunburst figure object

    """
    skills_fig = (
        px.sunburst(
            data_frame=skills_df,
            path=["type", "category", "skill"],
            values="value",
            color="category",
        )
        .update_layout(
            margin=dict(t=0, l=0, r=0, b=40, pad=4),
            width=800,
            height=800,
            font=dict(size=20, color="white"),
        )
        .update_traces(
            hovertemplate="------------------- <br> %{label} <br> ------------------- <br> %{parent}",
            hoverlabel=dict(font=dict(size=15)),
        )
    )

    # Return skills_fig
    return skills_fig
