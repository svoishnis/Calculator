"""A simple flask web app"""

from flask import Flask, send_file

from app.controllers.aaa import AAAController
from app.controllers.calculator_info import CalculatorInfoController
from app.controllers.csv_calc_controller import CsvCalcController
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.ooo import OOOController
from app.controllers.topic import TopicController
from calc.testesttest import CsvPostLogic

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


@app.route('/return-files/')
def return_files():
    CsvPostLogic.write_to_file()
    try:
        return send_file('/home/myuser/result.csv',
                         attachment_filename='test.csv')
    except Exception as e:
        return str(e)


@app.route("/ooo", methods=['GET'])
def ooo_get():
    return OOOController.get()


@app.route("/calculator_info", methods=['GET'])
def calculator_info_get():
    return CalculatorInfoController.get()


@app.route("/topic", methods=['GET'])
def topic_get():
    return TopicController.get()


@app.route("/aaa", methods=['GET'])
def aaa_get():
    return AAAController.get()


@app.route("/api/data", methods=['GET'])
def data():
    return {'data': [user.to_dict() for user in User.query]}


if __name__ == "__main__":
    app.run(debug=True)
