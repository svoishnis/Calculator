from werkzeug.utils import secure_filename
from app.controllers.controller import ControllerBase
from flask import render_template, request, flash, app

from calc.calculator import Calculator


class CsvCalcController(ControllerBase):

    @staticmethod
    def get():
        return render_template('csv_calc.html')

    @staticmethod
    def post():
        f = request.files['filename']
        f.save(secure_filename(f.filename))
        success = 'File Uploaded Successfully'
        operation = f.filename[: -4]

        # return render_template('csv_calc_result.html', success=success, operation=operation)
        return render_template('csv_calc_result.html')
