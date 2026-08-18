import pandas as pd
import numpy as np

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    df = queries.copy()
    df['ratio'] = df['rating'] / df['position']
    df['is_poor'] = (df['rating'] < 3).astype(int)
    
    grouped = df.groupby('query_name').agg(
        quality=('ratio', 'mean'),
        poor_query_percentage=('is_poor', 'mean')
    ).reset_index()
    
    grouped['poor_query_percentage'] = grouped['poor_query_percentage'] * 100
    
  
    def round_half_up(x, decimals=2):
        factor = 10 ** decimals
        return np.floor(x * factor + 0.5) / factor
    
    grouped['quality'] = round_half_up(grouped['quality'])
    grouped['poor_query_percentage'] = round_half_up(grouped['poor_query_percentage'])
    
    return grouped