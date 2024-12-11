"""Module Storing Data Used for Populating Visualizations."""

import pandas as pd

# For Education Graph
fau_data: list[str] = [
    "BA in Interdisciplinary Mathematical Sciences (Honors)",
    "Focus Path <br> in Biochemistry",
    "Magna Cum Laude",
    "Recipient of Outstanding <br> Thesis Award",
    "Graduated: May 2023",
    "Mathematics Tutor <br> for 2 Years",
    "Computational Chemistry <br> Lab Volunteer",
]
tdi_data: list[str] = [
    "Data Scientist Certification",
    "The Data Incubator <br> Fellowship Program",
    "Graduated: Nov 2023",
    "Achieved > 90% <br> on all Assignments",
    "Capstone Project: <br> Ingredient Identifier",
]

# For Intern Graph
intern_data: dict[str, str] = {
    "company": "Company: 24/7 Software",
    "role": "Role: Buisiness Analyst Intern",
    "timeframe": "Timeframe: May 2022 - May 2023",
    "project": "Name of Paper: Spatiotemporal Determinants of Football Stadium Incidents",
    "project_desc1": "Goal and Scope: Initiated analysis of raw Stadium Incident Data (>1G) reported at one professional football stadium with the goal to quantitatively analyze stadium incident response times and predict incidents' occurrence and locations. Regularly presented work to senior leadership and extended initial analysis and modeling to include 20 professional sports stadiums.",
    "project_desc2": "Some work I did: Cleaned and processed the data, built regression models, and performed classification using Apriori Association Rules Mining (ARM) to analyze the spatiotemporal determinants of football stadium incidents.",
    "project_desc3": "More work I did: Constructed visualizations displaying the likelihood of incidents occurring in various stadium locations during various times",
    "project_desc4": "Insights: Model output elucidated operational inefficiencies particularly related to security incidents and ADA accessibility requests.",
    "results_1": "Results: 25.6% of accessibility requests occurred when the stadium gates opened.",
    "results_2": "Results: 9% of fan code of conduct violations occurred in a specific section of the stadium during the 2nd quarter.",
    "project impact": "Impact: Verified that data driven insights could be productionalized and introduced a model capable of productionalization. Currently, the company is developing a product that would improve venue operations based on time/location risk prediction.",
}

# This dictionary is used to populate data during intern_graph click functionality
## It acts as a multi-tier map where the x point is the first dict key
## For each x point the value is a dict of y points corresponding the text to populate upon click
intern_data_map: dict[int | float, dict[int, str]] = {
    0: {
        10: intern_data["company"],
        4: intern_data["project"],
        -5: intern_data["project impact"],
    },
    -1: {
        7: intern_data["role"],
        1: intern_data["project_desc2"],
    },
    1: {
        7: intern_data["timeframe"],
        1: intern_data["project_desc3"],
    },
    -2: {
        1: intern_data["project_desc1"],
    },
    2: {
        1: intern_data["project_desc4"],
    },
    -0.5: {
        -2: intern_data["results_1"],
    },
    0.5: {
        -2: intern_data["results_2"],
    },
}

# Positions for Intern Graph
intern_positions: dict[str, tuple[int | float, int]] = {
    "company": (0, 10),
    "role": (-1, 7),
    "timeframe": (1, 7),
    "project": (0, 4),
    "project_desc1": (-2, 1),
    "project_desc2": (-1, 1),
    "project_desc3": (1, 1),
    "project_desc4": (2, 1),
    "results_1": (-0.5, -2),
    "results_2": (0.5, -2),
    "project impact": (0, -5),
}


# Skills DataFrame
# Set value to ensure consistent sizing of chart slices
SUNBURST_VALUE: int = 5
# Skill Types (secondary ring)
analysis: str = "Analysis"
ml: str = "Machine Learning"
viz: str = "Visualization"
tech: str = "Technologies"
langs: str = "Languages"
tools: str = "Tools"
# Skill Categories (inner ring)
dev: str = "Developement"
ds: str = "Data Science"


skills_df = pd.DataFrame.from_records(
    [
        # Pass tuples of the form ('skill', 'type', 'value', 'category')
        # Tools Group in Dev
        ("Tensorflow", dev, SUNBURST_VALUE, tools),
        ("Scikit-Learn", dev, SUNBURST_VALUE, tools),
        ("MyPy", dev, SUNBURST_VALUE, tools),
        ("Ruff", dev, SUNBURST_VALUE, tools),
        ("Regex", dev, SUNBURST_VALUE, tools),
        ("pySpark", dev, SUNBURST_VALUE, tools),
        ("sqlalchemy", dev, SUNBURST_VALUE, tools),
        # ML Group in DS
        ("Pipeline Architecture", ds, SUNBURST_VALUE, ml),
        ("Deep Learning", ds, SUNBURST_VALUE, ml),
        ("Image Processing", ds, SUNBURST_VALUE, ml),
        ("Sentiment Analysis", ds, SUNBURST_VALUE, ml),
        ("Association Rules <br>  Mining", ds, SUNBURST_VALUE, ml),
        ("NLP", ds, SUNBURST_VALUE, ml),
        ("Model Selection", ds, SUNBURST_VALUE, ml),
        ("Text <br> Classification", ds, SUNBURST_VALUE, ml),
        ("Hyperparameter <br> Tuning", ds, SUNBURST_VALUE, ml),
        # Analysis Group in DS
        ("PostgreSQL", ds, SUNBURST_VALUE, analysis),
        ("MySQL", ds, SUNBURST_VALUE, analysis),
        ("Time-series <br> Analysis", ds, SUNBURST_VALUE, analysis),
        ("PCA", ds, SUNBURST_VALUE, analysis),
        ("Linear Algebra", ds, SUNBURST_VALUE, analysis),
        ("Probalistic Modeling", ds, SUNBURST_VALUE, analysis),
        ("Data Visualization", ds, SUNBURST_VALUE, analysis),
        ("XML", ds, SUNBURST_VALUE, analysis),
        ("HTML", ds, SUNBURST_VALUE, analysis),
        # Viz Group in Dev
        ("Plotly", dev, SUNBURST_VALUE, viz),
        ("Altair", dev, SUNBURST_VALUE, viz),
        ("Bokeh", dev, SUNBURST_VALUE, viz),
        ("Dash", dev, SUNBURST_VALUE, viz),
        ("Streamlit", dev, SUNBURST_VALUE, viz),
        # Tech Group in Dev
        ("Linux", dev, SUNBURST_VALUE, tech),
        ("Shell Scripting", dev, SUNBURST_VALUE, tech),
        ("Git/GitLab", dev, SUNBURST_VALUE, tech),
        ("CI/CD", dev, SUNBURST_VALUE, tech),
        ("Markdown", dev, SUNBURST_VALUE, tech),
        # Langs Group in Dev
        ("Python", dev, SUNBURST_VALUE, langs),
        ("Bash", dev, SUNBURST_VALUE, langs),
        ("MATLAB", dev, SUNBURST_VALUE, langs),
        ("Scala", dev, SUNBURST_VALUE, langs),
        ("SQL", dev, SUNBURST_VALUE, langs),
    ],
    columns=["skill", "type", "value", "category"],
)
