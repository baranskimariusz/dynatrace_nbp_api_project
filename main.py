from flask import Flask
from currency_controller import currency_blueprint

app = Flask(__name__)
app.register_blueprint(currency_blueprint)

if __name__ == '__main__':
    app.run(debug=True)