import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id',suffixes=('_emp', '_dept'))
    max_salary = merged.groupby('departmentId')['salary'].transform('max')
    result = merged[merged['salary'] == max_salary]
    result = result.rename(columns={'name_dept': 'Department', 'name_emp': 'Employee', 'salary': 'Salary'})
    return result[['Department', 'Employee','Salary']]