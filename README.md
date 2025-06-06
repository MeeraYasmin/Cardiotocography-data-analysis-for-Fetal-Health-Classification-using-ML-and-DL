# Fetal Health Classification

This dataset contains fetal health records with various medical features. The goal is to analyze the data, visualize important trends, and build machine learning models to classify fetal health into **Normal**, **Suspect**, and **Pathological** categories.

## Dataset Overview
-**Number of Features:** 21

-**Target Variable:** fetal_health (1- Normal, 2- Suspect, 3- Pathological)

-**Total Samples:** 2126

-**Data Type:** all features are numerical

## Exploratory Data Analysis (EDA)
To understand the dataset better, the following EDA techniques were applied.

### Basic Inspection
-**'df.head()'**, **'df.tail()'** to examine records.

-**'df.shape'** to check dataset dimensions.

-**'df.columns'** to list all feature names.

-**'df.dtypes'** to verify data types of each column.

### Data Quality Checks
-**'df.isnull().sum()'** to check for missing values.

-**'df.describe()'** to get summary statistics of numerical features.

### Target Distribution
-**'df["fetal_health"].value_counts()'** to analyze class distribution.

### Feature Relationships
-**'df.corr()'** to compute correlation between features and identify potential dependencies.

These steps help in identifying data patterns, inconsistencies, and insights that guide feature selection and model building.
---
# Visualization of Fetal Health Distribution

Understanding the distribution of fetal health classes is essential for identifying imbalances in the dataset. Below, we use **a pie chart and a bar chart** to visualize the proportion of **Normal, Suspect, and Pathological** cases. This helps in assessing whether the dataset is balanced or if preprocessing is required.

Additionally, **histograms** provide deeper insights into the distribution of individual features, helping identify skewness, outliers, and patterns. The **correlation heatmap** further reveals relationships between features, highlighting potential dependencies that can influence model performance.


