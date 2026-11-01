
import pandas as pd

df = pd.read_csv("logistics_week3_data.csv")

print("===== LOGISTICS ANALYTICAL INSIGHTS =====")

# 1. Average delivery time by region
print("\n1. Average Delivery Time by Region")
print(df.groupby("Region")["Delivery_Time_Days"].mean().round(2))

# 2. Average cost by shipping mode
print("\n2. Average Transportation Cost by Shipping Mode")
print(df.groupby("Shipping_Mode")["Transportation_Cost"].mean().round(2))

# 3. Delivery status percentages
print("\n3. Delivery Status Percentage")
print(
    (df["Delivery_Status"].value_counts(normalize=True) * 100).round(2)
)

# 4. Most expensive region
print("\n4. Average Transportation Cost by Region")
region_cost = df.groupby("Region")["Transportation_Cost"].mean()
print(region_cost.round(2))
print("Highest cost region:", region_cost.idxmax())

# 5. Correlation between distance and cost
print("\n5. Distance and Transportation Cost Correlation")
print(
    df["Distance_KM"].corr(df["Transportation_Cost"]).round(3)
)

# 6. Delayed shipments
delayed = df[df["Delivery_Status"] == "Delayed"]
print("\n6. Total Delayed Shipments:", len(delayed))
print("Total Shipments:", len(df))

print("\nAnalysis completed successfully!")
