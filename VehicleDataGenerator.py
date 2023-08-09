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
                        record[field_name] = fake.word()
                    elif field_type == 'int':
                        record[field_name] = fake.random_int(min=2010, max=2022)
                    elif field_type == 'float':
                        record[field_name] = round(random.uniform(10000, 30000), 2)

                writer.writerow(record)

if __name__ == '__main__':
    num_files = 10
    rows_per_file = 100
    schema_file = 'vehicle_schema.yaml'
    output_directory = 'vehicle_data_output'  # Use a descriptive name

    with open(schema_file, 'r') as f:
        schema = yaml.safe_load(f)

    generate_csv_files(schema, output_directory, num_files, rows_per_file)
    print(f"{num_files} CSV files generated successfully, each with {rows_per_file} rows.")
