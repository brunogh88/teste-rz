# -*- coding: utf-8 -*-
from src.save.oil_derivative_fuels_save import OilDerivativeFuelsSave
from src.model.oil_derivative_fuels import oil_derivative_fuels
from tests.utils import delete_folder, path_exist
from decimal import Decimal
from datetime import datetime

def test_path_hdfs_trusted_exist(spark):
    data_mock = spark.createDataFrame([
        (datetime.strptime("2021-01-01", '%Y-%m-%d'), "ACRE", "GASOLINA C", "m3", Decimal(10090.00), 20210612),
        (datetime.strptime("2021-01-01", '%Y-%m-%d'), "ACRE", "GLP", "m3", Decimal(10300.23), 20210612),
        (datetime.strptime("2021-02-01", '%Y-%m-%d'), "ACRE", "GLP", "m3", Decimal(857463.66), 20210612),
        (datetime.strptime("2021-01-01", '%Y-%m-%d'), "SÃO PAULO", "GASOLINA DE AVIAÇÃO", "m3", Decimal(4384856.98), 20210612),
        (datetime.strptime("2021-03-01", '%Y-%m-%d'), "SÃO PAULO", "GASOLINA DE AVIAÇÃO", "m3", Decimal(847353.54), 20210612),
        (datetime.strptime("2021-01-01", '%Y-%m-%d'), "SÃO PAULO", "GASOLINA C", "m3", Decimal(847353.54), 20210612)
    ], 
    oil_derivative_fuels())

    path_hdfs_trusted = "../../data/TRUSTED/SALES_OIL_DERIVATIVE_FUELS"
    delete_folder(path_folder=path_hdfs_trusted)
    exp_path_exist = False

    assert exp_path_exist == path_exist(path_folder=path_hdfs_trusted)

    OilDerivativeFuelsSave(data_mock).save()
    exp_path_exist_after_process_save = True

    assert exp_path_exist_after_process_save == path_exist(path_folder=path_hdfs_trusted)
