from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Create Spark session
spark = SparkSession.builder \
    .appName("TransformOrders") \
    .getOrCreate()

# Replace with your GCS bucket path later
input_path = "gs://order-pipeline-bucket-cm/input/sample_orders.csv" 
output_path = "gs://order-pipeline-bucket-cm/output/transformed_orders" 

# Load CSV
df = spark.read.option("header", "true").csv(input_path)

# Basic type casting
df = df.withColumn("order_id", col("order_id").cast("int")) \
       .withColumn("customer_id", col("customer_id").cast("int")) \
       .withColumn("quantity", col("quantity").cast("int")) \
       .withColumn("price", col("price").cast("double")) \
       .withColumn("total_price", expr("quantity * price"))

# Optional: Filter completed orders only
df_filtered = df.filter(col("status") == "completed")

# Save transformed data
df_filtered.write.mode("overwrite").parquet(output_path)

print("Transformation complete.")
spark.stop()
