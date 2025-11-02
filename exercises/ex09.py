# Exercise 5 — Basic Data Analyzer

data = [4, 7, 10, 2, 9, 4, 3, 8, 4, 6]

# Calculate mean, min, max, and range.
mean_data = sum(data) / len(data) if data else 0
min_data = min(data)
max_data = max(data)
range_data = len(data)

# Count how many values are above the mean.
# range_above_mean = [num for num in data if num > mean_data]
# count_above_mean = len(range_above_mean)
count_above_mean = sum(num > mean_data for num in data)
# print(count_above_mean)

# Create a new list with only unique numbers, sorted ascending.
unique_sorted = sorted(set(data))
# print(unique_sorted)
