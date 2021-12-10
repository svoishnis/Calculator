"""A simple flask web app"""
from flask import Flask

from app.controllers.csv_calc_controller import CsvCalcController
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()


def index():
    return IndexController.index()


@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    return CalculatorController.index()


@app.route("/csv_calc", methods=['POST'])
def csv_calc_post():
    return CsvCalcController.post()


@app.route("/csv_calc", methods=['GET', 'POST'])
def csv_calc_get():
    return CsvCalcController.get()


def csv_calc():
    return CsvCalcController.index()


if __name__ == "__main__":
    app.run(debug=True)
