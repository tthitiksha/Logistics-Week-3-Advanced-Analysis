
import pandas as pd

# Load dataset
df = pd.read_csv("logistics_week3_data.csv")

# Select numerical columns
numerical_data = df[
    [
        "Distance_KM",
        "Shipment_Weight_KG",
        "Shipment_Volume",
        "Scheduled_Delivery_Days",
        "Delivery_Time_Days",
        "Transportation_Cost",
        "Fuel_Cost"
    ]
]

# Calculate correlation
correlation_matrix = numerical_data.corr()

print("===== CORRELATION MATRIX =====")
print(correlation_matrix.round(2))

# Save correlation results
correlation_matrix.to_csv("correlation_results.csv")

print("\nCorrelation analysis completed!")
