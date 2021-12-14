import csv
import os
from flask import render_template, request
from werkzeug.utils import secure_filename
from calc.testesttest import CsvPostLogic
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
        operation = f.filename[: -4]
        path = os.getcwd() + '/' + operation + ".csv"
        # df = pandas.read_csv(path,
        #                      header=0,
        #                      names=['Value_1', 'Value_2', 'Result'])
        # dateframe_rows = df.iterrows()
        #
        # list_of_tuples = list(map(lambda x,y,z: (x,y,z), dateframe_rows))
        with open(f.filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            data = [tuple(line) for line in reader]

        # asdfasdf = CsvPostLogic()
        # kdksk = asdfasdf.testtest()
        # list_of_tuples = list((kdksk,kdksk,kdksk ))

        return render_template('csv_calc_result.html', success=success, operation=operation, rows=data)
