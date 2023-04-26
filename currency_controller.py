from flask import Blueprint, jsonify, request
from nbp_service import get_average_exchange_rate, get_min_max_average, get_major_difference
from error_handler import handle_nbp_error

currency_blueprint = Blueprint('currency', __name__)

@currency_blueprint.route('/average_exchange_rate/<string:currency>/<string:date>', methods=['GET'])
def average_exchange_rate(currency, date):
    result, status_code = get_average_exchange_rate(currency, date)
    if status_code == 200:
        return jsonify(result)
    else:
        return handle_nbp_error(status_code)

@currency_blueprint.route('/min_max_average/<string:currency>/<int:num_days>', methods=['GET'])
def min_max_average(currency, num_days):
    result, status_code = get_min_max_average(currency, num_days)
    if status_code == 200:
        return jsonify(result)
    else:
        return handle_nbp_error(status_code)

@currency_blueprint.route('/major_difference/<string:currency>/<int:num_days>', methods=['GET'])
def major_difference(currency, num_days):
    result, status_code = get_major_difference(currency, num_days)
    if status_code == 200:
        return jsonify(result)
    else:
        return handle_nbp_error(status_code)