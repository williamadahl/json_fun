import ijson

filename = "traffic_violations.json"

with open(filename, 'r') as f:
    # meta is top level key, which contains view inside, wich contains items inside.
    # item indicates that I want to extract each individual item inside meta.view.columns.
    # ijson.items returns a generator
    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)
    print(columns[0])
