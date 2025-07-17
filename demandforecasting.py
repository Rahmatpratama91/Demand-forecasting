import pandas as pd
import matplotlib.pyplot as plt

# Data permintaan kuartalan dalam ribuan
demand = [98, 106, 109, 133, 130, 116, 133, 116,
          138, 130, 147, 141, 144, 142, 165, 173]

alpha = 0.1  # nilai smoothing

# Forecast pertama diinisialisasi sama dengan demand pertama
forecast = [demand[0]]  # F1 = D1

# Hitung forecast menggunakan simple exponential smoothing
for t in range(1, len(demand)):
    Ft = alpha * demand[t-1] + (1 - alpha) * forecast[t-1]
    forecast.append(Ft)

# Buat DataFrame hasilnya
quarters = [f"Q{i%4 + 1} Y{i//4 + 1}" for i in range(len(demand))]
df = pd.DataFrame({
    'Quarter': quarters,
    'Demand (000s)': demand,
    'Forecast (000s)': [round(f, 2) for f in forecast]
})

# Tampilkan tabel
print(df)

# Visualisasi
plt.figure(figsize=(12, 6))
plt.plot(df['Quarter'], df['Demand (000s)'], marker='o', label='Actual Demand')
plt.plot(df['Quarter'], df['Forecast (000s)'], marker='s', linestyle='--', label='Forecast (SES)')
plt.xticks(rotation=45)
plt.xlabel("Quarter")
plt.ylabel("Demand (in 000s)")
plt.title("Simple Exponential Smoothing Forecast")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()