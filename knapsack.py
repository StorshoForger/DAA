def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    items = []

    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i], i + 1))

    items.sort(reverse=True)

    total_value = 0.0

    print("Items taken:")

    for ratio, weight, value, item_no in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            print("Item", item_no, "full", weight, "kg", value)
        else:
            total_value += ratio * capacity
            print("Item", item_no, "partial", capacity, "kg", ratio * capacity)
            break

    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_val = fractional_knapsack(weights, values, capacity)
print("Maximum value:", max_val)
