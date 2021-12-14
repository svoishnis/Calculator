import csv
import os
from flask import render_template, request
from werkzeug.utils import secure_filename
from calc.calculator import Calculator
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
        CsvPostLogic.set_operation(f.filename[: -4])
        timestamp = CsvPostLogic.get_time()
        path = os.getcwd() + '/' + CsvPostLogic.get_operation() + ".csv"
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
            calc_list = []
            my_tuple2 = []

            x = CsvPostLogic()

            my_tuple2 = map(x.convert_input_row_into_output_row, data)

            # for value1, value2, result in data:
            #     my_tuple1 = (value1, value2)
            #     calc = Calculator.addition(my_tuple1)
            #     if calc == result:
            #         result = "Pass"
            #     else:
            #         result = "Fail"
            #     data_row = [value1, value2, operation, result, Calculator.get_last_result_value(),
            #                 result]
            #     my_tuple2 = my_tuple2.append(data_row)
            #
            #     # calc_list.append(str(Calculator.get_last_result_value()))

        # asdfasdf = CsvPostLogic()
        # kdksk = asdfasdf.testtest()
        # list_of_tuples = list((kdksk,kdksk,kdksk ))

        return render_template('csv_calc_result.html', success=success,
                               operation=CsvPostLogic.get_operation(), rows=my_tuple2,
                               validation=my_tuple2, timestamp=timestamp)
