"""Module for Cleaning, Merging, and Parsing Text from USDA data."""

import pandas as pd
import re

# Regexs
CONTAINS_RE: str = r"CONTAIN[S|:]?\+?[ING]"  # Tags: contain(s)(ing)
LESS_THAN_RE: str = (
    r"LESS THAN [0-9|\.{0,3}]*%?\s?:?(EACH|OF)?:?"  # Tags: less than x% of each
)
PCT_OR_LESS_RE: str = (
    r"[0-9|.]{0,3}\%?\s?(OR)?\sLESS (OF:?)?"  # Tags: x% or less than of
)

# Strings to be replaced with commas
COMMA_TAGS = [
    ".CONTAINS:",
    "CONTAINS",
    " CONTAINS",
    " - ",
    " (",
    ")",
    " [",
    "]",
    " {",
    "}",
    ":",
    ";",
]

# Strings to be replaced with empty spaces ("")
EMPTY_TAGS = [
    "INGREDIENTS:",
    " FOR COLOR",
    "*",
    "CONSISTS OF",
    "CONSIST OF",
    "ONE OR MORE OF THE FOLLOWING",
    "OF THE FOLLOWING",
    "THE FOLLOWING",
    "PRESERVATIVES",
    "AS A PRESERVATIVE",
    "FOR TARTNESS",
    "TO PRESERVE FRESHNESS",
    "TO PREVENT CAKING",
    "ANTI-CAKING AGENT",
    "ANTICAKING AGENT",
    "FOR COLOR",
    "COLOR ADDED",
    "EACH",
    "PRESERVATIVE",
    "USED FOR",
    "USED AS A",
    "USED",
    " *",
    "* ",
    ".",
]


# remove all statements relating to additive or contents
def additive_tag_removal(
    ingredient_list: str,
    contains_re: str = CONTAINS_RE,
    less_than_re: str = LESS_THAN_RE,
    pct_or_less_re: str = PCT_OR_LESS_RE,
) -> str:
    """
    Remove all tags caught in re expressions for additives.

    Input:
    -----
    ingredient_list : Str from USDA's branded_food.csv
    contains_re     : Regex to tag strings with 'containing'
    less_than_re    : Regex to tag string with 'less than x% of each'
    pct_or_less_re  : Regex to tag string with 'x% of less than of'

    Returns
    -------
    ingredients_tags_removed : Str where tags replaced with " "

    """
    # Sub contains
    sub1: str = re.sub(contains_re, " ", ingredient_list)

    # Sub less than
    sub2: str = re.sub(less_than_re, " ", sub1)

    # Sub pct or less
    ingredients_tags_removed: str = re.sub(pct_or_less_re, " ", sub2)

    return ingredients_tags_removed


# Parse ingredient string into list of strings
def ingredient_parser(
    ingredients_tags_removed: str,
    comma_tags: list[str] = COMMA_TAGS,
    empty_tags: list[str] = EMPTY_TAGS,
) -> list[str]:
    """
    Construct a list of cleaned food ingredients from a single ingredient string.

    Input:
    -----
    ingredients_tags_removed : String returned from additive_tag_removal()
    comma_tags               : List of Strings to replace with commas
    empty_tags               : List of Strings to replace with empty spaces

    Returns
    -------
    parsed_ingredients : List of ingredients with filler words removed from ingredient label

    """
    # Normalize input_str and replace "PERCENT" with "%"
    normed_str: str = (
        str(ingredients_tags_removed)
        .upper()
        .replace(" PERCENT", " %")
        .replace("PERCENT", "%")
    )

    # Replace substrings with ""
    for tag in empty_tags:
        normed_str = normed_str.replace(tag, "")

    # Replace substrings with ","
    for tag in comma_tags:
        normed_str = normed_str.replace(tag, ",")

    # Remove additive tags
    removed_tags: str = additive_tag_removal(normed_str)

    return [
        str(i).strip().rstrip(".")
        for i in removed_tags.split(",")
        if str(i).strip().rstrip(".") not in {"", " "}
    ]


# Create cleaned, parsed, merged dataframe
def clean_parse_merge(branded: pd.DataFrame, food: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and parsed branded and return merged with food.

    Input:
    -----
    branded : DataFrame read from USDA 'branded_food.csv'
    food    : DataFrame read from USDA 'food.csv'

    Returns
    -------
    usda: DataFrame consisting of the cleaned/parsed branded_data merged with food_data

    """
    # Merge DataFrames
    usda = branded.merge(food, on="fdc_id")

    # Convert 'ingredients' into 'ingredient_list'
    usda["ingredient_list"] = usda.ingredients.apply(lambda x: ingredient_parser(x))

    # Drop Null 'description'
    usda.dropna(axis=0, subset="description", inplace=True)

    # Normalize 'description'
    usda.loc[:, "description"] = usda.loc[:, "description"].apply(str.upper)

    return usda[["brand_owner", "brand_name", "ingredient_list", "description"]]
