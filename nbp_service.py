import requests

NBP_API_BASE_URL = "http://api.nbp.pl/api"

def get_average_exchange_rate(currency, date):
    response = requests.get(f'{NBP_API_BASE_URL}/exchangerates/rates/a/{currency}/{date}')
    if response.status_code == 200:
        data = response.json()
        result = {"currency": currency, "date": date, "average_exchange_rate": data['rates'][0]['mid']}
    return result, response.status_code

def get_min_max_average(currency, num_days):
    response = requests.get(f'{NBP_API_BASE_URL}/exchangerates/rates/a/{currency}/last/{num_days}')
    if response.status_code == 200:
        data = response.json()
        min_avg = min(rate['mid'] for rate in data['rates'])
        max_avg = max(rate['mid'] for rate in data['rates'])
        result = {"currency": currency, "min_average": min_avg, "max_average": max_avg}
    return result, response.status_code

def get_major_difference(currency, num_days):
    response = requests.get(f'{NBP_API_BASE_URL}/exchangerates/rates/c/{currency}/last/{num_days}')
    if response.status_code == 200:
        data = response.json()
        differences = [rate['ask'] - rate['bid'] for rate in data['rates']]
        major_diff = max(differences)
        major_diff_index = differences.index(major_diff)
        major_diff_date = data['rates'][major_diff_index]['effectiveDate']
        result = {
            "currency": currency,
            "major_difference": major_diff,
            "major_difference_date": major_diff_date
        }
        return result, response.status_code
    return None, response.status_code