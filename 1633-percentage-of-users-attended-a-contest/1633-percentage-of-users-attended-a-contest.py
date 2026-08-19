import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_users = len(users)

    result = register.groupby("contest_id")["user_id"].count().reset_index()

    result["percentage"] = (result["user_id"] / total_users * 100).round(2)

    result = result.sort_values(
        by=["percentage", "contest_id"],
        ascending=[False, True]
    )

    return result[["contest_id", "percentage"]]