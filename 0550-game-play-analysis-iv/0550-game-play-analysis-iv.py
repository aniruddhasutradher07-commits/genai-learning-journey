import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login.columns = ['player_id', 'first_login']
    
    merged = activity.merge(first_login, on='player_id')
    merged['next_day'] = merged['first_login'] + pd.Timedelta(days=1)
    
    consecutive = merged[merged['event_date'] == merged['next_day']]
    
    total_players = activity['player_id'].nunique()
    consecutive_players = consecutive['player_id'].nunique()
    
    fraction = round(consecutive_players / total_players, 2)
    
    return pd.DataFrame({'fraction': [fraction]})