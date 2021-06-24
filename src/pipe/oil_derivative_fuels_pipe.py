"""This module contains the Oil Derivative Fuels Pipe Class"""
from src.load.oil_derivative_fuels_load import OilDerivativeFuelsLoad
from src.quality.oil_derivative_fuels_quality import OilDerivativeFuelsQuality
from src.save.oil_derivative_fuels_save import OilDerivativeFuelsSave
from src.process.odf_group_by_uf_product_process import (
    ODFGroupByUfAndProductProcess)
from src.ingest.oil_derivative_fuels_ingest import OilDerivativeFuelsIngest


class OilDerivativeFuelsPipe(object):
    """Class with steps pipe Oil Derivative Fuels

    Args:
        spark_session: spark session
        args: arguments used to start pipe
    """

    def __init__(self, spark_session, args):
        self.spark_session = spark_session
        self.args = args
        self.df_oil_derivative_fuels = None

    def __load_step(self):
        """This method have all steps to load all data to dataframes"""
        self.df_oil_derivative_fuels = OilDerivativeFuelsLoad(
            spark_session=self.spark_session,
            dt_partition=self.args.date).load()

    def __quality(self):
        """This method have all steps to do quality of data"""
        self.df_oil_derivative_fuels = OilDerivativeFuelsQuality(
            self.df_oil_derivative_fuels
        ).process()

    def __save(self):
        """This method have all steps to save data in trusted"""
        OilDerivativeFuelsSave(self.df_oil_derivative_fuels).save()

    def __process_step(self):
        """This method have all steps to transformation data"""
        self.df_oil_derivative_fuels = ODFGroupByUfAndProductProcess(
            self.df_oil_derivative_fuels
        ).process()

    def __ingest_step(self):
        """This method have all steps to save data in refined"""
        OilDerivativeFuelsIngest(self.df_oil_derivative_fuels).ingest()

    def start(self):
        """This method start all process to pipe"""
        self.__load_step()
        self.__quality()
        self.__save()
        self.__process_step()
        self.__ingest_step()
