import pandas as pd
import numpy as np

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged = prices.merge(units_sold, on='product_id', how='left')

    mask = (merged['purchase_date'] >= merged['start_date']) & \
           (merged['purchase_date'] <= merged['end_date'])

    mask = mask | merged['purchase_date'].isna()

    merged = merged[mask].copy()
    merged['revenue'] = merged['price'] * merged['units'].fillna(0)

    grouped = merged.groupby('product_id').agg(
        total_revenue=('revenue', 'sum'),
        total_units=('units', 'sum')
    ).reset_index()

    grouped['total_units'] = grouped['total_units'].fillna(0)

    def round_half_up(x, decimals=2):
        factor = 10 ** decimals
        return np.floor(x * factor + 0.5) / factor

    grouped['average_price'] = np.where(
        grouped['total_units'] > 0,
        round_half_up(grouped['total_revenue'] / grouped['total_units']),
        0
    )           
    
    return grouped[['product_id', 'average_price']]