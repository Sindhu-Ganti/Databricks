# Databricks notebook source
# MAGIC %md
# MAGIC # Random Numbers DataFrame
# MAGIC This notebook demonstrates how to create and display a DataFrame with random numbers.

# COMMAND

import random
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

# COMMAND

# MAGIC %md
# MAGIC ## Method 1: Using Python list with random.randint()

# COMMAND

# Generate random data
num_rows = 10
random_data = [(i, random.randint(1, 100)) for i in range(1, num_rows + 1)]

# Create DataFrame with schema
schema = StructType([
    StructField("ID", IntegerType(), True),
    StructField("Random_Number", IntegerType(), True)
])

df_random = spark.createDataFrame(random_data, schema=schema)

# Display the DataFrame
display(df_random)

# COMMAND

# MAGIC %md
# MAGIC ## Method 2: Using NumPy for larger datasets

# COMMAND

import numpy as np

# Generate random numbers using NumPy
num_rows = 100
random_numbers = np.random.randint(1, 1000, num_rows)

# Create DataFrame
df_numpy = spark.createDataFrame(
    [(int(i), int(random_numbers[i])) for i in range(num_rows)],
    schema="ID INT, Random_Number INT"
)

# Display the DataFrame
display(df_numpy)

# COMMAND

# MAGIC %md
# MAGIC ## Method 3: Using Spark SQL for in-place generation

# COMMAND

# Create DataFrame using Spark SQL
df_spark_random = spark.sql("""
    SELECT 
        id,
        cast(rand() * 1000 as int) as Random_Number
    FROM (
        SELECT explode(sequence(1, 50)) as id
    )
""")

# Display the DataFrame
display(df_spark_random)

# COMMAND

# MAGIC %md
# MAGIC ## Summary Statistics

# COMMAND

# Show summary statistics for the random numbers
df_spark_random.describe().display()

# COMMAND

# MAGIC %md
# MAGIC ## Save the DataFrame (optional)

# COMMAND

# Save the DataFrame to Delta table (uncomment to use)
# df_spark_random.write.mode("overwrite").option("mergeSchema", "true").saveAsTable("random_numbers_table")

# Or save as CSV
# df_spark_random.write.mode("overwrite").csv("/tmp/random_numbers_output")

print("Notebook complete!")
