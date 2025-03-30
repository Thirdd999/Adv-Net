import math
from scipy.special import erfcinv
from tabulate import tabulate  # Import for table formatting

def Qinv(x):
    """
    Compute the inverse Q-function:
    Q^{-1}(x) = sqrt(2) * erfcinv(2*x)
    """
    return math.sqrt(2) * erfcinv(2 * x)

# Parameters
target_data_rate = 100.00e6  # Mbps
target_SER = 1e-3  # Target symbol error rate
mod_orders = [2, 4, 8, 16, 32, 64, 512, 1024, 2048, 4096]  # PSK Modulation orders
operating_SNR_dB = 20  # Assumed operating SNR in dB

results = []

for M in mod_orders:
    bits_per_symbol = math.log2(M)  # Bits per symbol
    baud_rate = target_data_rate / bits_per_symbol  # Symbol rate in Msps

    # Compute PSK SNR requirement
    denom_psk = math.sqrt(2) * math.sin(math.pi / M)
    argument_psk = target_SER / 2
    
    try:
        q_inv_psk = Qinv(argument_psk)
    except Exception:
        q_inv_psk = float('nan')

    snr_linear_psk = (q_inv_psk / denom_psk) ** 2
    snr_dB_psk = 10 * math.log10(snr_linear_psk) if snr_linear_psk > 0 else float('nan')

    # Compute Effective Throughput for PSK
    if operating_SNR_dB < snr_dB_psk:
        effective_throughput_psk = target_data_rate * (operating_SNR_dB / snr_dB_psk)
    else:
        effective_throughput_psk = target_data_rate

    # Bandwidth Requirement (assuming symbol rate is proportional to bandwidth)
    bandwidth_req = baud_rate  # MHz (assuming Nyquist criterion)

    results.append([
        M,
        bits_per_symbol,
        f"{baud_rate / 1e6:.2f} Msps",
        f"{snr_dB_psk:.2f} dB",
        f"{bandwidth_req / 1e6:.2f} MHz",
        f"{effective_throughput_psk / 1e6:.2f} Mbps"
    ])

# Print results in table format
headers = ["Modulation Order", "Bits per Symbol", "Baud Rate", "SNR Req (dB)", "Bandwidth Req", "Effective Throughput"]
print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
