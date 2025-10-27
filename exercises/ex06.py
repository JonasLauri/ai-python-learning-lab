# Exercise 6 — Sales Tracker (dictionaries + lists + math + loops)
sales = [
    {"product": "Phone", "units": 10, "price": 599},
    {"product": "Laptop", "units": 4, "price": 1200},
    {"product": "Headphones", "units": 20, "price": 89},
    {"product": "Tablet", "units": 6, "price": 350},
]

# Calculate total revenue per product
products_revenue = [sale["units"] * sale["price"] for sale in sales]

# Print total shop revenue.
total_revenue = sum(products_revenue)
print(f"total revenue - {total_revenue}")

# Print which product generated the most income.
product_max_revenue = max(sales, key=lambda sale: sale["units"] * sale["price"])
print(f"{product_max_revenue['product']}")

# Show a warning if any product sold less than 5 units.
for sale in sales:
    if sale["units"] < 5:
        print(f"Warning - product {sale['product']} sold less than 5 units!")
