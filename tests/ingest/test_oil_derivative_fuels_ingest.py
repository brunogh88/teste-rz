# -*- coding: utf-8 -*-
from src.ingest.oil_derivative_fuels_ingest import OilDerivativeFuelsIngest
from tests.utils import delete_folder, path_exist
from decimal import Decimal

def test_path_hdfs_refined_exist(spark):
    data_mock = spark.createDataFrame([
        ("ACRE", "GASOLINA C", Decimal('10090.00'), 20210612),
        ("SÃO PAULO", "GLP", Decimal('746563.76'), 20210612),
        ("RIO DE JANEIRO", "ÓLEO DISEL", Decimal('37475.58'), 20210612),
        ("SÃO PAULO", "GASOLINA C", Decimal('7463545.65'), 20210612),
        ("RIO DE JANEIRO", "GASOLINA C", Decimal('23455.98'), 20210612),
    ], 
    ["uf", "product", "volume", "dt_partition"])

    path_hdfs_refined = "../../data/REFINED/SALES_OIL_DERIVATIVE_FUELS"
    delete_folder(path_folder=path_hdfs_refined)
    exp_path_exist = False

    assert exp_path_exist == path_exist(path_folder=path_hdfs_refined)

    OilDerivativeFuelsIngest(data_mock).ingest()
    exp_path_exist_after_process_save = True

    assert exp_path_exist_after_process_save == path_exist(path_folder=path_hdfs_refined)
