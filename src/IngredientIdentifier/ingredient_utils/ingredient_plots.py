"""Module for generating plots from usda DB query output."""

from collections import Counter
import plotly.graph_objects as go  # type: ignore[import-untyped]
import pandas as pd

from src.IngredientIdentifier.ingredient_utils.query_processing import HDAG


def plot_ingredient_counts(ingredient_counts: Counter, search_item: str) -> go.Figure:
    """
    Display 25 Most Common Ingredients From User Item Query.

    Input:
    -----
    ingredient_counts : Top 25 Most Common Ingredients from db_tools.get_ingredient_counts()[0]
    search_item       : Input Text from query_item_input

    Return:
    ------
    ingredient_count_figure : Figure Object displaying horizontal count plot

    """
    top_25_ingredients: list[tuple[str, int]] = ingredient_counts.most_common(25)
    ingredient_names = [count[0] for count in top_25_ingredients]
    count_per_ingredient = [count[1] for count in top_25_ingredients]
    count_fig = go.Figure(
        go.Bar(
            x=count_per_ingredient,
            y=ingredient_names,
            orientation="h",
            # Display Counts Inside the Bars
            text=count_per_ingredient,
            textposition="inside",
        ),
        layout={
            "title": {
                "text": f"Top 25 Most Common Ingredients in {search_item}",
                "yanchor": "top",
            }
        },
    )
    return count_fig


def hdag_plot(
    user_queried_data: pd.DataFrame,
    parent_col: str,
    child_col: str,
    grandchild_col: str,
) -> go.Figure:
    """
    Heirarchically Directed Acyclic Graphs (HDAGs) For 3-tiered relationships.

    Input:
    -----
    user_queried_data : Resultant dataframe from db_tools.user_query()
    parent_col        : String column name of parent nodes in data
    child_col         : String column name of child nodes in data
    grandchild_col    : String column name of grandchild nodes in data

    Return:
    ------
    hdag_figure : Plotly figure displaying HDAG with the heirachy Parent -> Child -> Grandchild
                  for each brand in user_queried_data

    """
    # Create HDAG from user_queried_data
    query_hdag = HDAG(user_queried_data, parent_col, child_col, grandchild_col).hdag

    # Create Parent Trace
    parent_trace = go.Scatter(
        name=parent_col.upper(),
        x=query_hdag["parent_x"],
        y=query_hdag["parent_y"],
        mode="text",
        text=query_hdag["parent_text"],
        textposition="top center",
    )
    # Create Child Trace
    child_trace = go.Scatter(
        name=child_col.upper(),
        x=query_hdag["child_x"],
        y=query_hdag["child_y"],
        mode="markers",
        hovertemplate=query_hdag["child_text"],
        hoverinfo="text",
    )
    # Create Grandchild Trace
    grandchild_trace = go.Scatter(
        name=grandchild_col.upper(),
        x=query_hdag["grandchild_x"],
        y=query_hdag["grandchild_y"],
        mode="markers",
        hovertemplate=query_hdag["grandchild_text"],
    )

    # Instantiate emtpy 'edges' list
    edges: list[go.layout.Annotation] = []

    # Create List of all parent-child node edges
    for i in range(len(query_hdag["child_x_ref"])):
        child_edge = go.layout.Annotation(
            {
                "ax": query_hdag["child_x_ref"][i],
                "ay": query_hdag["child_y_ref"][i],
                "axref": "x",
                "ayref": "y",
                "x": query_hdag["child_x"][i],
                "y": query_hdag["child_y"][i],
                "xref": "x",
                "yref": "y",
                "arrowcolor": "silver",
                "arrowsize": 0.6,
                "showarrow": True,
                "arrowhead": 1,
            }
        )

        edges.append(child_edge)

    # Create List of all child-grandchild node edges
    for i in range(len(query_hdag["grandchild_x_ref"])):
        grandchild_edge = go.layout.Annotation(
            {
                "ax": query_hdag["grandchild_x_ref"][i],
                "ay": query_hdag["grandchild_y_ref"][i],
                "axref": "x",
                "ayref": "y",
                "x": query_hdag["grandchild_x"][i],
                "y": query_hdag["grandchild_y"][i],
                "xref": "x",
                "yref": "y",
                "arrowcolor": "silver",
                "arrowsize": 0.6,
                "showarrow": True,
                "arrowhead": 1,
            }
        )

        edges.append(grandchild_edge)

    # Create plotly figure
    hdag_figure = go.Figure(
        data=[parent_trace, child_trace, grandchild_trace],
        layout=go.Layout(
            title="All matches for requested item/criteria",
            annotations=edges,
            yaxis={"visible": False, "showticklabels": False},
            xaxis={"visible": False, "showticklabels": False},
        ),
    )

    return hdag_figure
