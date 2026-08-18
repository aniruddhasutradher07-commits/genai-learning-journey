import pandas as pd
import numpy as np

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    df = stadium[stadium['people'] >= 100].reset_index(drop=True).copy()
    
    if df.empty:
        return df[['id', 'visit_date', 'people']]
    
    df['grp'] = df['id'].values - np.arange(1, len(df) + 1)
    
    df['grp_size'] = df.groupby('grp')['id'].transform('size')
    
    result = df[df['grp_size'] >= 3][['id', 'visit_date', 'people']]
    
    result = result.sort_values('visit_date').reset_index(drop=True)
    
    return result