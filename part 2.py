import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

def calculate_bandwidth(data_rate, modulation_type, modulation_orders, coding_rate=1.0, spectral_efficiency_factor=1.0):
    """
    Calculate the required bandwidth for different modulation schemes and orders.
    
    :param data_rate: Target data rate in Mbps
    :param modulation_type: 'QAM' or 'PSK'
    :param modulation_orders: List of modulation orders
    :param coding_rate: Coding rate (default=1.0 for no error correction)
    :param spectral_efficiency_factor: Spectral efficiency adjustment factor
    :return: Dictionary of modulation orders and corresponding bandwidths in MHz
    """
    bandwidths = {}
    for M in modulation_orders:
        if M <= 1:
            continue  # Skip invalid modulation orders
        bits_per_symbol = np.log2(M)
        bandwidth = (data_rate * 1e6) / (bits_per_symbol * coding_rate * spectral_efficiency_factor)
        bandwidths[M] = bandwidth / 1e6  # Convert Hz to MHz
    
    return bandwidths

def main():
    data_rate = float(input("Enter target data rate (Mbps): "))
    modulation_orders = [2, 8, 16, 64, 512, 1024, 2048, 4096]
    
    print("\nQAM Modulation:")
    qam_bandwidths = calculate_bandwidth(data_rate, 'QAM', modulation_orders)
    for order, bw in qam_bandwidths.items():
        print(f"{order}-QAM: {bw:.3f} MHz")
    
    print("\nPSK Modulation:")
    psk_bandwidths = calculate_bandwidth(data_rate, 'PSK', modulation_orders)
    for order, bw in psk_bandwidths.items():
        print(f"{order}-PSK: {bw:.3f} MHz")

# Function to calculate SNR requirement using Shannon capacity formula
def calculate_snr(bps):
    snr_linear = (2 ** bps) - 1
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
plt.title("QAM Modulation Performance Analysis")
plt.grid()
plt.show()

if __name__ == "__main__":
    main()
