"""Module For Building and Using Spark ML Models in the resume_app."""

# Import modules
from pyspark.sql import SQLContext, SparkSession
from pyspark.ml import PipelineModel
from pyspark.ml.classification import LogisticRegressionModel
import pandas as pd


# Def function to create spark instance in app
def create_spark_instance() -> SQLContext:
    """Create a Spark SQL Context for in-app use."""
    spark = SparkSession.builder.appName("Emotion Classifier").getOrCreate()
    sqlContext = SQLContext(spark.sparkContext)
    return sqlContext


# Def function to load lrModel into app environment, may need a cache wrapper
def load_lrModel(model_path: str) -> LogisticRegressionModel:
    """
    Load LR Model into environment.

    Input:
    -----
    model_path : Filepath containing serialized LR Model

    Returns
    -------
    lrModel : Functional Instance of loaded Spark LR Model

    """
    lrModel = LogisticRegressionModel.load(model_path)
    return lrModel


# Def function to load prefit transformation pipeline to allow for data ingestion into model
def load_pipeline(pipeline_path: str) -> PipelineModel:
    """
    Load Spark Transformation Pipeline into environment.

    Input:
    -----
    pipeline_path : Filepath containing serialized Spark Transformation Pipeline

    Returns
    -------
    fitPipeline : Prefit Spark Transformation Pipeline.

    """
    fitPipeline = PipelineModel.load(pipeline_path)
    return fitPipeline


def classify_input(
    input_txt: str,
    sqlContext: SQLContext,
    fitPipeline: PipelineModel,
    lrModel: LogisticRegressionModel,
) -> str:
    """
    Accept str input, transform in proper shape, return LR Model output.

    Input:
    -----
    input_txt   : User String Input to be classified
    sqlContext  : SQL Context required for spark functionality
    fitPipeline : Loaded Transformation Pipeline to ingest data
    lrModel     : Loaded Text Classification Model

    Returns
    -------
    classification label from numeric output of lrModel

    """
    # Define class label mapping to map model output
    class_label_mapping = {
        "0": "sadness",
        "1": "joy",
        "2": "love",
        "3": "anger",
        "4": "fear",
        "5": "surprise",
    }

    # Convert input into spark digestible format
    inputDF = sqlContext.createDataFrame(
        pd.DataFrame({"text": [input_txt]}, columns=["text"])
    )

    # Transform txt via fitPipeline
    transformed_txt = fitPipeline.transform(inputDF)

    # Prediction text class label via lrModel and extract prediction
    input_pred = int(
        lrModel.transform(transformed_txt).toPandas()["prediction"].values[0]
    )

    return class_label_mapping[str(input_pred)]
