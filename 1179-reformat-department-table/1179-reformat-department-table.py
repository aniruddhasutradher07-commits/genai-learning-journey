import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    department['month'] = department['month'] + '_Revenue'
    result = department.pivot(index='id', columns='month', values='revenue')

    month_order = [f'{m}_Revenue' for m in
                   ['Jan','Feb','Mar','Apr','May','Jun',
                   'Jul','Aug','Sep','Oct','Nov','Dec']]
    result = result.reindex(columns=month_order).reset_index()
    result.columns.name = None
    return result               