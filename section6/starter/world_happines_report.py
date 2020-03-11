# a country name to statistics dictionary
data = {}
# a tuple that will contain column names of statistics
columns = None

with open('data.csv', 'r') as data_file:
    lines = data_file.readlines()
    columns = tuple(lines[0].strip().split(',')[1:])
    for row in lines[1:]:
        row_data = row.strip().split(',')
        data['row']
print(columns)
