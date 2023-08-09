import csv
import os
import yaml
from faker import Faker
import random

def generate_csv_files(schema, output_directory, num_files, rows_per_file):
    os.makedirs(output_directory, exist_ok=True)

    fake = Faker()

    for i in range(1, num_files + 1):
        filename = os.path.join(output_directory, f'vehicle_data_{i}.csv')

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[field['name'] for field in schema])
            writer.writeheader()

            for j in range(rows_per_file):
                record = {}
                for field in schema:
                    field_name = field['name']
                    field_type = field['type']

                    if field_type == 'string':
                        if field_name == 'Car_Name':
                            record[field_name] = fake.word()
                        elif field_name == 'Fuel_Type':
                            record[field_name] = fake.random_element(elements=('Petrol', 'Diesel', 'CNG'))
                        elif field_name == 'Seller_Type':
                            record[field_name] = fake.random_element(elements=('Dealer', 'Individual'))
                        elif field_name == 'Transmission':
                            record[field_name] = fake.random_element(elements=('Manual', 'Automatic'))
                        elif field_name == 'Car_Type':
                            record[field_name] = fake.random_element(elements=('Sedan', 'SUV', 'Hatchback'))
                        elif field_name == 'Location':
                            record[field_name] = fake.city()
                        else:
                            record[field_name] = fake.word()
                    elif field_type == 'int':
                        if field_name == 'Year':
                            record[field_name] = fake.random_int(min=2000, max=2022)
                        elif field_name == 'Owner':
                            record[field_name] = fake.random_int(min=0, max=3)
                        else:
                            record[field_name] = fake.random_int(min=0, max=1000)
                    elif field_type == 'float':
                        if field_name == 'Selling_Price' or field_name == 'Present_Price':
                            record[field_name] = round(random.uniform(1, 20), 2)
                        else:
                            record[field_name] = round(random.uniform(1000, 50000), 2)

                writer.writerow(record)

if __name__ == '__main__':
    num_files = 10
    rows_per_file = 100
    schema_file = 'vehicle_schema.yaml'
    output_directory = 'vehicle_data_output'

    with open(schema_file, 'r') as f:
        schema = yaml.safe_load(f)

    generate_csv_files(schema, output_directory, num_files, rows_per_file)
    print(f"{num_files} CSV files generated successfully, each with {rows_per_file} rows.")
