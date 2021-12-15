import os
from flask import render_template, request
from werkzeug.utils import secure_filename
from calc.testesttest import CsvPostLogic
from app.controllers.controller import ControllerBase


class CsvCalcController(ControllerBase):

    @staticmethod
    def get():
        Calculations.clear_history()
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
        calc_list = []
        my_tuple2 = []

        x = CsvPostLogic()

        my_tuple2 = map(x.convert_input_row_into_output_row, data)
        CsvPostLogic.store_output_data(my_tuple2)

        return render_template('csv_calc_result.html', success=success,
                               operation=CsvPostLogic.get_operation(), rows=my_tuple2,
                               timestamp=timestamp, file=path)
