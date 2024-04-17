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
                # Sections
            
                [Education](#education)
            
                [Internship](#internship)
            
                [Skills](#skills)
            
                [Capstone Project for The Data Incubator](#ingredient-identifier)
            
                [pySpark Text Classification Model](#pyspark-text-classification-model)
            
                """)
    col_2.image("imgs/headshot.png")

#About Me 
st.subheader("About Me")
st.write("""
                
        I am a Data Scientist who is enthusiastic about learning new technologies
        and adapting to innovations in the field. 

        All of the facets of machine learning are vital arrows in the 
        quiver of buisiness problem solving. Data is a tool drastically 
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
edu_graph = education_treemap(tdi_data, fau_data)
st.plotly_chart(edu_graph)

#Describe Tutoring Role and Timeframe
st.subheader("Mathematics Tutor at Florida Atlantic University")
st.write("""
        Courses Tutored: Matrix Theory, Introduction to Statistics, 
        Calculus 1,2 & 3, and Differential Equations

        While tutoring students from nontechnical backgrounds I found success in
        looking for applications of the pertinant material in the real world to help 
        motivate learning of the material.

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
        Click 'Build Graph' to build the visualization and then hover over each data point to view the corresponding information.
        """)
#load internship graph data
intern_data = undill_it('resume_data/intern_data.dll')
intern_pos_dict = undill_it('resume_data/intern_pos_dict.dll')
#generate animated_intern_graph
intern_graph = animated_intern_graph(intern_data, intern_pos_dict)
st.plotly_chart(intern_graph)

#embed thesis hyperlink
st.write("I used this work to write my senior thesis at FAU, you can click the button 'View Paper' below to find the paper hosted on github.")
st.write("""
            This was a great opportunity to work on a project from start to finish. 
            My work entailed retrieving the data, anonymizing, cleaning, analyzing, processing, 
            and modelling the data in a manner that was generalizable to other company assets.
            One particularly exciting facet of the project is the Transparency (Explainability) 
            of the insights generated, this is an important feature considering strict documentation 
            is required to explain decisions guiding users of a model of this nature. 
        """)
        
st.link_button("View Paper: Spatiotemporal Determinants of Football Stadium Incidents",
               "https://github.com/jrw34/ThesisJW_PDF/blob/main/JW_Thesis_pdf2.pdf")

#skills graph
st.header("Skills")
#load skills graph data
skills_df = undill_it('resume_data/skills_df.dll')
#generate skills_graph
skill_graph = skills_graph(skills_df)
st.plotly_chart(skill_graph)

#Capstone Project 
st.header("Ingredient Identifier")
st.subheader("Capstone Project For The Data Incubator Fellowship Program")
#display images from capstone project
st.write("""
        Describe Data
        
        Describe Cleaning the Data (Regex, parsing, removing phrases like 'Contains'
        
        Describe Establishing Data Base
        
        Describe use of sqlalchemy
        
        Describe Building the graph to display perfect matches
        """)

capstone_toggler = st.toggle("Display Capstone Project")
if capstone_toggler:
    st.write("Input Food Item")
    st.image('imgs/cap_proj_1.png')
    st.write("Select Desired Features")
    st.image('imgs/cap_proj_2.png')
    st.write("Display Query Results")
    st.image('imgs/cap_proj_3.png')

st.write("""Data Source:

        U.S. Department of Agriculture, Agricultural Research Service. 
        FoodData Central, 2023. fdc.nal.usda.gov.
        """)

#Embed emotion classification spark model
st.header("pySpark Text Classification Model")
st.subheader("Here is a simple emotion classifier I built using spark because I think it is a great framework for NLP classification tasks")
st.write("""        
        Building this model I had to walk the line of overfitting based on single words. It has proven quite easy to trick the model
        with oxymoronic input. The training data also elucidates the complexity of language and the dangers of 
        restricting human behavior to oversimplified descriptions (speech only being categorically confined to 6 emotions).

        The model performed with 90% accuracy on the training data and the most important parameter was document frequency count in the 
        processing step. This was a great reminder of the age old adage 'garbage in garbage out' because despite pulling all of the levers of 
        the logistic regression model (which performed better than 4 other models), the accuracy was limited by how the text was preprocessed.
        Another apparent shortcoming of the model is the inability to classify surprise without the presence of explicit surprise 
        related keywords in the text. This is likely due to the descrepency between the number of training labels associated with surprise
        which had approximately 15,000 labels compared to all other labels with at least four times as many for training.

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
            Input any sentence to see how this model holds up, the more abstract the more suprising the model will behave, 
            sometimes favorably and sometimes far less favorably.
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

        Data Source: 
        
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
        add some fun stuff I did while building this project
        
        talk about add java to packages.txt
        
        talk about embedding autoscroll anchors in markdown sections
        
        talk about building the animation
        
        talk about adding download button for pdf ... mime data
        
        """)
