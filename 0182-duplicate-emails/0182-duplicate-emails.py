import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    counts = person['email'].value_counts()
    duplicated = counts[counts > 1].index
    result = pd.DataFrame({'Email': duplicated})
    return result
    