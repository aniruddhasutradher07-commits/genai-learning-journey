import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counts = orders.groupby('customer_number').size().reset_index(name='order_count')
    top_customer = counts.loc[counts['order_count'].idxmax(),['customer_number']]
    return pd.DataFrame([top_customer])