"""Tools to query and access the AIVEN PostgreSQL instance."""

from collections import Counter
from sqlalchemy import create_engine, text
import pandas as pd
import streamlit as st
import os
from src.IngredientIdentifier.ingredient_utils.query_processing import count_ingredients  # type: ignore[import-not-found]

# For use in user_query
QUERY_STRUCT: str = """
    SELECT brand_owner, brand_name, ingredient_list
    , description
    FROM usda
    WHERE
        description LIKE :select_item AND
        ingredient_list LIKE ANY(:prioritize) AND
        NOT ingredient_list LIKE ANY(:avoid)

    """

# For use in get_ingredient_counts
COUNT_QUERY_STRUCT: str = """
    SELECT ingredient_list
    FROM usda
    WHERE description LIKE :select_item

    """


def create_regex_containment(target_words: list[str]) -> str:
    """
    Convert list of strings into regex for checking containment in postgresql query.

    Input:
    -----
    target_words: Either prioritize or avoid args in user_query()

    Return:
    ------
    regex_containment: Regex of the form '{%word 1%, %word 2%, ..., %word n%}'
    """
    # Define begining of regex
    regex_containment = "{"
    for word in target_words:
        regex_containment += f"%{word.upper()}%,"

    # Add end tag to replace w/ '}'
    regex_containment += "END OF REGEX"

    return regex_containment.replace(",END OF REGEX", "}")


def user_query(
    search_item: str,
    prioritize: list[str],
    avoid: list[str],
    db_web: bool,
) -> pd.DataFrame:
    """
    Accept user input and return dataframe from postgresql query.

    Input:
    -----
    search_item : String w/ item name to query
    prioritize  : List of strings w/ ingredients/additives to look for
    avoid       : List of strings w/ ingredients/additives to exclude
    db_web      : Bool flag that is True if streamlit, False if local

    Return:
    ------
    queried_usda: Dataframe containing only items with prioritized ingredients

    """
    if db_web is False:
        DB_URL = str(os.environ["DB_URL"]).replace("postgres", "postgresql")
    else:
        DB_URL = st.secrets["DB_URL"]

    # Create sqlalchemy engine
    engine = create_engine(DB_URL)

    # Define Query Params for safe user input
    params = {
        "select_item": search_item.upper(),
        "prioritize": create_regex_containment(prioritize),
        "avoid": create_regex_containment(avoid),
    }
    # Create Query body
    query = text(QUERY_STRUCT)

    # Connect, query, close
    with engine.connect() as conn:
        results = conn.execute(query, params).fetchall()
        conn.close()

    return pd.DataFrame(results)


def get_ingredient_counts(search_item: str, db_web: bool) -> tuple[Counter, int]:
    """
    Get 25 Most Commmon Ingredients For Requested Item.

    Input:
    -----
    search_item : String Containing Item name to query in db (e.g. Orange Juice)
    db_web      : Bool flag that is True if streamlit, False if local

    Return:
    ------
    ingredient_info: Tuple containing (top_25_ingredients, total_ingredients)

    """
    if db_web is False:
        DB_URL = str(os.environ["DB_URL"]).replace("postgres", "postgresql")
    else:
        DB_URL = st.secrets["DB_URL"]

    # Create sqlalchemy engine
    engine = create_engine(DB_URL)

    # Define Query Params for safe user input
    params = {"select_item": search_item.upper()}
    # Create Query body
    query = text(COUNT_QUERY_STRUCT)

    # Connect, query, close
    with engine.connect() as conn:
        results = conn.execute(query, params).fetchall()
        conn.close()

    ingredient_counts = count_ingredients(results)  # type: ignore[arg-type]
    total_counts: int = len(set(ingredient_counts.keys()))

    return (ingredient_counts, total_counts)
