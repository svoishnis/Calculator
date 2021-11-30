import csv
import os.path
import pandas as pandas

from calc.calculator import Calculator

filename = os.path.abspath('addition.csv')

"""with open(filename) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Header Row {", ".join(row)}')
            line_count += 1
        print(f'\t input {row["value_1"]}, {row["value_2"]} equate to {row["result"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')

with open('result_log.csv', mode='w') as result_log:
    header = []
    result_writer = csv.writer(result_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    result_writer.writerow(['testing', 'next'])
    result_writer.writerow(['value_1', 'test'])
"""

df = pandas.read_csv(filename,
                     header=0,
                     names=['Value_1', 'Value_2', 'Result'])

dateframe_rows = df.iterrows()
# y= list(map(lambda dataframe_row: (dataframe_row[1].Value_1, y[1].Value_2), dateframe_rows))

def parseDataFrameRow(row):
    mTuple = row[1]
    Value_1 = mTuple.Value_1
    Value_2 = mTuple.Value_2
    Result = mTuple.Result
    return (Value_1, Value_2, float(Result))

def parseTupleforAddition(mTuple):
  Calculator.add_numbers(mTuple[0:2])
  return (Calculator.get_last_result_value(), mTuple[2])

def compareSumsToResults(mTuple):



list_of_tuples = list(map(parseDataFrameRow, dateframe_rows))
list_of_sums = list(map(parseTupleforAddition, list_of_tuples))

print("test")
for i, j in df.iteritems():
    my_tuple = df.at[i]

    print(Calculator.get_last_result_value())
    print()
    """df['calcresult'] = Calculator.get_last_result_value()"""
    """Calculator.add_numbers(i, j)
    print(Calculator.get_last_result_value())
    print('Result')"""
print(df)



"""print(df)"""
df.to_csv('result_log2.csv')
