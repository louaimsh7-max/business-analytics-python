def calculate_metrics(df):
    revenue = df["price"].sum()
    costs = df["cost"].sum()
    profit = df["profit"].sum()
    orders = len(df)

    if orders > 0:
        aov = revenue / orders
    else:
        aov = 0

    if revenue > 0:
        margin = profit / revenue * 100
    else:
        margin = 0

    return {
        "revenue": revenue,
        "costs": costs,
        "profit": profit,
        "orders": orders,
        "aov": aov,
        "margin": margin
    }

def profit_by_customer(df):
    return df.groupby("customer")["profit"].sum()


def profit_by_status(df):
    return df.groupby("status")["profit"].sum()