import os

from app.controllers.controller import ControllerBase
from flask import render_template, request, flash, app

from calc.calculator import Calculator


class CsvCalcController(ControllerBase):
    @staticmethod
    def get():
        return render_template('csv_calc.html')

    @staticmethod
    def post():
        file = request.files['file']
        # file.save(os.path.join(app.config['csv_input'], file))
        # if request.form['filename'] == '' or request.form['filename'] == 'null':
        #     error = 'You must enter a value for value 1 and or value 2'
        # else:
        #     flash('Successfully uploaded')
        #     # get the values out of the form
        #     # value1 = request.form['filename']
        #     # make the tuple
        #     # my_tuple = (value1, value2)
        #     # # this will call the correct operation
        #     # getattr(Calculator, operation)(my_tuple)
        #     # result = str(Calculator.get_last_result_value())
        #     return render_template('result.html')
        return render_template('csv_calc_result.html')

