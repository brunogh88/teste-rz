"""This module is HdfsUtils Class"""


class OracleUtils(object):
    """Hdfs Utils Class have some methods to work with Oracle

        Args:
        spark_session: spark session
    """

    def __init__(self, spark_session):
        self.spark_session = spark_session

    def read_oracle(self, table_name):
        """This method read data from Oracle

        Args:
            table_name: table name to save data
        """
        return (
            self
            .spark_session
            .read
            .format('jdbc')
            .option("url", "jdbc:oracle:thin:DW/test@//localhost:1521/xe")
            .option("dbtable", table_name)
            .option("user", "DW")
            .option("password", "test")
            .option("driver", "oracle.jdbc.driver.OracleDriver")
            .load()
        )

    @classmethod
    def write_oracle(cls, dataframe, table_name):
        """This method write data in HDFS

        Args:
            dataframe: dataframe with data to save
            table_name: table name where will save the data
        """
        (
            dataframe
            .write
            .format('jdbc')
            .option("batchsize", 1000)
            .mode('append')
            .jdbc(
                "jdbc:oracle:thin:@localhost:1521/xe",
                table_name,
                properties={
                    "driver": "oracle.jdbc.OracleDriver",
                    "user": "DW",
                    "password": "test"
                }
            )
        )
