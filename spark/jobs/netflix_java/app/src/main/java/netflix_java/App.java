package netflix_java;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import static org.apache.spark.sql.functions.*;

public class App {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
            .master("spark://spark:7077")
            .appName("Netflix Java")
            .getOrCreate();

        spark.sparkContext().setLogLevel("ERROR");

        try {
            Dataset<Row> df = spark.read()
                .option("inferSchema", "true")
                .option("header", "true")
                .csv("/app/datasets/netflix_titles.csv");

            df.groupBy("release_year")
                .count()
                .orderBy(col("count").desc())
                .show();

            df.groupBy("type")
                .count()
                .orderBy(col("count").desc())
                .show();

            System.out.println(df.filter(col("listed_in").like("%Horro Movies%")).count());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            spark.stop();
        }
    }
}
