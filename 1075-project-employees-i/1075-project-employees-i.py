import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee, on='employee_id')
    result = merged.groupby('project_id')['experience_years'].mean().round(2).reset_index()
    result.columns = ['project_id', 'average_years']
    return result