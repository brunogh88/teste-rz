# -*- coding: utf-8 -*-
from src.process.odf_group_by_uf_product_process import ODFGroupByUfAndProductProcess
from src.model.oil_derivative_fuels import oil_derivative_fuels
from datetime import datetime
from decimal import Decimal


def test_odf_group_by_uf_product_is_correct(spark):
    data_mock = spark.createDataFrame([
        (datetime.strptime("2021-01-01", '%Y-%m-%d'), "ACRE", "GASOLINA C", "m3", Decimal(10090.00), 20210612),
        (datetime.strptime("2021-01-01", '%Y-%m-%d'), "ACRE", "GLP", "m3", Decimal(10300.23), 20210612),
        (datetime.strptime("2021-02-01", '%Y-%m-%d'), "ACRE", "GLP", "m3", Decimal(857463.66), 20210612),
        (datetime.strptime("2021-01-01", '%Y-%m-%d'), "SÃO PAULO", "GASOLINA DE AVIAÇÃO", "m3", Decimal(4384856.98), 20210612),
        (datetime.strptime("2021-03-01", '%Y-%m-%d'), "SÃO PAULO", "GASOLINA DE AVIAÇÃO", "m3", Decimal(847353.54), 20210612),
        (datetime.strptime("2021-01-01", '%Y-%m-%d'), "SÃO PAULO", "GASOLINA C", "m3", Decimal(847353.54), 20210612)
    ], 
    oil_derivative_fuels())
    
    df_odf = ODFGroupByUfAndProductProcess(data_mock).process()

    df_odf.show()

    exp_vlm_sp_aviation_gasoline = Decimal('5232210.52')
    exp_vlm_ac_glp = Decimal('867763.89')
    exp_qty_total_lines = 4

    """assert exp_vlm_sp_aviation_gasoline == df_odf.select("volume").filter(
        'uf = "SÃO PAULO" and product = "GASOLINA DE AVIAÇÃO"').first()[0]"""

    assert exp_vlm_ac_glp == df_odf.select("volume").filter(
        'uf = "ACRE" and product = "GLP"').first()[0]

    assert exp_qty_total_lines == df_odf.count()