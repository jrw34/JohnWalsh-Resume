"""
Streamlit Application Containing An Interactive Resume.

If running locally, the current solution requires changing the db_web = True -> False
under __name__ == "__main__" at the bottom of the file
"""

import streamlit as st
from pathlib import Path

# Import util functions
from src.utils.AppGraphs.education_graph import education_treemap  # Education Section
from src.utils.AppGraphs.internship_graph import (
    animated_intern_graph,
)  # Internship Section
from src.utils.AppGraphs.skills_graph import skills_graph  # Skills section
from src.utils.spark_app_interface import (  # Simple NLP section
    classify_input,
    create_spark_instance,
    load_lrModel,
    load_pipeline,
)
from src.utils.AppDataStructs.graph_data import (  # Data For resume visualization
    fau_data,
    tdi_data,
    intern_data_map,
    intern_positions,
    skills_df,
)
from src.utils.AppDataStructs.section_descriptions import (
    section_descriptions,
)  # Text body data


def app(db_web: bool = True) -> None:
    """
    Run the streamlit app for local dev and web deployment.

    Input:
    -----
    db_web : Boolean that controls if deployment should use local vairables or streamlit secrets for db connection

    """
    # Create title
    st.title("John Walsh Resume")

    # Download Resume PDF button
    with open(Path("src/resume_data/John_Walsh_Resume.pdf"), "rb") as file:
        st.download_button(
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
        st.subheader("Data Source")
        st.write(section_descriptions["capstone"]["data_source"])

    if st.button("Cleaning and Processing the Data"):
        st.write(section_descriptions["capstone"]["cleaning_and_processing"])

    if st.button("Database Management and Interface"):
        st.write(section_descriptions["capstone"]["database_management_and_interface"])

    if st.button("Display Perfect Matches"):
        st.write(section_descriptions["capstone"]["display_perfect_matches"])

    capstone_toggler = st.toggle("View Ingredient Identifier")
    # Click toggle bar to activate Ingredient Identifier
    if capstone_toggler:
        # Display Capstone Project Images
        st.subheader("Input and Ingredient Display")
        st.image("src/resume_data/imgs/cap_proj_1.png")
        st.subheader("Query Selection")
        st.image("src/resume_data/imgs/cap_proj_2.png")
        st.subheader("Processed Query Visual Output")
        st.image("src/resume_data/imgs/cap_proj_3.png")

        st.write("""
                 The updated code for this project can be found by following the link in the 'Python code' section of this app.

                 The database has been shutdown due to avoiding costs associated with running it through AIVEN. Thus, the pictures are provided to
                 display what the application looked like while it was still operational.
                 """)

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

    # Model Overview and Diagram
    st.subheader("Model Diagram")
    st.image("src/resume_data/imgs/spark_model_diagram.png")

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

    # Add Sample Code Section
    st.header("Sample Code")
    st.subheader("Bayesian Likelihood in SQL")
    # create checkbox to display sample sql code
    sample_sql_check = st.checkbox("SQL Sample")
    if sample_sql_check:
        st.markdown(section_descriptions["sample_sql_code"])

    st.subheader("Python Code")
    st.write(
        "Follow the link to see the IngredientIdentifier code embedded in this application!"
    )
    st.link_button(
        "JohnWalsh-Resume/src/IngredientIdentifier/",
        "https://github.com/jrw34/JohnWalsh-Resume/tree/main/src/IngredientIdentifier",
    )
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
        "Find me on LinkedIn",
        "https://www.linkedin.com/in/john-walsh-90b0a82a0/",
    )


if __name__ == "__main__":
    # This enables local developement
    ## run command 'streamlit run resume_app.py"
    app(db_web=True)
