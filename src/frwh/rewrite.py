from datetime import date


def calculate_relative_change_rewrite(
    d1: date, d2: date, obs: dict[date, float]
) -> float:
    current_dt1 = None
    current_val1 = None

    current_dt2 = None
    current_val2 = None

    current_min_dt = None
    current_min_val = None
    for dt, val in obs.items():
        if current_min_dt is None or dt < current_min_dt:
            current_min_dt = dt
            current_min_val = val
        if dt <= d1 and (current_dt1 is None or current_dt1 < dt):
            current_dt1 = dt
            current_val1 = val
        if dt <= d2 and (current_dt2 is None or current_dt2 < dt):
            current_dt2 = dt
            current_val2 = val
    val1 = current_val1 or current_min_val
    val2 = current_val2 or current_min_val
    if val1 is None or val2 is None:
        raise Exception("Unable to find valid index values")
    return val2 / val1
