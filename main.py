import defines as d
import methods as m
import pandas as pd

def main():
    data = []
    data = m.read(d.filename, d.good_columns, d.column_names)

    stops = pd.DataFrame(data, columns = d.good_columns)
    print('These are the colors of stoped vehicles: \n{}' .format(stops['color'].value_counts()) )
    print('These are the arrest types: \n{}' .format(stops['arrest_type'].value_counts()))

    # do some parsing of the strings to float
    stops['longitude'] = stops['longitude'].apply(m.parse_float)
    stops['latitude'] = stops['latitude'].apply(m.parse_float)

if __name__ == '__main__':
    main()
