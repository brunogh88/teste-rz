# -*- coding: utf-8 -*-
from src.quality.oil_derivative_fuels_quality import OilDerivativeFuelsQuality

def test_if_there_are_values_in_required_columns(spark):
    data_mock = spark.createDataFrame([
        ("2021-01-01", "ACRE", "GASOLINA", "m3", 10090.00, 20210612),
        ("2021-01-01", "SÃO PAULO", "GLP", "m3", None, 20210612),
        ("2021-01-01", "RIO DE JANEIRO", "", "m3", None, 20210612),
        ("2021-02-01", "MINAS GERAIS", None, "m3", None, 20210612),
        ("2021-02-01", None, "GASOLINA", "m3", 23455.98, 20210612),
    ], 
    ["year_month", "uf", "product", "unit", "volume", "dt_partition"])

    expected_list = 0
    filter = 'uf is null or product is null or volume is null'
    result_uf = OilDerivativeFuelsQuality(data_mock).process().filter(filter).count()

    assert expected_list == result_uf

    
