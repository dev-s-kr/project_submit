from datetime import datetime, timedelta

DELIVERY_DAYS = 2
# test

def _is_holiday(day: datetime) -> bool:
    return day.weekday() > 5


def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1

    return current_date


def test_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)


def test_eta_2024_12_31() -> None:
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)


def test_eta_2024_2_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)


def test_eta_2023_2_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)
