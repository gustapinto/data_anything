from os import getenv

from pyspark.sql import SparkSession
from pyspark.sql import functions as f


if __name__ == '__main__':
    spark = SparkSession.builder.master(getenv('SPARK_MASTER_URL')) \
                                .appName('Netflix') \
                                .getOrCreate()
    spark.sparkContext.setLogLevel('ERROR')

    df = spark.read.option('inferSchema', 'true') \
                   .option('header', 'true') \
                   .csv('/jupyter/netflix/datasets/netflix_titles.csv')

    df.groupBy(f.col('release_year')).count().orderBy(f.col('count').desc()).show()

    df.groupBy(f.col('type')).count().orderBy(f.col('count').desc()).show()

    print(df.filter(f.col('listed_in').like('%Horror Movies%')).count())

    spark.stop()
