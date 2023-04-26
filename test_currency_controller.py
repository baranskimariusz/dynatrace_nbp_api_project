import pytest
from main import app
from http import HTTPStatus

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_av_exch_rate(client):
    response = client.get('/average_exchange_rate/usd/2021-04-01')
    assert response.status_code == HTTPStatus.OK
    assert response.json['average_exchange_rate'] is not None

def test_min_max_averages(client):
    response = client.get('/min_max_average/usd/10')
    assert response.status_code == HTTPStatus.OK
    assert response.json['min_average'] is not None
    assert response.json['max_average'] is not None

def test_major_rate_difference(client):
    response = client.get('/major_difference/usd/10')
    assert response.status_code == HTTPStatus.OK
    assert response.json['major_difference'] is not None
    assert response.json['major_difference_date'] is not None

def test_invalid_currency_code(client):
    response = client.get('/average_exchange_rate/invalid_code/2021-04-01')
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_invalid_date_format(client):
    response = client.get('/average_exchange_rate/usd/2021/04/01')
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_invalid_num_days(client):
    response = client.get('/min_max_average/usd/-1')
    assert response.status_code == HTTPStatus.BAD_REQUEST