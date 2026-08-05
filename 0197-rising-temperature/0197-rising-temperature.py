import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.copy()
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather = weather.sort_values('recordDate')

    weather['prevDate'] = weather['recordDate'].shift(1)
    weather['prevTemp'] = weather['temperature'].shift(1)

    mask = (
        (weather['recordDate'] - weather['prevDate'] == pd.Timedelta(days=1)) &
        (weather['temperature'] > weather['prevTemp'])
    )

    result = weather.loc[mask, ['id']]
    return result