import math 

target_data_rate = 100.00 #Mbps 
mod_orders = [2, 8, 16, 64, 512, 1024, 2048, 4096] 
results = []
for M in mod_orders: 
    bits = math.log2(M)
    baud_rate = target_data_rate / bits 
    snr_req = bits + 5
    operating_SNR = 20 
    if operating_SNR < snr_req: 
        effective_throughput = target_data_rate * (operating_SNR / snr_req)
    else: 
        effective_throughput = target_data_rate

    bandwidth_req = target_data_rate / bits 
    results.append({
        "Modulation Order": M,
        "Bits per Symbol": bits, 
        "Baud Rate": baud_rate, 
        "SNR Requirement (dB)": snr_req, 
        "Bandwidth Required (MHz)": bandwidth_req,
        "Effective Throughput (Mbps)": effective_throughput            


      })
    
for res in results: 
    print(res)
