from flask import render_template

from app.controllers.controller import ControllerBase


class CalculatorInfoController(ControllerBase):

    @staticmethod
    def get():
        return render_template('calculator_info.html')
