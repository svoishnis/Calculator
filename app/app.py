"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)


@app.route("/")
def index():
    return IndexController.index()


@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    return CalculatorController.index()
