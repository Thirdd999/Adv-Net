import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input Parameters
target_data_rate = 100e6  # 100 Mbps
modulation_orders = [2, 4, 8, 16, 32, 64, 128, 256]  # PSK Modulation Orders
bandwidth_efficiency = 1.2  # Assumed spectral efficiency factor (depends on system design)

# Function to calculate SNR requirement for PSK using approximate Eb/N0 formula
def calculate_snr(bps):
    snr_linear = (np.sin(np.pi / (2 ** bps))) ** -2
    snr_db = 10 * np.log10(snr_linear)
    return snr_db

# Compute Key Values
data = []
for m in modulation_orders:
    bits_per_symbol = int(np.log2(m))
    baud_rate = target_data_rate / bits_per_symbol
    effective_throughput = baud_rate * bits_per_symbol
    snr_requirement = calculate_snr(bits_per_symbol)
    bandwidth_required = baud_rate / bandwidth_efficiency
    
    data.append([m, bits_per_symbol, baud_rate, effective_throughput, snr_requirement, bandwidth_required])

# Create DataFrame
df = pd.DataFrame(data, columns=["Modulation Order", "Bits per Symbol", "Baud Rate (Hz)","Effective Throughput (bps)", "SNR Requirement (dB)", "Bandwidth Required (Hz)"])

# Display Table
print(df)

# Plot Results
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()
ax1.plot(df["Modulation Order"], df["Baud Rate (Hz)"], 'g-o', label='Baud Rate')
ax1.plot(df["Modulation Order"], df["Bandwidth Required (Hz)"], 'b-s', label='Bandwidth Required')
ax2.plot(df["Modulation Order"], df["SNR Requirement (dB)"], 'r-d', label='SNR Requirement')

ax1.set_xlabel("Modulation Order")
ax1.set_ylabel("Baud Rate / Bandwidth Required (Hz)", color='g')
ax2.set_ylabel("SNR Requirement (dB)", color='r')
ax1.set_xscale('log', base=2)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title("PSK Modulation Performance Analysis")
plt.grid()
plt.show()
