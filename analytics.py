def calculate_revenue(orders):
    total_revenue = 0
    for order in orders:
        total_revenue += order["price"]
    return total_revenue

def calculate_costs(orders):
    total_cost = 0
    for order in orders:
        total_cost += order["cost"]
    return total_cost

def calculate_profit(orders):
    total_profit = 0
    for order in orders:
        total_profit += order["price"] - order["cost"]
    return total_profit

def calculate_paid_orders(orders):
    paid_orders = 0 
    for order in orders:
        if order["status"] == "paid":
            paid_orders += 1
    return paid_orders

def calculate_aov(revenue, orders):
    return revenue/len(orders)

def calculate_margin(revenue, profit):
    return profit/revenue * 100