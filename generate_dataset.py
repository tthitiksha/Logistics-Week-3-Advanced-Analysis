
import pandas as pd
import numpy as np

np.random.seed(42)
n = 600

region = np.random.choice(["North", "South", "East", "West"], n)
mode = np.random.choice(["Standard", "Express", "Same Day"], n)

distance = np.random.randint(10, 1001, n)
weight = np.random.randint(1, 101, n)
volume = np.random.randint(1, 51, n)

scheduled = np.random.randint(2, 9, n)

# Realistic cost relationships
mode_cost = np.select(
    [mode == "Standard", mode == "Express"],
    [300, 700],
    default=1200
)

transport_cost = (
    150 + distance * 2.2 + weight * 8
    + volume * 12 + mode_cost
    + np.random.normal(0, 180, n)
)
transport_cost = np.maximum(transport_cost, 100)

fuel_cost = distance * 0.8 + np.random.normal(100, 40, n)
fuel_cost = np.maximum(fuel_cost, 50)

# Delivery time increases with distance
delivery_time = (
    1 + distance / 180
    + np.where(mode == "Express", -1, 0)
    + np.where(mode == "Same Day", -2, 0)
    + np.random.normal(0, 1, n)
)
delivery_time = np.maximum(1, np.round(delivery_time)).astype(int)

status = np.where(
    delivery_time > scheduled, "Delayed",
    np.where(delivery_time < scheduled, "Early", "On Time")
)

df = pd.DataFrame({
    "Order_ID": range(1001, 1001 + n),
    "Region": region,
    "Shipping_Mode": mode,
    "Distance_KM": distance,
    "Shipment_Weight_KG": weight,
    "Shipment_Volume": volume,
    "Scheduled_Delivery_Days": scheduled,
    "Delivery_Time_Days": delivery_time,
    "Transportation_Cost": transport_cost.round(2),
    "Fuel_Cost": fuel_cost.round(2),
    "Delivery_Status": status
})

df.to_csv("logistics_week3_data.csv", index=False)

print("Improved dataset generated successfully!")
print("Dataset shape:", df.shape)
print(df.head())

