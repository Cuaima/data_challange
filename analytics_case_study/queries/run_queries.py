from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("TopPurchasedProducts") \
    .config("spark.driver.extraClassPath", "/path/to/sqlite-jdbc.jar") \
    .getOrCreate()

# Path to the SQLite database
db_path = "../website_data.db"
db_url = f"jdbc:sqlite:{db_path}"

# Read the purchases table from the SQLite database
purchases_df = spark.read.format("jdbc") \
    .option("url", db_url) \
    .option("dbtable", "purchases") \
    .option("driver", "org.sqlite.JDBC") \
    .load()

# Group by product_id and count purchases
top_products = purchases_df.groupBy("product_id") \
    .count() \
    .orderBy("count", ascending=False) \
    .limit(10)

# Show the results
top_products.show()

# Stop the Spark session
spark.stop()