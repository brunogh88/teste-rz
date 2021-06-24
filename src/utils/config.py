def config(key):
    """
    Class to load variable parameters

    :param key: key parameter name
    :return: value to key
    """
    config = {
                "APP_NAME" : 'raizen-test',
                "CSV_FORMAT": "csv",
                "JDBC_FORMAT": "jdbc",
                "PATH_RAW_OIL_DERIVATIVE_FUELS": "../../data/RAW/SALES_OIL_DERIVATIVE_FUELS/",
                "PATH_TRUSTED_OIL_DERIVATIVE_FUELS": "../../data/TRUSTED/SALES_OIL_DERIVATIVE_FUELS/",
                "PATH_REFINED_OIL_DERIVATIVE_FUELS": "../../data/REFINED/SALES_OIL_DERIVATIVE_FUELS/",
                "APPEND_MODE" : "append",
                "PARQUET_FORMAT" : "parquet",
                "OVERWRITE_MODE" : "Overwrite"
    }
    return config[key]