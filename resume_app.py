"""Streamlit Application Containing An Interactive Resume."""

import streamlit as st
from pathlib import Path

# Import util functions
from src.utils.AppGraphs.education_graph import education_treemap
from src.utils.AppGraphs.internship_graph import animated_intern_graph
from src.utils.AppGraphs.skills_graph import skills_graph
from src.utils.spark_app_interface import (
    classify_input,
    create_spark_instance,
    load_lrModel,
    load_pipeline,
)
from src.utils.AppDataStructs.graph_data import (
    fau_data,
    tdi_data,
    intern_data_map,
    intern_positions,
    skills_df,
)
from src.utils.AppDataStructs.section_descriptions import section_descriptions

# Create title
st.title("John Walsh Resume")

# Download Resume PDF button
with open(Path("src/resume_data/John_Walsh_Resume.pdf"), "rb") as file:
    btn = st.download_button(
        label="Click Here to Download My Tradtional Resume as a PDF",
        file_name="John_Walsh_Resume.pdf",
        data=file,
        mime="application/pdf",
    )

# Reference Section and Headshot container
with st.container():
    col_1, col_2 = st.columns([2, 1])
    col_1.markdown(
        """ ##### Welcome to my streamlit app! The blue underlined text can be clicked to easily navigate the page. You can also use the 'Sections' sidebar."""
    )
    col_1.markdown(section_descriptions["experience_section"])
    col_2.image("src/resume_data/imgs/headshot.png")

# SciTec
st.subheader("SciTec")
st.markdown(section_descriptions["scitec_description"])

# The Data Incubator
st.subheader("The Data Incubator (TDI)")
st.markdown(section_descriptions["tdi_overview"])
# Capstone Project
st.subheader("TDI Capstone Project: Ingredient Identifier")
# Display images from capstone project
if st.button("Data and Motivation"):
    st.write(section_descriptions["capstone"]["data_and_motivation"])

if st.button("Cleaning and Processing the Data"):
    st.write(section_descriptions["capstone"]["cleaning_and_processing"])

if st.button("Database Management and Interface"):
    st.write(section_descriptions["capstone"]["database_management_and_interface"])

if st.button("Display Perfect Matches"):
    st.write(section_descriptions["capstone"]["display_perfect_matches"])

capstone_toggler = st.toggle("Display Capstone Project")
if capstone_toggler:
    st.write("Input Food Item")
    st.image("src/resume_data/imgs/cap_proj_1.png")
    st.write("Select Desired Features")
    st.image("src/resume_data/imgs/cap_proj_2.png")
    st.write("Display Query Results")
    st.image("src/resume_data/imgs/cap_proj_3.png")

st.write(section_descriptions["capstone"]["data_source"])

# Internship
st.markdown(section_descriptions["intern_overview"])
st.write(section_descriptions["thesis"])
st.markdown("""
        ##### Click 'Build Graph' to build the visualization.
        ###### Then click each data point to view the corresponding information.
        """)
# Generate animated_intern_graph
intern_graph = animated_intern_graph(intern_positions)
intern_plot = st.plotly_chart(intern_graph, on_select="rerun")
try:
    # Use x,y coords of click data to get description from intern_data_map
    st.html(
        """<b> """
        + intern_data_map[intern_plot.selection["points"][0]["x"]][  # type: ignore[attr-defined]
            intern_plot.selection["points"][0]["y"]  # type: ignore[attr-defined]
        ]
        + """<b>"""
    )  # type: ignore[attr-defined]
except IndexError:
    st.write("Click on a Data Point to view the information.")
else:
    st.write("")

# Embed thesis hyperlink
st.link_button(
    "View Paper: Spatiotemporal Determinants of Football Stadium Incidents",
    "https://github.com/jrw34/ThesisJW_PDF/blob/main/JW_Thesis_pdf2.pdf",
)

# Education graph
st.header("Education")

# Generate education_treemap
edu_graph = education_treemap(
    tdi_data,
    fau_data,
    color_1="#94E3FE",
    color_2="#FFC677",
    sector_bg_color="#D4E3FE",
    sector_font_color="#1A0A53",
)
st.plotly_chart(edu_graph)

# Describe Tutoring Role and Timeframe
st.subheader("Mathematics Tutor at Florida Atlantic University")
st.write(section_descriptions["tutoring"])

# Describe Volunteer Role at Computational Chemistry Lab
st.subheader("Computational Chemistry Laboratory Volunteer")
st.write(section_descriptions["chem_lab"])

# Skills graph
st.header("Skills")
st.write(
    "Click within the inner two circles to toggle view, center click to toggle back"
)

# Generate skills_graph
skill_graph = skills_graph(skills_df)
st.plotly_chart(skill_graph)

# Embed emotion classification spark model
st.header("pySpark Text Classification Model")
st.subheader("A simple emotion classifier built using spark")

st.write(section_descriptions["pyspark"]["build_description"])

# Checkbox to explain model performance
model_perf_check = st.checkbox("Model Performance")
if model_perf_check:
    st.write(section_descriptions["pyspark"]["model_performance"])

# Checkbox to explain hyperparameter tuning
hyperparam_check = st.checkbox("Hyperparameter Tuning")
if hyperparam_check:
    st.write(section_descriptions["pyspark"]["hyperparams"])

# Checkbox to show some examples of the model input/output
examples_check = st.checkbox("Examples")
if examples_check:
    st.write(section_descriptions["pyspark"]["example_outputs"])

# Describe input format
st.write(section_descriptions["pyspark"]["input_guide"])

# Load sqlContext
sqlContext = create_spark_instance()

# Load lrModel
lrModel = load_lrModel("src/SparkModel/lrModel_emotions.model")

# Load fitPipeline
fitPipeline = load_pipeline("src/SparkModel/lrModel_transformation_pipe")

# User input
input_text = st.text_input("Input sentence here")

if input_text:
    st.write(f"User Input: {input_text}")

    # Classify_text
    classifier_pred = classify_input(input_text, sqlContext, fitPipeline, lrModel)
    st.write(f"Did your text describe {classifier_pred}?")

st.write(section_descriptions["pyspark"]["data_source"])

# Create sidebar
with st.sidebar:
    st.markdown(section_descriptions["reference_section"])

# Add section about process of building the site
st.header("How I built this")
st.write(section_descriptions["how_i_built_this"])

# Add About Me
st.header("About Me")
st.write(section_descriptions["about_me"])
# Add Contact Info
st.subheader("Contact Info")
st.write("""
        email: johnrwalsh34@gmail.com
        """)
st.link_button(
    "Find Me on LinkedIn",
    "https://www.linkedin.com/in/john-walsh-90b0a82a0/",
)
