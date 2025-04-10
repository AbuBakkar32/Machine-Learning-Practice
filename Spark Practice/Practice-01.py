from pyspark.sql import SparkSession

# Step 2: Initialize Spark Session
spark = SparkSession.builder \
    .appName("Simple Spark Application") \
    .getOrCreate()

# Step 3: Load Data
data_path = "data.csv"  # Replace with your data file path
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Step 4: Perform Data Operations
# Example: Filter rows where a specific column value meets a condition
filtered_df = df.filter(df['Population'] > 100)  # Replace 'column_name' with actual column

# Example: Aggregate data
aggregated_df = filtered_df.groupBy('Yearly Change').count()  # Replace 'another_column' with actual column

# Step 5: Show Results
aggregated_df.show()

# Step 6: Stop Spark Session
spark.stop()
