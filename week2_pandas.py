import pandas as pd
from analytics_engine import (
    calculate_metrics,
    profit_by_customer,
    profit_by_status
)

df = pd.read_csv("orders.csv")

df["price"] = pd.to_numeric(df["price"], errors="coerce")

valid_price = df["price"].notna()

valid_orders = df[valid_price].copy()

valid_orders["profit"] = valid_orders["price"] - valid_orders["cost"]

metrics = calculate_metrics(valid_orders)

print()
print("=== BUSINESS ANALYTICS ENGINE V1 ===")

print("Revenue:", metrics["revenue"])
print("Costs:", metrics["costs"])
print("Profit:", metrics["profit"])
print("Orders:", metrics["orders"])
print("AOV:", metrics["aov"])
print("Profit margin:", metrics["margin"])

print()
print("=== PROFIT BY CUSTOMER ===")
print(profit_by_customer(valid_orders))

print()
print("=== PROFIT BY STATUS ===")
print(profit_by_status(valid_orders))

