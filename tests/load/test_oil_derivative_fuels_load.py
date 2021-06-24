from src.load.oil_derivative_fuels_load import OilDerivativeFuelsLoad

def test_get_data_from_load_csv(spark):
    dt_partition=20210612
    expected_list = 54432
    result_list = OilDerivativeFuelsLoad(spark, dt_partition).load().count()
    assert expected_list == result_list

def test_check_column_dt_partition_exist(spark):
    dt_partition=20210612
    expected_column=True
    df = OilDerivativeFuelsLoad(spark, dt_partition).load()
    result_column= 'dt_partition' in df.columns
    assert expected_column == result_column
