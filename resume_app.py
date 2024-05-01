import streamlit as st
import pandas as pd

#import app_utils functions
from app_utils.education_graph import *      #education_treemap
from app_utils.internship_graph import *     #animated_intern_graph
from app_utils.skills_graph import *         #skills_graph
from app_utils.dill_loader import *          #undill_it
from app_utils.spark_app_interface import *  #create_spark_instance, load_lrModel, load_pipeline, classify_input


#create title
st.title("John Walsh Resume")

#Download Resume PDF button
with open("John_Walsh_Resume.pdf", "rb") as file:
    btn=st.download_button(
    label="Click Here to Download My Tradtional Resume as a PDF",
    file_name = 'John_Walsh_Resume.pdf',
    data=file,
    mime =  'application/pdf'
    )


#Reference Section and Headshot container
with st.container():
    col_1, col_2 = st.columns([2,1])
    col_1.markdown("""
                ## Sections
            
                [Education](#education)
            
                [Internship](#internship)
            
                [Skills](#skills)
            
                [Capstone Project for The Data Incubator](#ingredient-identifier)
            
                [pySpark Text Classification Model](#pyspark-text-classification-model)

                [How I Built This](#how-i-built-this)

                [Contact Info](#contact-info)
            
                """)
    col_2.image("imgs/headshot.png")

#About Me 
st.subheader("About Me")
st.write("""
                
        I am a Data Scientist and Python Developer who is enthusiastic about learning new technologies
        and adapting to innovations in the field. 

        All of the facets of machine learning are vital arrows in the 
        quiver of business problem solving. Data is a tool drastically 
        improving the world and I am thrilled to participate in bringing 
        data to life.
                        
        With firm belief in hard work, I persistently strive to produce meaningful, 
        thorough, and reproducible results built from an adequate mathematical
        foundation. 

        Furthermore, I hold communication as essential in the data science 
        process and there is little value in improperly communicated insights derived from data.

        Beyond my interests as a data scientist the outdoors, cooking, and travelling are an 
        important part of who I am.
                
        """)


#education graph
st.header("Education")

#load education graph data
tdi_data = undill_it('resume_data/tdi_data.dll')
fau_data = undill_it('resume_data/fau_data.dll')
#generate education_treemap
edu_graph = education_treemap(tdi_data, fau_data, 
                              color_1 = '#94E3FE', color_2 = '#FFC677', 
                              sector_bg_color = '#D4E3FE', 
                              sector_font_color = '#1A0A53')
st.plotly_chart(edu_graph)

st.write("""[Return to top](#sections) """)
#Describe Tutoring Role and Timeframe
st.subheader("Mathematics Tutor at Florida Atlantic University")
st.write("""
        Courses Tutored: Matrix Theory, Introduction to Statistics, 
        Calculus 1,2 & 3, and Differential Equations

        Found success by identifying real world applications of the pertinant mathematics 
        when tutoring students with nontechnical backgrounds. 

        Duration: 2 years
        """)

#Describe Volunteer Role at Computational Chemistry Lab
st.subheader("Computational Chemistry Laboratory Volunteer")
st.write("""
        Performed least squares optimization (analytically) using SVD in a Linux environment to project data points 
        onto a best-fit plane in 3-D. As a result, enabled better assessment of molecular interactions in the dynamic model.

        Duration: Summer Volunteer (3 months)
        """)

#internship graph
st.header("Internship")
st.write("""
        Click 'Build Graph' to build the visualization and hover over the data poins to view the corresponding information.
        """)
#load internship graph data
intern_data = undill_it('resume_data/intern_data.dll')
intern_pos_dict = undill_it('resume_data/intern_pos_dict.dll')
#generate animated_intern_graph
intern_graph = animated_intern_graph(intern_data, intern_pos_dict)
st.plotly_chart(intern_graph)

#embed thesis hyperlink
st.write("This work was also my senior thesis at FAU, you can click the button 'View Paper' below to find the paper hosted on github.")
st.write("""
            It was a great opportunity to work on a project from start to finish. 
            My project entailed retrieving the data, anonymizing, cleaning, analyzing, processing, 
            and modelling the data in a manner that was generalizable to other company assets.
            One particularly exciting facet of the project is the transparency (explainability) 
            of the insights generated, an important feature considering strict documentation 
            is required to explain decisions guiding users of a model of this nature. 
        """)
        
st.link_button("View Paper: Spatiotemporal Determinants of Football Stadium Incidents",
               "https://github.com/jrw34/ThesisJW_PDF/blob/main/JW_Thesis_pdf2.pdf")

st.write("""[Return to top](#sections) """)

#skills graph
st.header("Skills")
st.write("Click within the inner two circles to toggle view, center click to toggle back")
#load skills graph data
skills_df = undill_it('resume_data/skills_df.dll')
#generate skills_graph
skill_graph = skills_graph(skills_df)
st.plotly_chart(skill_graph)

st.write("""[Return to top](#sections) """)

