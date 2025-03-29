import math 

target_data_rate = 100.00  # Mbps
mod_orders = [2, 4, 8, 16, 32, 64, 128, 256]  # Typical PSK modulation orders
results = []

for M in mod_orders: 
    bits = math.log2(M)  # Bits per symbol
    baud_rate = target_data_rate / bits  # Symbol rate
    snr_req = 10 * math.log10(M)  # PSK SNR requirement in dB
    operating_SNR = 20  # Fixed operating SNR in dB
    
    # Adjust throughput based on SNR performance
    if operating_SNR < snr_req: 
        effective_throughput = target_data_rate * (operating_SNR / snr_req)
    else: 
        effective_throughput = target_data_rate

    bandwidth_req = target_data_rate / bits  # Bandwidth requirement
    
    results.append({
        "Modulation Order (M)": M,
        "Bits per Symbol": bits, 
        "Baud Rate (Msps)": baud_rate, 
        "SNR Requirement (dB)": snr_req, 
        "Bandwidth Required (MHz)": bandwidth_req,
        "Effective Throughput (Mbps)": effective_throughput            
    })
    
# Print results
for res in results: 
    print(res)
