"""Script for populating the PostgreSQL DB with a cleaned and parsed dataframe."""

import os
# from sqlalchemy import create_engines

# Get DB url key from local variable
DB_URL = os.getenv("DB_URL")

# Read in local copy of data from USDA
# usda_data = ...

# Clean and Parse usda_data
# cleaned_and_parsed = ...

# Create engine to connect to PostgreSQL DB
# engine = create_engine(DB_URL)

# Create new table in DB to store cleaned_and_parsed
# cleaned_and_parsed.to_sql("usda", engine)
