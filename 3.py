# Step 1: Create new record
import pandas as pd

# Sample sales dataset (20 rows)
data = {
    "OrderID": range(1001, 1021),
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", 
        "Headphones", "Mouse", "Chair", "Desk", "Laptop",
        "Printer", "Keyboard", "Monitor", "Mouse", "Laptop",
        "Headphones", "Desk", "Monitor", "Printer", "Chair"
    ],
    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics", "Electronics",
        "Accessories", "Accessories", "Furniture", "Furniture", "Electronics",
        "Electronics", "Accessories", "Electronics", "Accessories", "Electronics",
        "Accessories", "Furniture", "Electronics", "Electronics", "Furniture"
    ],
    "Quantity": [2, 5, 3, 4, 1, 6, 10, 2, 1, 3, 2, 4, 2, 7, 5, 3, 2, 4, 1, 6],
    "Price": [800, 20, 50, 200, 850, 40, 25, 150, 300, 900, 120, 55, 250, 20, 750, 35, 280, 220, 110, 180],
    "Customer": [
        "Alice", "Bob", "Charlie", "Diana", "Ethan",
        "Fiona", "George", "Hannah", "Ian", "Jane",
        "Kyle", "Laura", "Mike", "Nina", "Oscar",
        "Paul", "Queen", "Robert", "Sarah", "Tom"
    ],
    "Region": [
        "North", "South", "East", "West", "North",
        "South", "East", "West", "North", "South",
        "East", "West", "North", "South", "East",
        "West", "North", "South", "East", "West"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute Total column


# Step 1: Create new record
new_row = {
    "OrderID": 1021,
    "Product": "Tablet",
    "Category": "Electronics",
    "Quantity": 2,
    "Price": 450,
    "Customer": "Victor",
    "Region": "East",
    "Total": 2 * 450
}

# Step 2: Append to DataFrame
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

df["Total"] = df["Quantity"] * df["Price"]

# Step 3: Show last 3 rows
print(df.tail(3))

