import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    totals = rides.groupby('user_id')['distance'].sum().reset_index(name='travelled_distance')
    
    result = users.merge(totals, left_on='id', right_on='user_id', how='left')
    result['travelled_distance'] = result['travelled_distance'].fillna(0).astype(int)

    result = result.sort_values(
        by=['travelled_distance', 'name'],
        ascending=[False, True]
    ).reset_index(drop=True)

    return result[['name', 'travelled_distance']]