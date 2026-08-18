import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    all_combos = students.merge(subjects, how='cross')
    
    counts = (
        examinations
        .groupby(['student_id', 'subject_name'])
        .size()
        .rename('attended_exams')
    )
    
    all_combos = all_combos.set_index(['student_id', 'subject_name'])
    all_combos['attended_exams'] = counts
    all_combos['attended_exams'] = all_combos['attended_exams'].fillna(0).astype(int)
    
    result = all_combos.reset_index()
    result = result.sort_values(['student_id', 'subject_name']).reset_index(drop=True)
    
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]