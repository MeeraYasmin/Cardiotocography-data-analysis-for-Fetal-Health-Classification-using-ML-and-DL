import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("fetal_health.csv")
df.head()  # Display first 5 rows
df.tail()  # Display last 5 rows
df.shape  # Check dataset dimensions (Rows, Columns)
df.columns # Check column names
df.dtypes # Check data types of each column
df.isnull().sum() # Check for missing values
df.describe() # Summary statistics for numerical columns
df["fetal_health"].value_counts() # Value counts of the target column (fetal_health)
df.corr() # Check feature correlations
