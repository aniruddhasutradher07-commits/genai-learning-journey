import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    window_start = pd.Timestamp('2019-06-28')
    window_end = pd.Timestamp('2019-07-27')

    filtered = activity[
        (activity['activity_date'] >= window_start) &
        (activity['activity_date'] <= window_end)
    ]

    result = filtered.groupby('activity_date')['user_id'].nunique().reset_index()
    result.columns = ['day', 'active_users']
    return result