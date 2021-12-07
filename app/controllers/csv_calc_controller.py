from app.controllers.controller import ControllerBase
from flask import render_template, request, flash

from calc.calculator import Calculator


class CsvCalcController(ControllerBase):
    @staticmethod
    def get():
        return render_template('csv_calc.html')


