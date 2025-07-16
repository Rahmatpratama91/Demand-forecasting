import pandas as pd

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

# Tampilkan data dan contoh perhitungan rinci untuk salah satu kuartal
print(df)

# Contoh perhitungan manual untuk kuartal ke-2 (Q2 Year 1):
D_prev = demand[0]       # 98
F_prev = forecast[0]     # 98
F2 = alpha * D_prev + (1 - alpha) * F_prev
print(f"\nContoh perhitungan Q2 Year 1:")
print(f"F2 = {alpha} * {D_prev} + (1 - {alpha}) * {F_prev} = {F2:.2f}")