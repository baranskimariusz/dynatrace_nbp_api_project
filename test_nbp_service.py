import pytest
from nbp_service import get_average_exchange_rate, get_min_max_average, get_major_difference
from http import HTTPStatus

def test_fetch_av_exch_rate():
    result, status_code = get_average_exchange_rate('usd', '2021-04-01')
    assert status_code == HTTPStatus.OK
    assert result['average_exchange_rate'] is not None

def test_get_min_max_average():
    result, status_code = get_min_max_average('usd', 10)
    assert status_code == HTTPStatus.OK
    assert result['min_average'] is not None
    assert result['max_average'] is not None

def test_get_major_difference():
    result, status_code = get_major_difference('usd', 10)
    assert status_code == HTTPStatus.OK
    assert result['major_difference'] is not None
    assert result['major_difference_date'] is not None

def test_invalid_currency_code():
    result, status_code = get_average_exchange_rate('invalid_code', '2021-04-01')
    assert status_code == HTTPStatus.NOT_FOUND
    assert result is None

def test_invalid_date_format():
    result, status_code = get_average_exchange_rate('usd', '2021/04/01')
    assert status_code == HTTPStatus.BAD_REQUEST
    assert result is None

def test_invalid_num_days():
    result, status_code = get_min_max_average('usd', -1)
    assert status_code == HTTPStatus.BAD_REQUEST
    assert result is None