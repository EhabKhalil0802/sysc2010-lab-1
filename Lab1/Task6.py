import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("env_temp_humidity_clean.csv")

print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values per column:")
print(df.isna().sum())

plt.figure()
plt.plot(df["timestamp"], df["temperature_C"])
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(df["timestamp"], df["humidity_pct"])
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.title("Humidity vs Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