#Capstone Project 
st.header("Ingredient Identifier")

st.subheader("Capstone Project For The Data Incubator Fellowship Program")
#display images from capstone project

if st.button("Data and Motivation"):
    st.write("""
             
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
                
            """)

if st.button("Cleaning and Processing the Data"):
    st.write("""

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
            
            """)

if st.button("Database Management and Interface"):
    st.write("""
            To efficiently access the processed data in an application, it was stored in a PostgresSQL database. Aiven was used to
            host this database. Then to establish connections and perform in-app querying, sqlalchemy was used to pythonically 
            execute SQL queries within the database. 
            
            """)

if st.button("Display Perfect Matches"):
    st.write("""
            Once queried, the data was displayed using a custom hierarichally directed acyclic graph built in plotly.
            Although this process was slightly tedious, the functionality and interactivity of the plotly figure 
            generated proved worth the effort. One issue encountered during the developement of the visualization was 
            dealing with queries returning large result sets. 
            
            This issue was resolved with a rendition of an alternating sequence, utilized to compute the horizontal 
            distribution of nodes on the graph. Ensuring spacing would account for various items per brand whilst remaining
            independent of the number of nodes on the graph.
            """)

capstone_toggler = st.toggle("Display Capstone Project")
if capstone_toggler:
    st.write("Input Food Item")
    st.image('imgs/cap_proj_1.png')
    st.write("Select Desired Features")
    st.image('imgs/cap_proj_2.png')
    st.write("Display Query Results")
    st.image('imgs/cap_proj_3.png')

st.write("""Data Source For Ingredient Identifier:

        U.S. Department of Agriculture, Agricultural Research Service. 
        FoodData Central, 2023. fdc.nal.usda.gov.
        """)
st.write("""[Return to top](#sections) """)
#Embed emotion classification spark model
st.header("pySpark Text Classification Model")
st.subheader("A simple emotion classifier built using spark")

st.write("""        
        Building this model a balance was acheived on overfitting based on single words. It has proven quite easy to trick the model
        with oxymoronic input. The training data also elucidates the complexity of language and the dangers of 
        restricting human behavior to oversimplified descriptions (speech only being categorically confined to 6 emotions).
        """)

#checkbox to explain model performance
model_perf_check = st.checkbox("Model Performance")
if model_perf_check:
    st.write("""
            The model performed with 90% accuracy on the training data and the most important parameter was document frequency count in the 
        processing step. 
        
        This was a great reminder of the age old adage 'garbage in garbage out' because despite pulling all of the levers of 
        the logistic regression model (which performed better than 4 other models), the accuracy was limited by how the text was preprocessed.
        
        Another apparent shortcoming of the model is the inability to classify surprise without the presence of explicit surprise 
        related keywords in the text. This is likely due to the descrepency between the number of training labels associated with surprise
        which had approximately 15,000 labels compared to all other labels with at least four times as many for training.
            """)
    
#checkbox to explain hyperparameter tuning
hyperparam_check = st.checkbox("Hyperparameter Tuning")
if hyperparam_check:
    st.write("""
            The models hyperpameters were tuned using pySpark's CrossValidator with ClassificationEvaluator.

            As stated above, the greatest improvement in model accuracy was achieved by increasing document frequency count during
            the text vectorization step. 
            
            """)


#checkbox to show some examples of the model input/output
examples_check = st.checkbox("Examples")
if examples_check:
    st.write("""
            The model sometimes performs surprisingly well with more abstract emotional expressions,
            here are some examples of this abstract metaphoric classification: 
        
        "That ship has left the harbour" = sadness
        
        "His blood boiled" = anger
        
        "You are my number 1" = joy
        
        "Watching that whale warmed my heart" = love
        
        "I almost soiled myself when the leopard ran at me" = fear

        "Is it possible to do that" = surprise
            """)

#describe input format
st.write("""
        Type any sentence into the textbox to see how this model holds up. With oxymoronic or abstract input
        the model behavior can be quite surprising, sometimes favorably and sometimes far less favorably.
        """)

## consider adding regex to replace all non alphabet characters with ''

#load sqlContext
sqlContext = create_spark_instance()

#load lrModel
lrModel = load_lrModel("lrModel_emotions.model")

#load fitPipeline
fitPipeline = load_pipeline("lrModel_transformation_pipe")

#user input
input_text = st.text_input("Input sentence here")

if input_text:
    st.write(f"User Input: {input_text}")

    #classify_text
    classifier_pred = classify_input(input_text, sqlContext, fitPipeline, lrModel)
    st.write(f"Did your text describe {classifier_pred}?")

st.write("""

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
        
        """)

    
#Add ssesction about process of building the site
st.header("How I built this")
st.write("""
        To checkout the python code used to build this app, click the github logo in the top right corner.
        
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
        
        """)

st.header("Contact Info")
st.write("""
        email: johnrwalsh34@gmail.com
        """)
st.write("""[Return to top](#sections) """)
