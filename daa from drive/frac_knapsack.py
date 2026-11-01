# ---------------- Fractional Knapsack Function ----------------
def fractional_knapsack(weights, values, capacity):
    n = len(values)
    ratio = []

    for i in range(n):
        if weights[i] == 0:
            print(f"Skipping item {i+1} (weight is 0, invalid).")
            continue
        ratio.append((values[i] / weights[i], i))

    ratio.sort(reverse=True)

    total_value = 0.0
    fractions = [0.0] * n

    for r, i in ratio:
        if capacity == 0:
            break

        if weights[i] <= capacity:
            total_value += values[i]
            capacity -= weights[i]
            fractions[i] = 1
        else:
            fraction = capacity / weights[i]
            total_value += values[i] * fraction
            fractions[i] = fraction
            capacity = 0

    return total_value, fractions


# ---------------- Main Program ----------------
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    values = []
    weights = []

    for i in range(n):
        val = float(input(f"Enter value of item {i+1}: "))
        wt = float(input(f"Enter weight of item {i+1}: "))
        values.append(val)
        weights.append(wt)

    capacity = float(input("Enter capacity of knapsack: "))

    max_value, fractions = fractional_knapsack(weights, values, capacity)

    print("\nItem | Value | Weight | Fraction Taken")
    print("---------------------------------------")
    for i in range(n):
        print(f"{i+1:4d} | {values[i]:6.2f} | {weights[i]:7.2f} | {fractions[i]:14.2f}")

    print("\nMaximum value that can be obtained = {:.2f}".format(max_value))
