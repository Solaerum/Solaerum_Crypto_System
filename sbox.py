import numpy as np

# Parameters for the Rossler attractor
a = 0.2
b = 0.2
c = 5.7

# Function to normalize the key bytes to [0, 10]
def normalize_key_to_range(key_bytes, lower=0, upper=10):
    return [lower + (upper - lower) * (byte / 255) for byte in key_bytes]

# Rossler attractor system
def rossler_attractor(x0, y0, z0, steps=1000):
    # Time step for integration
    dt = 0.01
    x, y, z = x0, y0, z0
    result = []
    
    for _ in range(steps):
        dx = (-y - z) * dt
        dy = (x + a * y) * dt
        dz = (b + z * (x - c)) * dt
        x += dx
        y += dy
        z += dz
        result.append((x, y, z))
    
    return result

# Extract the first 3 bytes of the key for the initial conditions
key = [198, 47, 210]  # Example key bytes
normalized_values = normalize_key_to_range(key)

# Initialize the attractor with the first 3 normalized key bytes
x0, y0, z0 = normalized_values[0], normalized_values[1], normalized_values[2]

# Run the Rossler attractor for a number of steps
steps = 1000
attractor_output = rossler_attractor(x0, y0, z0, steps)

# Extract a portion of the attractor output to generate the S-box (using the x component)
s_box_values = [int((output[0] % 1) * 255) for output in attractor_output]

# Output the first few S-box values
print(s_box_values[:16])  # Print first 16 values as a sample of the S-box

