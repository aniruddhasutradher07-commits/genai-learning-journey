import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    active = borrowing_records[borrowing_records['return_date'].isna()]
    borrower_counts = (
        active.groupby('book_id')
        .size()
        .reset_index(name='current_borrowers')
    )
    merged = library_books.merge(borrower_counts, on='book_id', how='inner')

    result = merged[merged['total_copies'] == merged['current_borrowers']]

    result = result[['book_id', 'title', 'author', 'genre', 'publication_year', 'current_borrowers']]

    return result.sort_values(
        by=['current_borrowers', 'title'],
        ascending=[False, True]
    )