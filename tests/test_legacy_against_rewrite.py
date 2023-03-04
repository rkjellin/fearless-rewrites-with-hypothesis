from dataclasses import dataclass
from datetime import date

import hypothesis
import hypothesis.strategies as st

from frwh.legacy import calculate_relative_change
from frwh.rewrite import calculate_relative_change_rewrite


@st.composite
def observations(
    draw: st.DrawFn,
    min_size: int | None = None,
    max_size: int | None = None,
) -> st.SearchStrategy[dict[date, float]]:
    dates = draw(
        st.lists(
            st.dates(min_value=date(1999, 1, 1), max_value=date(2023, 3, 3)),
            min_size=min_size,
            max_size=max_size,
            unique=True,
        )
    )
    values = draw(
        st.lists(
            st.floats(
                min_value=0,
                exclude_min=True,
                allow_nan=False,
                allow_infinity=False,
            ),
            min_size=len(dates),
            max_size=len(dates),
        )
    )
    return dict(zip(dates, values))


@hypothesis.given(d1=st.dates(), d2=st.dates(), obs=observations(min_size=1))
def test_legacy_against_rewrite(d1: date, d2: date, obs: dict[date, float]):
    legacy_result = calculate_relative_change(d1, d2, obs)
    rewrite_result = calculate_relative_change_rewrite(d1, d2, obs)
    assert legacy_result == rewrite_result
