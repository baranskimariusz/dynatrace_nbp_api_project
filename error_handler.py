from flask import jsonify
from http import HTTPStatus

def handle_nbp_error(status_code):
    if status_code == HTTPStatus.NOT_FOUND:
        message = "The requested data was not found."
    elif status_code == HTTPStatus.BAD_REQUEST:
        message = "Invalid input data."
    else:
        message = "An error occurred while processing your request."
    
    return jsonify({"error": message}), status_code