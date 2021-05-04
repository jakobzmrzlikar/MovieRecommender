import csv
import json

csv_file = 'IMDb_movies.csv'
json_file = 'IMDb_movies.json'

data_list = []

with open(csv_file, 'r') as in_file:
    reader = csv.reader(in_file)
    fields = next(reader)
    for row in reader:
        data = {}
        for field, value in zip(fields, row):
            data[field] = value
        data_list.append(data)

with open(json_file, 'w') as out_file:
    out_file.write(json.dumps(data_list, indent=2, ensure_ascii=False))
