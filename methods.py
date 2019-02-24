import ijson
import numpy as np

'''
with open(filename, 'r') as f:
    # meta is top level key, which contains view inside, wich contains items inside.
    # item indicates that I want to extract each individual item inside meta.view.columns.
    # ijson.items returns a generator
    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)
print(columns[0])

'''
def read(filename, good_columns, column_names):
    data = []
    with open(filename, 'r') as f:
        objects = ijson.items(f, 'data.item')
        for row in objects:
            selected_row = []
            for item in good_columns:
                selected_row.append(row[column_names.index(item)])
            data.append(selected_row)
            if(len(data)==15000):
                return data

def parse_float(data):
    try:
        data = np.float(data)
    except Exception:
        data = 0
    return data
