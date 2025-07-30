# - Load energy logs from CSV, API, or sensor simulator
import pandas as pd
df = pd.read_csv("energy_logs.csv")
# - Clean missing or malformed readings
df['log_time'] = pd.to_datetime(df['log_time'], format='mixed', errors='coerce')
df['energy_used_kwh'] = pd.to_numeric(df['energy_used_kwh'], errors='coerce')
df = df[df['energy_used_kwh'] >= 0]
# - Use numpy to calculate total and average energy per device
grouped = df.groupby('device_id')['energy_used_kwh']
total_energy = grouped.sum()
average_energy = grouped.mean()
# - Use pandas to generate room-level summaries
devices = pd.read_csv('devices.csv')
merged = pd.merge(df, devices, on='device_id')
room_summary = merged.groupby('room_name')['energy_used_kwh'].agg(['sum', 'mean']).round(2)
print("Room-Level Summary:\n\n", room_summary)
df.to_csv("cleaned_energy_logs.csv", index=False)
room_summary.to_csv("room_energy_summary.csv")