import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    feb_orders = orders[
        (orders['order_date'] >= '2020-02-01') &
        (orders['order_date'] < '2020-03-01')
    ]

    totals = feb_orders.groupby('product_id')['unit'].sum().reset_index(name='unit')

    totals = totals[totals['unit'] >= 100]

    result = totals.merge(products, on='product_id', how='left')

    return result[['product_name', 'unit']]