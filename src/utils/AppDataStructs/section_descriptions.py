"""File containing data structures used in section description population."""

from typing import TypedDict, Dict

reference_markdown: str = """
                ## Sections

                [Home](#john-walsh-resume)

                [Experience](#experience)

                [Education](#education)

                [Skills](#skills)

                [pySpark Text Classification](#pyspark-text-classification-model)

                [How I Built This](#how-i-built-this)

                [About Me + Contact Info](#about-me)

                """

experience_section: str = """
            ## Experience

            [Associate Analyst @ SciTec](#scitec)

            [Data Science Fellow @ The Data Incubator](#the-data-incubator)

            [Business Analyst Intern @ 24/7 Software](#internship)

            """

about_me_description: str = """

        I am a Python Developer and Data Scientist who is enthusiastic about learning new technologies
        and adapting to the ever expanding state of innovation.

        Data is a feature of the modern world capable of drastically improving our quality of life, and I am thrilled to participate
        in bringing data to life.

        With firm belief in hard work, I persistently strive to produce meaningful,
        well documented, and reproducible results built from an adequate mathematical
        foundation.

        Furthermore, I hold communication as essential in the development
        process and there is little value in improperly communicated insights derived from data.

        Beyond my interests as a developer I often find myself trail running or travelling when the opportunities arise.

        """

tutoring_description: str = """
        From: Jan. 2021 - May 2023

        Courses Tutored: Matrix Theory, Introduction to Statistics,
        Calculus 1,2 & 3, and Differential Equations

        Found success by identifying real world applications of the pertinant mathematics
        when tutoring students with nontechnical backgrounds.
        """

comp_chem_descrption: str = """
        From: May 2021 - Aug. 2021

        Performed least squares optimization (analytically) using SVD in a Linux environment to project data points
        onto a best-fit plane in 3-D. As a result, enabled better assessment of molecular interactions in the dynamic model.

        """

intern_overview: str = """
        ### Internship

        ##### Position: Business Analyst Intern

        ###### From: May 2022 - May 2023

        - Built proof of concept ML model and data visualization capabilities to utilize previously unused customer data

        - Frequently presented my findings and results to a Senior Product Manager and other Senior Leadership

        - Work enabled better allocation of entertainment venue staff during events

        """

thesis_description: str = """
            This work was also my senior thesis at FAU.
            It was a great opportunity to work on a project from start to finish.
            My project entailed retrieving the data, anonymizing, cleaning, analyzing, processing,
            and modelling the data in a manner that was generalizable to other company assets.
            One particularly exciting facet of the project is the transparency (explainability)
            of the insights generated, an important feature considering strict documentation
            is required to explain decisions guiding users of a model of this nature.
        """

tdi_overview: str = """
        ##### Position: Data Science Fellow

        ###### Completed: Dec. 2023

         - Achieved >90% on all assignments

         - Built ML models for image processing, sentiment analysis, and regression

         - Refined my ability to maintain and access SQL databases

         - Learned how to apply ML from through the lens of business problem solving

         - Coursework entailed ML Pipelines, Model/Feature Selection, Distributed Computing, and Data Processing/Visualization

        """

# Capstone Descriptions
capstone_data_and_motivation: str = """

            USDA Branded Food Items Dataset contains all food items registered with the USDA. The dataset
            also contains informaiton about the ingredients, description, brand owner, and parent company selling the items.

            This dataset is > 2GB and contains more than 3,568,000 food and beverage products' label information.

            An application was built that assists consumers in finding food items registered
            with the USDA that match criteria according to their dietary preferences.

            The motivation for this project came from encountering the reaction mechanism of the preservative
            Sodium Benzoate and Ascorbic Acid (Vitamin C). Under conditions favoring homolysis (high temperatures or
            sun exposure) benzene is a byproduct; albiet, often in extremely small quantities. Still, I was concerned
            with the potential presence of a carcinogen floating around in my orange juice. So I thought an application
            that empowered users to make more informed decisions about items they consume would be a useful tool.

            """

