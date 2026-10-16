readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

above = 0
high = readings[0]
low = readings[0]
total = 0
count = 0

for v in readings:
    if v > 3.2:
        above += 1
    if v > high:
        high = v
    if v < low:
        low = v
    total += v
    count += 1

avg = round(total / count, 2)

print("Readings above 3.2 V:", above)
print("Highest:", high, "V")
print("Lowest:", low, "V")
print("Average:", avg, "V")
