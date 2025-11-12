# nums = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, nums))

# print(doubled)


# def outer(x):
#     def inner(y):
#         return x + y

#     return inner


# add_10 = outer(10)
# add_5 = outer(5)
# print(add_10)
# print(add_5)

# add_10 = outer(10)
# print(add_10(5))

# add_10 = outer(10)
# add_5 = add_10(5)

# print(add_5)

# print(outer(10)(5))


# def get_user_age():
#     while True:
#         try:
#             age = int(input("Enter your age: "))
#             if age <= 0:
#                 raise ValueError("Age must be positive.")
#             return age
#         except ValueError as e:
#             print(f"Invalid input: {e}")


# get_user_age()


# def calculate_average(*values: float) -> float:
#     """Return the average of given numeric values."""
#     if not values:
#         raise ValueError("No values provided.")
#     try:
#         return sum(values) / len(values)
#     except TypeError:
#         raise ValueError("All arguments must be numbers.")
#     finally:
#         print("Calculation completed.")


# calculate_average()
