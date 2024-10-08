import csv

def read_csv(name):
    rows = []
    
    with open(f'{name}.csv',mode='r',newline='',encoding='utf-8') as csv_file:
        csv_file_read = csv.reader(csv_file)
        next(csv_file_read)
        for row in csv_file_read:
            if row != None:
                rows.append(row)
    return rows