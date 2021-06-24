"""This module contains the Oil Derivative Fuels Load Class"""
from pyspark.sql import functions as F
from src.utils.hdfs_utils import HdfsUtils
from src.utils.config import config
from src.model.oil_derivative_fuels import oil_derivative_fuels
from src.utils import log


class OilDerivativeFuelsLoad(object):
    """Class Oil Derivative Fuels Load

    Args:
        spark_session: Spark Session
        dt_partition: Processing Date
    """

    def __init__(self, spark_session, dt_partition):
        self.spark_session = spark_session
        self.dt_partition = dt_partition

    def load(self):
        """This method to do load dataset Oil Derivative Fuels with data csv"""
        log.info("Start Load data Oil Derivative Fuels")

        df_oil_derivative_fuels = HdfsUtils(self.spark_session).read_hdfs(
            path=config("PATH_RAW_OIL_DERIVATIVE_FUELS") +
            str(self.dt_partition) + '/',
            schema=oil_derivative_fuels(),
            format_data=config("CSV_FORMAT")
        )

        df_oil_derivative_fuels = self.__add_partition_column(
            df_oil_derivative_fuels
        )

        log.info("Finish Load data Oil Derivative Fuels")
        return df_oil_derivative_fuels

    def __add_partition_column(self, df_oil_derivative_fuels):
        """This method add column partition with processing
            date to dataset Oil Derivative Fuels
        """
        return (
            df_oil_derivative_fuels
            .withColumn("dt_partition", F.lit(self.dt_partition))
        )
