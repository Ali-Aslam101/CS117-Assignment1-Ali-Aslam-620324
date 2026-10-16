count = int(input("How many resistors? "))

total_resistance = 0

for i in range(1, count + 1):
    r = int(input(f"Enter R{i}: "))
    total_resistance += r

print("Total resistance =", total_resistance, "ohm")
