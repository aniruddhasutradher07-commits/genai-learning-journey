import pandas as pd

def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    grouped = prompts.groupby('user_id')['tokens'].agg(
        prompt_count='count',
        avg_tokens_exact='mean'
    ).reset_index()
    grouped = grouped[grouped['prompt_count'] >= 3]
    merged = prompts.merge(grouped[['user_id', 'avg_tokens_exact']], on='user_id', how='inner')
    has_above_avg = (
        merged[merged['tokens'] > merged['avg_tokens_exact']]['user_id']
        .unique()
    )

    result = grouped[grouped['user_id'].isin(has_above_avg)].copy()
    result['avg_tokens'] = result['avg_tokens_exact'].round(2)
    result = result[['user_id', 'prompt_count', 'avg_tokens']]

    return result.sort_values(
        by=['avg_tokens', 'user_id'],
        ascending=[False, True]
    )