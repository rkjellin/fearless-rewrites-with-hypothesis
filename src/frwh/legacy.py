from datetime import date

import pandas as pd


def calculate_relative_change(d1: date, d2: date, obs: dict[date, float]) -> float:
    s = pd.Series(obs)
    s[d1] = pd.NaT
    s[d2] = pd.NaT
    s = s.sort_index().ffill().bfill()
    return s[d2] / s[d1]
