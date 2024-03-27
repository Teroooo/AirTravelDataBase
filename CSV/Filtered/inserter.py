import csv

csv_file = 'Airline.csv'  # Replace with the actual name of your CSV file
table_name = 'AIRLINE'   # Replace with the actual name of your table

insert_template = 'INSERT INTO {} VALUES '

with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row if it exists

    for row in csvreader:
        values = ', '.join(f"'{value}'" for value in row)
        insert_statement = insert_template.format(table_name, values)
        print(insert_statement)
