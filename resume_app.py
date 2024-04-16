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
                
        I believe that data is a tool that is drastically improving the world
        and I am always thrilled to participate in the process of bringing data
        to life.
                
        For me, all of the facets of machine learning are vital arrows in the 
        quiver of buisiness problem solving.
                
        I am firm believer in hard work and I persistently strive to produce meaningful 
        results that are thorough, reproducible, and built from an adequate mathematical
        foundation. 

        Another belief I hold is that communication is an essential component in the data science 
        process and I think there is little value in insights derived from data if these insights
        are not properly communicated.

        When I am not working I love to get to outdoors as much as possible, whether that is in my 
        backyard or the on other side of the world I am indifferent; however, I certainly cherish 
        the occassional departure from the continental shelf I call home. 
                
        """)

#education graph
st.header("Education")
#load in education graph data
tdi_data = undill_it('resume_data/tdi_data.dll')
fau_data = undill_it('resume_data/fau_data.dll')
#generate education treemap
edu_graph = education_treemap(tdi_data, fau_data)
st.plotly_chart(edu_graph)

#Describe Tutoring Role and Timeframe
st.subheader("Mathematics Tutor at Florida Atlantic University")
st.write("Add Bulleted Description Here")

#Describe Volunteer Role at Computational Chemistry Lab
st.subheader("Computational Chemistry Laboratory Volunteer")
st.write("Add Description of what I did here")

#internship graph
st.header("Internship")
#load in internship graph data
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
               "https://github.com/jrw34/ThesisJW_PDF/blob/main/JW_Thesis_pdf2.pdf") #make this bigger!

#skills graph
st.header("Skills")
#load in skills graph data
skills_df = undill_it('resume_data/skills_df.dll')
#generate skills_graph
skill_graph = skills_graph(skills_df)
st.plotly_chart(skill_graph)

#Describe Capstone Project with each image
st.header("Ingredient Identifier")
st.subheader("Capstone Project For The Data Incubator Fellowship Program")
#display images from capstone project --> wrap in buttons with corresponding descriptions
st.write("Add Project Description Here")
if st.button("Ingredient Identifier: Input"):
    st.image('imgs/cap_proj_1.png')

st.write("Explain Select Boxes and Importance of Caching Data pulled from Postgres DB")
if st.button("Ingredient Identifier: Select Features"):
    st.image('imgs/cap_proj_2.png')

st.write("Explain custom graph and why I thought it was important to display the data in this fashion")
if st.button("Ingredient Identifier: Display Query Results"):
    st.image('imgs/cap_proj_3.png')

st.write("""Data Source:

        U.S. Department of Agriculture, Agricultural Research Service. 
        FoodData Central, 2023. fdc.nal.usda.gov.
        """)

#Embed emotion classification spark model
st.header("pySpark Text Classification Model")
st.subheader("Here is a fun emotion classifier I built using spark because I think it is a great framework for NLP classification tasks")
st.write("""        
        Building this model I had to walk the line between overfitting based on single words. It has proven quite easy to trick the model
        with oxymoronic input. The training data also elucidates the complexity of language and the dangers of 
        restricting human behavior to oversimplified descriptions like speech only being categorically confined to 6 emotions.

        The model performance was 90% and the most important parameter was document frequency count in the processing step,
        this was a great reminder of the age old adage 'garbage in garbage out' because despite pulling all of the levers of the logistic
        regression model (which performed better than 4 other models), the accuracy was limited by how the text was preprocessed.
        Another apparent shortcoming of the model is the inability to classify surprise without the presence of explicit surprise 
        related keyword in the text. This is likely due to the descrepency between the number of training labels associated with surprise
        which had only 15,000 labels to train on compared to all other labels with at least four times as many training cases.

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
st.write("""Input any sentence to see how this model holds up, the more abstract the more suprising the model will behave, 
            sometimes favorably and sometimes far less favorably.
            """)

## consider adding regex to replace all non alphabet characters with ''

#load sqlContext
sqlContext = create_spark_instance()

#user input
input_text = st.text_input("Input sentence here")

if input_text:
    st.write(input_text)
    
    #load lrModel
    lrModel = load_lrModel("lrModel_emotions.model")

    #load fitPipeline
    fitPipeline = load_pipeline("lrModel_transformation_pipe")

    #classify_text
    classifier_pred = classify_input(input_text, sqlContext, fitPipeline, lrModel)
    st.write(f"Did your text describe {classifier_pred}?")

st.write("""

        Data Source: 
        
            @inproceedings{saravia-etal-2018-carer,
        
            title = "{CARER}: Contextualized Affect Representations for Emotion Recognition",
        
            author = "Saravia, Elvis  and Liu, Hsien-Chi Toby  and Huang, Yen-Hao 
                        and Wu, Junlin  and Chen, Yi-Shin",
            booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
        
            month = oct # "-" # nov, year = "2018",
        
            address = "Brussels, Belgium",
        
            publisher = "Association for Computational Linguistics",
        
            url = "https://www.aclweb.org/anthology/D18-1404",
        
            doi = "10.18653/v1/D18-1404",
        
            pages = "3687--3697",
    
            abstract = "Emotions are expressed in nuanced ways, which varies by collective or individual experiences, knowledge, and beliefs. 
            Therefore, to understand emotion, as conveyed through text, a robust mechanism capable of capturing and modeling different 
            linguistic nuances and phenomena is needed. We propose a semi-supervised, graph-based algorithm to produce rich structural 
            descriptors which serve as the building blocks for constructing contextualized affect representations from text. The pattern 
            based representations are further enriched with word embeddings and evaluated through several emotion recognition tasks. Our 
            experimental results demonstrate that the proposed method outperforms state-of-the-art techniques on emotion recognition tasks.",}
        
        """)

    



