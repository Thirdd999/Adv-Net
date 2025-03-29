import numpy as np
import matplotlib.pyplot as plt
def get_symbol_coord(mod_type, symbol_bits):
    """
    Compute the (x, y) coordinate for a given binary symbol based on the modulation type.
    
    Parameters:
        mod_type (str): Modulation type ("QAM", "PSK", "ASK", "FSK", "CSS").
        symbol_bits (str): Binary string representing the symbol.
        
    Returns:
        tuple: (x, y) coordinate.
    """
    n = len(symbol_bits)
    mod = mod_type.upper()
    
    if mod == "QAM":
        # For QAM, split bits equally into I and Q parts.
        half = n // 2
        I = int(symbol_bits[:half], 2)
        Q = int(symbol_bits[half:], 2)
        # Center the constellation by subtracting the midpoint.
        mid = (2**half - 1) / 2
        return (I - mid, Q - mid)
    
    elif mod == "PSK":
        # For PSK, treat the entire binary string as an integer to compute an angle.
        value = int(symbol_bits, 2)
        angle = 2 * np.pi * value / (2**n)
        return (np.cos(angle), np.sin(angle))
    
    elif mod == "ASK":
        # For ASK, map the integer value to an amplitude in [-1, 1].
        value = int(symbol_bits, 2)
        amplitude = (value / (2**n - 1)) * 2 - 1
        return (amplitude, 0)
    
    elif mod == "FSK":
        # For FSK, a simple one-dimensional mapping based on the integer value.
        value = int(symbol_bits, 2)
        return (value, 0)
    
    elif mod == "CSS":
        # For CSS (Chirp Spread Spectrum), use an abstract mapping.
        # Here, we map the integer value into a grid pattern.
        value = int(symbol_bits, 2)
        return (value % 5, value // 5)
    
    else:
        raise ValueError("Unsupported modulation type. Choose from QAM, PSK, ASK, FSK, CSS.")

def main():
    # The input word
    word = "antenna"
    
    # Convert each character to its ASCII code and then to an 8-bit binary representation.
    ascii_codes = [ord(char) for char in word]
    binary_codes = [format(code, '08b') for code in ascii_codes]
    
    print("Word:", word)
    print("ASCII Codes:", ascii_codes)
    print("Binary Codes:", binary_codes)
    
    # Choose a modulation type: "QAM", "PSK", "ASK", "FSK", or "CSS"
    mod_type = "CSS"  # Change this value as needed.
    
    # Compute the constellation coordinates for each symbol.
    coordinates = [get_symbol_coord(mod_type, bits) for bits in binary_codes]
    print("Coordinates for modulation type", mod_type, ":", coordinates)
    
    # Plotting the constellation diagram.
    xs = [coord[0] for coord in coordinates]
    ys = [coord[1] for coord in coordinates]
    
    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, color='blue')
    
    # Annotate each point with its binary symbol.
    for i, (x, y) in enumerate(coordinates):
        plt.annotate(binary_codes[i], (x, y), textcoords="offset points", xytext=(5, 5))
    
    plt.title(f"Constellation Diagram ({mod_type}) for word '{word}'")
    plt.xlabel("I (In-phase)" if mod_type.upper() == "QAM" else "X")
    plt.ylabel("Q (Quadrature)" if mod_type.upper() == "QAM" else "Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    
if __name__ == "__main__":
    main()
