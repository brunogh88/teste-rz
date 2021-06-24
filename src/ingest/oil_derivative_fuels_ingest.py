"""This module contains the Oil Derivative Fuels Class"""
from src.utils import log
from src.utils.hdfs_utils import HdfsUtils
from src.utils.config import config


class OilDerivativeFuelsIngest(object):
    """Oil Derivative Fuels Save in Refined

    Args:
        df_oil_derivative_fuels: dataframe with data Oil Derivative Fuels
    """
    def __init__(self, df_oil_derivative_fuels):
        self.df_oil_derivative_fuels = df_oil_derivative_fuels

    def ingest(self):
        """This method to do ingest data Oil Derivative Fuels in Refined"""
        log.info("Start Save data Oil Derivative Fuels in Refined")

        HdfsUtils(None).write(
            dataframe=self.df_oil_derivative_fuels,
            path=config("PATH_REFINED_OIL_DERIVATIVE_FUELS"),
            format_data=config("PARQUET_FORMAT"),
            partition_name="dt_partition",
            save_mode=config("OVERWRITE_MODE")
        )

        log.info("Finish Save data Oil Derivative Fuels in Refined")
