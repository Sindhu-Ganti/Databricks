# Databricks notebook source
# MAGIC %md
# MAGIC # Pie Chart Visualization
# MAGIC This notebook demonstrates how to create and display pie charts in Databricks using different methods.

# COMMAND

# MAGIC %md
# MAGIC ## Setup: Import Required Libraries

# COMMAND

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession

# COMMAND

# MAGIC %md
# MAGIC ## Method 1: Simple Pie Chart with Matplotlib

# COMMAND

# Sample data
categories = ['Sales', 'Marketing', 'Development', 'Support', 'HR']
values = [35, 20, 25, 12, 8]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Department Budget Distribution', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# COMMAND

# MAGIC %md
# MAGIC ## Method 2: Pie Chart from Spark DataFrame

# COMMAND

# Create a Spark DataFrame with data
data = [
    ('Product A', 150),
    ('Product B', 200),
    ('Product C', 120),
    ('Product D', 180),
    ('Product E', 250)
]

df_products = spark.createDataFrame(data, schema=['Product', 'Sales'])

# Convert to Pandas for visualization
df_pandas = df_products.toPandas()

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(df_pandas['Sales'], labels=df_pandas['Product'], autopct='%1.1f%%', startangle=45)
plt.title('Product Sales Distribution', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# COMMAND

# MAGIC %md
# MAGIC ## Method 3: Multiple Pie Charts (Subplots)

# COMMAND

# Create multiple datasets
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Pie chart 1: Q1 Sales
q1_data = [45, 55, 40]
q1_labels = ['North', 'South', 'West']
axes[0].pie(q1_data, labels=q1_labels, autopct='%1.1f%%', colors=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[0].set_title('Q1 Sales by Region', fontweight='bold')

# Pie chart 2: Q2 Sales
q2_data = [50, 60, 35]
q2_labels = ['North', 'South', 'West']
axes[1].pie(q2_data, labels=q2_labels, autopct='%1.1f%%', colors=['#FFA07A', '#98D8C8', '#FF9FF3'])
axes[1].set_title('Q2 Sales by Region', fontweight='bold')

plt.tight_layout()
plt.show()

# COMMAND

# MAGIC %md
# MAGIC ## Method 4: Donut Chart (Pie Chart with a hole)

# COMMAND

# Donut chart data
sizes = [30, 25, 20, 15, 10]
labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

# Create donut chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', 
                                    colors=colors, startangle=90)

# Draw circle to create donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

ax.set_title('Market Share (Donut Chart)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# COMMAND

# MAGIC %md
# MAGIC ## Method 5: Interactive Pie Chart with Plotly

# COMMAND

try:
    import plotly.express as px
    import plotly.graph_objects as go
    
    # Create interactive pie chart
    data = {
        'Technology': ['Python', 'Scala', 'SQL', 'R', 'Java'],
        'Usage': [45, 20, 18, 12, 5]
    }
    
    df_tech = pd.DataFrame(data)
    
    fig = px.pie(df_tech, values='Usage', names='Technology', 
                 title='Programming Language Usage in Data Engineering')
    fig.show()
    
except ImportError:
    print("Plotly not installed. Install it using: pip install plotly")

# COMMAND

# MAGIC %md
# MAGIC ## Display DataFrame Summary

# COMMAND

# Display the product sales DataFrame
print("Product Sales Data:")
display(df_products)

# COMMAND

print("✓ Pie chart visualizations completed successfully!")
