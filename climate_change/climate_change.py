import tarfile
from os import getenv, path

from pyspark.sql import SparkSession
from pyspark.sql import functions as f


TAR_PATH = '/jupyter/datasets/GlobalLandTemperaturesByCity.csv.tar.gz'
CSV_DIR = '/jupyter/tmp/'
CSV_PATH = CSV_DIR + 'GlobalLandTemperaturesByCity.csv'


if __name__ == '__main__':
    spark = SparkSession.builder.master(getenv('SPARK_MASTER_URL')) \
                                .appName('ClimateChange') \
                                .getOrCreate()
    spark.sparkContext.setLogLevel('ERROR')

    if not path.exists(CSV_PATH):
        with tarfile.open(TAR_PATH) as file:
            file.extractall(CSV_DIR)

    df = spark.read.option('inferSchema', 'true') \
                   .option('header', 'true') \
                   .csv(CSV_PATH)

    brazil_df = df.filter((f.col('Country') == 'Brazil') &
                          (f.col('AverageTemperature').isNotNull())) \
                  .select('*', f.round(f.col('AverageTemperature'), 2).alias('avg_temp'),
                          f.round(f.col('AverageTemperatureUncertainty'), 2).alias('avg_temp_uncert')) \
                  .cache()

    brazil_df.groupBy(f.col('City')) \
             .agg(f.round(f.avg(f.col('avg_temp')), 2).alias('avg')) \
             .orderBy(f.col('avg').desc()) \
             .show()

    araras_yearly_avg_df = brazil_df.select(f.col('dt'), f.col('City'),
                                            f.col('avg_temp'),
                                            f.year(f.col('dt')).alias('year')) \
                                    .filter(f.col('City') == 'Araras') \
                                    .groupBy(f.col('year')) \
                                    .agg(f.round(f.avg(f.col('avg_temp')), 2).alias('avg_year')) \
                                    .orderBy(f.col('year').asc())

    brazil_df.createOrReplaceTempView('brazil_climate')
    araras_yearly_avg_df_sql = spark.sql("""SELECT YEAR(dt) AS year,
                                                   ROUND(AVG(avg_temp), 2) AS avg_year
                                            FROM brazil_climate
                                            WHERE City = 'Araras'
                                            GROUP BY year
                                            ORDER BY year ASC""")

    araras_yearly_avg_df.show()
    araras_yearly_avg_df_sql.show()

    spark.stop()
