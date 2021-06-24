# -*- coding: utf-8 -*-
"""This module contains the Oil Derivative Fuels Process Class"""
from pyspark.sql import functions as F
from src.utils import log


class ODFGroupByUfAndProductProcess(object):
    """ This class return the columns uf, product, volume and dt_partition
        group by uf and product about data Oil Derivative Fuels

    Args:
        df_oil_derivative_fuels: Data frame with data Oil Derivative Fuels
    """

    def __init__(self, df_oil_derivative_fuels):
        self.df_oil_derivative_fuels = df_oil_derivative_fuels

    def process(self):
        """ This method to do group by uf, product and dt_partition
            for Oil Dericative Fuels dataframe
        """
        log.info("""Start Process Group by uf, product
            and dt_partition for Oil Dericative Fuels""")

        df_oil_derivative_fuels = self.df_oil_derivative_fuels.select(
            F.col("uf"),
            F.col("product"),
            F.col("volume"),
            F.col("dt_partition")
        ).groupBy(
            F.col("uf"),
            F.col("product"),
            F.col("dt_partition")
        ).agg(F.sum(F.col("volume")).cast("decimal(20,2)").alias("volume"))

        log.info("""Finish Process Group by uf, product
            and dt_partition for Oil Dericative Fuels""")

        return df_oil_derivative_fuels
