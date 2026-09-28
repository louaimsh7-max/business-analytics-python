from data_loader import load_orders_from_csv
from analytics import (
    calculate_revenue,
    calculate_costs,
    calculate_profit,
    calculate_paid_orders,
    calculate_aov,
    calculate_margin
)
    


def main():
    orders, invalid_rows = load_orders_from_csv("orders.csv")
    customers = [order["customer"] for order in orders]
    paid_order_list = [order for order in orders if order["status"] == "paid"]
    paid_orders = calculate_paid_orders(orders)
    revenue = calculate_revenue(orders)
    costs = calculate_costs(orders)
    profit = calculate_profit(orders)
    aov = calculate_aov(revenue, orders)
    margin = calculate_margin(revenue, profit)
    print(customers)
    print(paid_orders)
    

    print("\n=== BUSINESS ANALYTICS  ===")
    print(f"Revenue: €{revenue:.2f}")
    print(f"Costs: €{costs:.2f}")
    print(f"Profit: €{profit:.2f}")
    print(f"Paid orders: {paid_orders}")
    print(f"AOV: €{aov:.2f}")
    print(f"Profit margin: {margin:.2f}%")
    print(f"Invalid rows: {invalid_rows}")

if __name__ ==  "__main__":
    main()

