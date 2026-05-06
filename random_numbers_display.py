# Databricks notebook source
# MAGIC %md
# MAGIC # Random Numbers DataFrame Display
# MAGIC This notebook generates and displays random numbers in a DataFrame using multiple methods.

# COMMAND

# MAGIC %md
# MAGIC ## Setup: Import Required Libraries

# COMMAND

import random
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType

# COMMAND

# MAGIC %md
# MAGIC ## Method 1: Generate Random Integers using Python

# COMMAND

# Create a list of random integers
random_integers = [random.randint(1, 100) for _ in range(20)]

# Create DataFrame from list
df_integers = spark.createDataFrame(
    [(i+1, num) for i, num in enumerate(random_integers)],
    schema="ID INT, Random_Number INT"
)

# Display the DataFrame
print("Random Integers (1-100):")
display(df_integers)

# COMMAND

# MAGIC %md
# MAGIC ## Method 2: Generate Random Floats using NumPy

# COMMAND

# Generate random floats using NumPy
random_floats = np.random.uniform(0, 1, 15)

# Create DataFrame
df_floats = spark.createDataFrame(
    [(i+1, float(num)) for i, num in enumerate(random_floats)],
    schema="ID INT, Random_Float DOUBLE"
)

# Display the DataFrame
print("Random Floats (0-1):")
display(df_floats)

# COMMAND

# MAGIC %md
# MAGIC ## Method 3: Generate Large Random Dataset using Spark

# COMMAND

# Create a larger dataset using Spark SQL
df_large = spark.sql("""
    SELECT 
        id,
        CAST(RAND() * 10000 AS INT) as Random_Number,
        RAND() as Random_Float
    FROM (
        SELECT explode(sequence(1, 100)) as id
    )
""")

# Display the DataFrame
print("Large Random Dataset (100 rows):")
display(df_large)

# COMMAND

# MAGIC %md
# MAGIC ## Statistics Summary

# COMMAND

# Show statistics for random numbers
print("Summary Statistics:")
display(df_large.describe())

# COMMAND

# MAGIC %md
# MAGIC ## Display Count and Distribution

# COMMAND

# Show row count and basic info
print(f"Total rows in large dataset: {df_large.count()}")
print("\nFirst 10 rows:")
display(df_large.limit(10))

# COMMAND

print("✓ Notebook execution completed successfully!")
