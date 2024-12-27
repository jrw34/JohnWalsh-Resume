"""Script for populating the PostgreSQL DB with a cleaned and parsed dataframe."""

import os
from pathlib import Path
import pandas as pd

from clean_merge_parse import clean_parse_merge  # type: ignore[import-not-found]
from sqlalchemy import create_engine

# Get DB url key from local variable
DB_URL = str(os.getenv("DB_URL")).replace("postgres", "postgresql")

# Read in local copies of data from USDA
usda_data = pd.read_csv(
    Path("src/IngredientIdentifier/FoodData_Central_csv_2024-10-31/branded_food.csv"),
    low_memory=False,
)
food_data = pd.read_csv(
    Path("src/IngredientIdentifier/FoodData_Central_csv_2024-10-31/food.csv"),
    low_memory=False,
)

# Clean, Parse, and Merge usda_data
cleaned_and_parsed = clean_parse_merge(usda_data, food_data)

# Create engine to connect to PostgreSQL DB
engine = create_engine(DB_URL)

# Create new table in DB to store cleaned_and_parsed
cleaned_and_parsed.to_sql("usda", engine, if_exists="replace", index=False)
