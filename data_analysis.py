
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("logistics_week3_data.csv")

print("===== DATASET OVERVIEW =====")
print("Shape:", df.shape)

print("\n===== FIRST 5 RECORDS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

print("\n===== DELIVERY STATUS COUNTS =====")
print(df["Delivery_Status"].value_counts())

print("\n===== AVERAGE DELIVERY TIME =====")
print(df["Delivery_Time_Days"].mean())

print("\n===== MEDIAN TRANSPORTATION COST =====")
print(df["Transportation_Cost"].median())

print("\n===== AVERAGE DISTANCE =====")
print(df["Distance_KM"].mean())
