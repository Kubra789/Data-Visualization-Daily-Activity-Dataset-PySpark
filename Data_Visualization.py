# Databricks notebook source
# Daily Activity Dataset/ Data Visualization With PySpark

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# COMMAND ----------

spark= SparkSession.builder.appName("Data Visualization Çalışması").getOrCreate()

# COMMAND ----------

df=spark.read.option("delimiter",",").option("header","true").option("inferSchema","true").csv("/FileStore/tables/DailyActivities.csv")

# COMMAND ----------

df.show(truncate=False)

# COMMAND ----------

display(df)

# COMMAND ----------

display(df)

# COMMAND ----------

display(df)

# COMMAND ----------

display(df)

# COMMAND ----------

display(df)

# COMMAND ----------