capstone_cleaning_and_processing: str = """

            As with most data in the real world. Some cleaning needed to be done to ensure consistency
            with the desired functionality. To accomplish this regular expressions were utilized to
            standardize and parse comma separated strings into python lists.

            Many ingredient labels contain some rendition of a tag like 'Contains 0.5% or less of the following'.
            However, given the variety of food products and producers, this tag is far from standardized in the dataset.
            Thus regex was a great tool to generalize the above tag to account for edge cases like contain(s), (x)%,
            less than, less, or less, or less than, etc.

            Another textual behavior in need of wrangling were descriptive modifiers before and after ingredients.
            These modifiers were of the form: 'as an anti-caking agent', 'to preserve freshness', 'for color', 'used for', etc.
            Many of these occurences were identified and added to a list which was scanned for each item in the dataset and removed if
            they were found in the ingredient list.

            Parsing the data was a very important step so ample time was spent covering as many different forms of data impurity as
            possible to ensure noningredient words would not be passed as ingredients to the database.

            """

capstone_database_management_and_interface: str = """
            To efficiently access the processed data in an application, it was stored in a PostgresSQL database. Aiven was used to
            host this database. Then to establish connections and perform in-app querying, sqlalchemy was used to pythonically
            execute SQL queries within the database.

            """

capstone_display_perfect_matches: str = """
            Once queried, the data was displayed using a custom hierarichally directed acyclic graph built in plotly.
            Although this process was slightly tedious, the functionality and interactivity of the plotly figure
            generated proved worth the effort. One issue encountered during the developement of the visualization was
            dealing with queries returning large result sets.

            This issue was resolved with a rendition of an alternating sequence, utilized to compute the horizontal
            distribution of nodes on the graph. Ensuring spacing would account for various items per brand whilst remaining
            independent of the number of nodes on the graph.
            """

capstone_data_source: str = """
    Data Source For Ingredient Identifier:

    U.S. Department of Agriculture, Agricultural Research Service.
    FoodData Central, 2023. fdc.nal.usda.gov.

    """

# PySpark Classifier Descriptions
pyspark_build_description: str = """
        Building this model a balance was acheived on overfitting based on single words. It has proven quite easy to trick the model
        with oxymoronic input. The training data also elucidates the complexity of language and the dangers of
        restricting human behavior to oversimplified descriptions (speech only being categorically confined to 6 emotions).
        """

pyspark_model_performance: str = """
            The model performed with 90% accuracy on the training data and the most important parameter was document frequency count in the
        processing step.

        This was a great reminder of the age old adage 'garbage in garbage out' because despite pulling all of the levers of
        the logistic regression model (which performed better than 4 other models), the accuracy was limited by how the text was preprocessed.

        Another apparent shortcoming of the model is the inability to classify surprise without the presence of explicit surprise
        related keywords in the text. This is likely due to the descrepency between the number of training labels associated with surprise
        which had approximately 15,000 labels compared to all other labels with at least four times as many for training.
            """

pyspark_hyperparams: str = """
            The models hyperpameters were tuned using pySpark's CrossValidator with ClassificationEvaluator.

            As stated above, the greatest improvement in model accuracy was achieved by increasing document frequency count during
            the text vectorization step.

            """

pyspark_example_outputs: str = """
            The model sometimes performs surprisingly well with more abstract emotional expressions,
            here are some examples of this abstract metaphoric classification:

        "That ship has left the harbour" = sadness

        "His blood boiled" = anger

        "You are my number 1" = joy

        "Watching that whale warmed my heart" = love

        "I almost soiled myself when the leopard ran at me" = fear

        "Is it possible to do that" = surprise
            """

pyspark_input_guide: str = """
        Type any sentence into the textbox to see how this model holds up. With oxymoronic or abstract input
        the model behavior can be quite surprising, sometimes favorably and sometimes far less favorably.
        """

