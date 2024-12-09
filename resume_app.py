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
    intern_data,
    intern_positions,
    skills_data,
)
from src.utils.AppDataStructs.section_descriptions import section_descriptions

# create title
st.title("John Walsh Resume (Currently Rebuilding ...)")

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
    col_1.markdown(section_descriptions["reference_section"])
    col_2.image("src/resume_data/imgs/headshot.png")

# About Me
st.subheader("About Me")
st.write(section_descriptions["about_me"])

# education graph
st.header("Education")

# generate education_treemap
edu_graph = education_treemap(
    tdi_data,
    fau_data,
    color_1="#94E3FE",
    color_2="#FFC677",
    sector_bg_color="#D4E3FE",
    sector_font_color="#1A0A53",
)
st.plotly_chart(edu_graph)

st.write("""[Return to top](#sections) """)
# Describe Tutoring Role and Timeframe
st.subheader("Mathematics Tutor at Florida Atlantic University")
st.write(section_descriptions["tutoring"])

# Describe Volunteer Role at Computational Chemistry Lab
st.subheader("Computational Chemistry Laboratory Volunteer")
st.write(section_descriptions["chem_lab"])

# Internship graph
st.header("Internship")
st.write("""
        Click 'Build Graph' to build the visualization and hover over the data poins to view the corresponding information.
        """)

# Generate animated_intern_graph
intern_graph = animated_intern_graph(intern_data, intern_positions)
st.plotly_chart(intern_graph)

# Embed thesis hyperlink
st.write(
    "This work was also my senior thesis at FAU, you can click the button 'View Paper' below to find the paper hosted on github."
)
st.write(section_descriptions["thesis"])

st.link_button(
    "View Paper: Spatiotemporal Determinants of Football Stadium Incidents",
    "https://github.com/jrw34/ThesisJW_PDF/blob/main/JW_Thesis_pdf2.pdf",
)

st.write("""[Return to top](#sections) """)

# Skills graph
st.header("Skills")
st.write(
    "Click within the inner two circles to toggle view, center click to toggle back"
)

# Generate skills_graph
skill_graph = skills_graph(skills_data)
st.plotly_chart(skill_graph)

st.write("""[Return to top](#sections) """)

# Capstone Project
st.header("Ingredient Identifier")

st.subheader("Capstone Project For The Data Incubator Fellowship Program")

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

st.write("""[Return to top](#sections) """)

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

# Add sesction about process of building the site
st.header("How I built this")
st.write(section_descriptions["how_i_built_this"])

st.header("Contact Info")
st.write("""
        email: johnrwalsh34@gmail.com
        """)
st.write("""[Return to top](#sections) """)
