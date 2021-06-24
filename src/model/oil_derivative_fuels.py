"""Structed for Oil Derivative Fuels"""
from pyspark.sql.types import (
    DateType, DecimalType, IntegerType, StructField, StructType, StringType
)


def oil_derivative_fuels():
    """ This Method return the structed to use
        in dataframe Oil Derivative Fuels
    """
    return StructType([
        StructField("year_month", DateType(), True),
        StructField("uf", StringType(), True),
        StructField("product", StringType(), True),
        StructField("unit", StringType(), True),
        StructField("volume", DecimalType(15, 2), True),
        StructField("dt_partition", IntegerType(), True)
    ])
