import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates()

    result = (
        activities.sort_values('product')
        .groupby('sell_date')['product']
        .agg(num_sold='count', products=lambda x: ','.join(x))
        .reset_index()
        .sort_values('sell_date')
    )

    return result