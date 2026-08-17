import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    singles = counts[counts == 1].index
    result = singles.max() if len(singles) > 0 else None
    return pd.DataFrame({ 'num': [result]})