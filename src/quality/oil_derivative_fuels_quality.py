# -*- coding: utf-8 -*-
"""This module contains the Oil Derivative Fuels Quality Class"""
from src.utils import log


class OilDerivativeFuelsQuality(object):
    """Oil Derivative Fuels Quality

        Args:
        df_oil_derivative_fuels: dataframe with data Oil Derivative Fuels
    """

    def __init__(self, df_oil_derivative_fuels):
        self.df_oil_derivative_fuels = df_oil_derivative_fuels

    def process(self):
        """This method to do data quality Oil Derivative Fuels dataframe"""
        log.info("Start Quality data Oil Derivative Fuels")

        df_oil_derivative_fuels = (
            self.df_oil_derivative_fuels
            .na.fill(value=0, subset=["volume"])
            .na.fill(value="UKNOW", subset=["uf", "product"])
        )

        log.info("Finish Quality data Oil Derivative Fuels")
        return df_oil_derivative_fuels
