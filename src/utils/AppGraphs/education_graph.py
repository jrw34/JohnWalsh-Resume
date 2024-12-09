"""Module Containing Education Treemap."""

import plotly.graph_objects as go  # type: ignore[import-untyped]
from plotly.subplots import make_subplots  # type: ignore[import-untyped]


# def function to return plotly figure displaying Treemap containing education data
def education_treemap(
    tdi_data: list[str],
    fau_data: list[str],
    color_1: str,
    color_2: str,
    sector_bg_color: str,
    sector_font_color: str,
) -> go.Figure:
    """
    Create Plotly Treemap containing education data.

    Input:
    -----
    tdi_data          : TDI Info from AppDataStructs.graph_data
    fau_data          : FAU Info from AppDataStructs.graph_data
    color_1           : Top Level Box Color
    color_2           : Bottom Level Box Color
    sector_bg_color   : Underlying Box Color
    sector_font_color : Text Color in all Boxes

    Returns
    -------
    education_trees : Treemap with each branch containing an education section

    """
    # create subplot template
    education_trees = (
        make_subplots(
            cols=2,
            rows=1,
            column_widths=[0.4, 0.6],
            subplot_titles=("The Data Incubator", "Florida Atlantic University"),
            specs=[[{"type": "treemap", "rowspan": 1}, {"type": "treemap"}]],
        )
        .add_trace(
            go.Treemap(  # add TDI trace to subplot figure
                labels=tdi_data,
                parents=[""] + [tdi_data[0]] * 4,
                values=[16] + [4] * 4,
                branchvalues="total",
                insidetextfont=dict(size=15),
                outsidetextfont=dict(size=25),
                hoverinfo="skip",
                marker_colors=[sector_bg_color] + [color_1, color_2] * 2,
                textfont=dict(size=18, color=sector_font_color),
            ),
            row=1,
            col=1,
        )
        .add_trace(
            go.Treemap(  # add FAU trace to subplot figure
                labels=fau_data,
                parents=[""] + [fau_data[0]] * 6,
                values=[18] + [3] * 6,
                branchvalues="total",
                hoverinfo="skip",
                insidetextfont=dict(size=15),
                outsidetextfont=dict(size=25),
                marker_colors=[sector_bg_color] + [color_1, color_2] * 3,
                textfont=dict(size=18, color=sector_font_color),
            ),
            row=1,
            col=2,
        )
        .update_annotations(yshift=20, font_size=28, font_color=sector_font_color)
    )

    # return plotly figure object
    return education_trees
