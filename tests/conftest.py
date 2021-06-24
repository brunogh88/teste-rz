import pytest
from pyspark.sql import SparkSession

#from tests import utils


@pytest.fixture(scope='session')
def spark():
    spark = SparkSession.builder \
        .master("local") \
        .appName("raizen-test") \
        .config('spark.sql.sources.partitionOverwriteMode', 'dynamic') \
        .getOrCreate()
    yield spark
    spark.stop()


"""@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # Setup
    # If something default have to be done, it should be here
    yield  # this is where the testing happens
    # Teardown
    utils.delete_tmp()
"""

