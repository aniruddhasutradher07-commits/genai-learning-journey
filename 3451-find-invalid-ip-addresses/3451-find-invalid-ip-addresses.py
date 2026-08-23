import pandas as pd

def is_invalid_ip(ip: str) -> bool:
    parts = ip.split('.')
    if len(parts) != 4:
        return True
    
    for part in parts:
        if part.isdigit():
            if len(part) > 1 and part[0] == '0':
                return True
            if int(part) > 255:
                return True
    
    return False


def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    invalid_mask = logs['ip'].apply(is_invalid_ip)
    invalid_logs = logs[invalid_mask]
    
    result = (
        invalid_logs.groupby('ip')
        .size()
        .reset_index(name='invalid_count')
    )
    
    return result.sort_values(
        by=['invalid_count', 'ip'],
        ascending=[False, False]
    )