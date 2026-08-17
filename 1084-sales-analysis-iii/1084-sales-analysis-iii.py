import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    grouped = sales.groupby('product_id')['sale_date'].agg(['min', 'max']).reset_index()
    
    q1_start = pd.Timestamp('2019-01-01')
    q1_end = pd.Timestamp('2019-03-31')
    
    valid_products = grouped[
        (grouped['min'] >= q1_start) & (grouped['max'] <= q1_end)
    ]['product_id']
    
    result = product[product['product_id'].isin(valid_products)][['product_id', 'product_name']]
    return result