pyspark_data_source: str = """

        Data Source For Training Spark Model:

            @inproceedings{saravia-etal-2018-carer,\n
            title = "{CARER}: Contextualized Affect Representations for Emotion Recognition",\n
            author = "Saravia, Elvis  and Liu, Hsien-Chi Toby  and Huang, Yen-Hao
                        and Wu, Junlin  and Chen, Yi-Shin",\n
            booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",\n
            month = oct # "-" # nov, year = "2018",\n
            address = "Brussels, Belgium",\n
            publisher = "Association for Computational Linguistics",\n
            url = "https://www.aclweb.org/anthology/D18-1404",\n
            doi = "10.18653/v1/D18-1404",\n
            pages = "3687--3697",\n

            abstract = "Emotions are expressed in nuanced ways, which varies by collective or individual experiences, knowledge, and beliefs.
            Therefore, to understand emotion, as conveyed through text, a robust mechanism capable of capturing and modeling different
            linguistic nuances and phenomena is needed. We propose a semi-supervised, graph-based algorithm to produce rich structural
            descriptors which serve as the building blocks for constructing contextualized affect representations from text. The pattern
            based representations are further enriched with word embeddings and evaluated through several emotion recognition tasks. Our
            experimental results demonstrate that the proposed method outperforms state-of-the-art techniques on emotion recognition tasks.",}

        """

how_i_built_this: str = """
        To see the python code used to build this app, click the github logo in the top right corner.

        For incorporating the pySpark classification model, Scala and Java are needed in the application environment.
        Thankfully streamlit allows for additional non-python packakes to be specified in a 'packages.txt' file.

        The autoscroll/anchor feature in the 'Sections' container is a nice trick streamlit inherited from markdown.

        All figures in the app were built using Plotly. Plotly is a personal favorite for high-level visualizations because I
        have yet to encounter a visualization that cannot be built (often concisely)
        using either plotly express or the more robust figure objects. It also has nice features for creating animations
        like the one found in the [Internship](#internship) section.

        Another great feature of streamlit is the ability to add the download button for any file in the environment.
        In a data science context this could even be used to train a model or configure a visualization and then allow for the user
        to download that object directly from the application.

        """

scitec_description: str = """
        ##### Position: Asscociate Analyst/Engineer

        ###### From: Aug. 2024 - Nov. 2024

        -  Worked on a six-member analyst agile team in a Linux Dev Environment \n

        -  Contributed to library code employing modern DevOps/CICD pipelines \n

        -  Built interactive 3D visualizations to verify the behavior of simulated trajectories produced
            using Python and MATLAB \n

        -  Contributed to projects that asynchronously read and analyzed logging outputs from C++
            code and implemented proprietary algorithms to make decisions for customers \n

        -  Used Linear Algebra techniques to apply spatial transformations to simulated data \n

        -  Implemented Test Driven Development (TDD) \n

        -  Built Dash prototype to display algorithm output for customer demos \n
        """


# Create TypedDict class to store section description Data
## When New Sections are add this typing structure needs to be updated as well
class SectionDescriptions(TypedDict):
    """Typed Dictionary Holding Section Descriptions."""

    reference_section: str
    experience_section: str
    scitec_description: str
    intern_overview: str
    thesis: str
    tdi_overview: str
    capstone: Dict[str, str]
    tutoring: str
    chem_lab: str
    pyspark: Dict[str, str]
    about_me: str
    how_i_built_this: str


# Dictionary Containing all text sections for easy import and readibility
section_descriptions: SectionDescriptions = {
    "reference_section": reference_markdown,
    "experience_section": experience_section,
    "scitec_description": scitec_description,
    "intern_overview": intern_overview,
    "thesis": thesis_description,
    "tdi_overview": tdi_overview,
    "capstone": {
        "data_and_motivation": capstone_data_and_motivation,
        "cleaning_and_processing": capstone_cleaning_and_processing,
        "database_management_and_interface": capstone_database_management_and_interface,
        "display_perfect_matches": capstone_display_perfect_matches,
        "data_source": capstone_data_source,
    },
    "tutoring": tutoring_description,
    "chem_lab": comp_chem_descrption,
    "pyspark": {
        "build_description": pyspark_build_description,
        "model_performance": pyspark_model_performance,
        "hyperparams": pyspark_hyperparams,
        "example_outputs": pyspark_example_outputs,
        "input_guide": pyspark_input_guide,
        "data_source": pyspark_data_source,
    },
    "about_me": about_me_description,
    "how_i_built_this": how_i_built_this,
}
