from datetime import date

import pandas as pd


def calculate_relative_change(d1: date, d2: date, obs: dict[date, float]) -> float:
    s = pd.Series(obs)
    s2 = pd.Series({d1: pd.NaT, d2: pd.NaT})
    s = s.combine_first(s2).sort_index().ffill().bfill()
    return s[d2] / s[d1]
