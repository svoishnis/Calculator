import os
from flask import render_template, request
from werkzeug.utils import secure_filename
from calc.csvreader.csvfunctions import CsvPostLogic
from app.controllers.controller import ControllerBase


class CsvCalcController(ControllerBase):

    @staticmethod
    def get():
        return render_template('csv_calc.html')

    @staticmethod
    def post():
        f = request.files['filename']
        f.save(secure_filename(f.filename))
        success = 'File Uploaded Successfully'
        CsvPostLogic.set_operation(f.filename[: -4])
        timestamp = CsvPostLogic.get_time()
        path = os.getcwd() + '/' + CsvPostLogic.get_operation() + ".csv"

        data = CsvPostLogic.read_file(f)
        x = CsvPostLogic()
        y = CsvPostLogic()

        my_tuple2 = map(x.convert_input_row_into_output_row, data)
        output_data = list(map(y.convert_input_row_into_output_row, data))
        CsvPostLogic.store_output_data(output_data)

        return render_template('csv_calc_result.html', success=success,
                               operation=CsvPostLogic.get_operation(), rows=my_tuple2,
                               timestamp=timestamp, file=path)
