from datetime import date

from frwh.legacy import calculate_relative_change


def test_calculate_relative_change_flat_extrapolation_to_the_right():
    d = {
        date(2023, 1, 1): 101.0,
        date(2023, 2, 1): 103.0,
        date(2023, 3, 1): 102.0,
    }
    actual_relchange = calculate_relative_change(
        d1=date(2023, 2, 5), d2=date(2023, 3, 2), obs=d
    )
    assert actual_relchange == 102.0 / 103.0


def test_calculate_relative_change_flat_extrapolation_to_the_left():
    d = {
        date(2023, 1, 1): 101.0,
        date(2023, 2, 1): 103.0,
        date(2023, 3, 1): 102.0,
    }
    actual_relchange = calculate_relative_change(
        d1=date(2022, 12, 1), d2=date(2023, 3, 2), obs=d
    )
    assert actual_relchange == 102.0 / 101.0
