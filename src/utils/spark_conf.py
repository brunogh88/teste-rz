"""
spark_utils.py
~~~~~~~~

Method to create sparkSession
"""
from pyspark.sql import SparkSession
from src.utils.config import config


def get_spark_session(pipe):
    """
    Start session Spark

    :return: SparkSession
    """
    return SparkSession.builder.appName(
        config("APP_NAME")+"_"+pipe
    ).config("spark.streaming.stopGracefullOnShutdown", True).getOrCreate()
