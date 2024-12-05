#import modules
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

from pyspark.ml.feature import RegexTokenizer, StopWordsRemover, CountVectorizer
from nltk.corpus import stopwords
from pyspark.ml import PipelineModel
from pyspark.ml.classification import LogisticRegressionModel
import pandas as pd

#def function to create spark instance in app
def create_spark_instance():
    spark = SparkSession.builder.getOrCreate()#.appName("Emotion Classifier")
    sqlContext = SQLContext(spark)
    return sqlContext

#def function to load lrModel into app environment, may need a cache wrapper
def load_lrModel(model_path:str):
    lrModel = LogisticRegressionModel.load(model_path)
    return lrModel

#def function to load prefit transformation pipeline to allow for data ingestion into model
def load_pipeline(pipeline_path:str):
    fitPipeline = PipelineModel.load(pipeline_path)
    return fitPipeline

def classify_input(input_txt:str, sqlContext, fitPipeline, lrModel):
    #define class label mapping to map model output
    class_label_mapping = {'0' : 'sadness', '1' : 'joy', 
                           '2' : 'love', '3' : 'anger', 
                           '4' : 'fear', '5' : 'surprise'}
    
    #convert input into spark digestible format
    inputDF = sqlContext.createDataFrame(pd.DataFrame({'text': [input_txt]}, columns = ['text']))
    
    #transform txt via fitPipeline
    transformed_txt = fitPipeline.transform(inputDF)
    
    #prediction text class label via lrModel and extract prediction
    input_pred = int(lrModel.transform(transformed_txt).toPandas()['prediction'].values[0])

    return class_label_mapping[str(input_pred)]

    
    

