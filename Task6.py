import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("env_temp_humidity_clean.csv")

# Display basic info
print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values per column:")
print(df.isna().sum())

# Plot temperature vs time
plt.figure()
plt.plot(df["timestamp"], df["temperature_C"])
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot humidity vs time
plt.figure()
plt.plot(df["timestamp"], df["humidity_pct"])
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.title("Humidity vs Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
