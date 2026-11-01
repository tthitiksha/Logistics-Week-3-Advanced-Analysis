
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("logistics_week3_data.csv")

sns.set_theme(style="whitegrid")

# 1. Delivery Time Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Delivery_Time_Days"], bins=12, kde=True)
plt.title("Distribution of Delivery Times")
plt.xlabel("Delivery Time (Days)")
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.savefig("delivery_time_distribution.png")
plt.close()

# 2. Transportation Cost by Shipping Mode
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Shipping_Mode", y="Transportation_Cost")
plt.title("Transportation Cost by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Transportation Cost")
plt.tight_layout()
plt.savefig("transportation_cost_by_mode.png")
plt.close()

# 3. Distance vs Transportation Cost
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Distance_KM",
    y="Transportation_Cost",
    hue="Shipping_Mode"
)
plt.title("Distance vs Transportation Cost")
plt.xlabel("Distance (KM)")
plt.ylabel("Transportation Cost")
plt.tight_layout()
plt.savefig("distance_vs_cost.png")
plt.close()

# 4. Correlation Heatmap
numerical_data = df.select_dtypes(include="number").drop(
    columns=["Order_ID"]
)
plt.figure(figsize=(10, 7))
sns.heatmap(
    numerical_data.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Logistics Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# 5. Delivery Status by Region
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="Region",
    hue="Delivery_Status"
)
plt.title("Delivery Status by Region")
plt.xlabel("Region")
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.savefig("delivery_status_by_region.png")
plt.close()

print("All 5 visualizations generated successfully!")
