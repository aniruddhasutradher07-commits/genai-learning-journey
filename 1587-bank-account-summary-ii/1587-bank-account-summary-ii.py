import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    balance = transactions.groupby("account")["amount"].sum().reset_index()

    result = users.merge(balance, on="account")

    result = result[result["amount"] > 10000]

    return result[["name", "amount"]].rename(columns={"amount": "balance"})