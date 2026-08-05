import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', inplace=True)
    duplicates = person[person.duplicated(subset='email', keep='first')].index
    person.drop(duplicates, inplace=True)
    