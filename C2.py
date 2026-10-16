def parallel_resistance(resistors):
    # R_eq = 1 / sum(1 / R_i)
    return 1 / sum(1 / r for r in resistors)

# Sample test cases
test1 = parallel_resistance([10, 10])
test2 = parallel_resistance([100, 200, 300])

# Print results outside the function
print(f"parallel_resistance([10, 10]) -> {round(test1, 2)}")
print(f"parallel_resistance([100, 200, 300]) -> {round(test2, 2)}")
