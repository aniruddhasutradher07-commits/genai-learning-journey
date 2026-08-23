import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-z0-9_]+@[a-z]+\.com$'
    result = users[users['email'].str.match(pattern, flags=__import__('re').IGNORECASE)]
    return result.sort_values('user_id')