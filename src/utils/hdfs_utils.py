"""This module is HdfsUtils Class"""


class HdfsUtils(object):
    """Hdfs Utils Class have some methods to work with HDFS

        Args:
        spark_session: spark session
    """

    def __init__(self, spark_session):
        self.spark_session = spark_session

    def read_hdfs(self, path, schema, format_data):
        """This method read data from HDFS

        Args:
            path: path where will save data in hdfs
            schema: data structure
            format_data: data format to save to hdfs
        """

        return (
            self.spark_session
            .read
            .schema(schema)
            .format(format_data)
            .option("sep", ";")
            .option("header", "true")
            .option("encoding", "UTF-8")
            .load(path)
        )

    @classmethod
    def write(cls, dataframe, path, format_data, partition_name, save_mode):
        """This method write data in HDFS

        Args:
            dataframe: dataframe with data to save
            path: path where will save the data
            format_data: data format to save
            partition_name: partition name
            save_mode: format that will save the data
        """
        (
            dataframe
            .write
            .mode(save_mode)
            .format(format_data)
            .partitionBy(partition_name)
            .save(path)
        )
