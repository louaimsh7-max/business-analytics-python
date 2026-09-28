import csv
def load_orders_from_csv(filename):
    orders = []
    invalid_rows = 0

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            order = validate_order(row)

            if order is not None:
                orders.append(order)
            else:
                invalid_rows += 1

    return orders, invalid_rows

def validate_order(row):

    if not row["customer"]:
        print("Invalid order: customer is missing")
        return None

    if not row["price"]:
        print(f"Invalid order for {row['customer']}: price is missing")
        return None

    if not row["cost"]:
        print(f"Invalid order for {row['customer']}: cost is missing")
        return None

    try:
        price = float(row["price"])
        cost = float(row["cost"])
    except ValueError:
        print(f"Invalid price for {row['customer']}: {row['price']}")
        return None

    if price < 0 or cost < 0 :
        print(f"Invalid price for {row['customer']}: price cannot be negative")
        return None

    if row["status"] not in {"paid" , "pending"}:
        print(f"Invalid status")
        return None

    return {
        "customer": row["customer"],
        "price": price,
        "cost": cost,
        "status": row["status"]
    }
