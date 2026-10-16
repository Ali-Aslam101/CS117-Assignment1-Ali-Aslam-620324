def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return (i ** 2) * r

# Test values
voltage = 12
resistance = 6

# Function calls
current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)

# Print results outside the functions
print(f"Current = {current:.1f} A")
print(f"Power = {power:.1f} W")
