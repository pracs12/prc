def fractional_knapsack(weights,values,capacity):
    n = len(values)
    ratio = []

    for i in range(n):
        if weights[i] == 0:
            print("Skipping as invalid weight")

        ratio.append((values[i]/weights[i],i))

    ratio.sort(reverse=True)

    total_val = 0.0
    fractions = [0.0] * n

    for r,i in ratio:
        if capacity == 0:
            break

        if weights[i] <= capacity:
            total_val += values[i]
            capacity -= weights[i]
            fractions[i] = 1
        else:
            frac = capacity / weights[i]
            total_val += values[i] * frac
            fractions[i] = frac
            capacity = 0
    

    return total_val, fractions


if __name__ == "__main__":
    n = int(input("Enter the number of items:"))

    weights = []
    values = []

    for i in range(n):
        val = float(input(f"Enter the value of item{i+1}:"))
        wt = float(input(f"Enter the weight of item {i+1}:"))
        values.append(val)
        weights.append(wt)

    capacity = float(input("Enter the capacity of knapsack")) 

    max_profit,fractions = fractional_knapsack(weights,values,capacity)

    print(f"Item\tValue\tWeight\tFraction Taken")
    print("--------------------------------------")

    for i in range(n):
        print(f"{i+1}\t {values[i]}\t {weights[i]} \t {fractions[i]}")


    print("Maximum Profit:",max_profit)       