
# Vehicle Data Generator

The Vehicle Data Generator is a Python script that generates synthetic vehicle data in CSV format. It uses the Faker library to create random car-related information such as car names, years, selling prices, present prices, kilometers driven, fuel types, seller types, transmission details, and owner information. This tool is useful for creating sample datasets for testing, analysis, and development purposes.

## Usage

1. Clone the repository.
2. Customize the `vehicle_schema.yaml` file to define the data fields you want to generate.
3. Run `VehicleDataGenerator.py` to generate CSV files with synthetic vehicle data.
4. CSV files will be stored in the `vehicle_data_output/` directory.

## Schema Configuration

Modify the `vehicle_schema.yaml` file to define the fields and data types for the generated vehicle data. Each field includes a name and type (string, int, or float).

## Requirements

- Python 3.x
- Faker library (install using `pip install faker`)
- PyYAML library (install using `pip install pyyaml`)
