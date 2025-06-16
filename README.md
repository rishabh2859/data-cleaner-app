# Data Cleansing Application

A Python application designed to clean datasets by handling duplicates and missing values.

## Features

- Detects and removes duplicate records while keeping a copy of duplicates
- Identifies missing values in the dataset
- Handles missing values differently based on column type:
  - Numeric columns: replaces nulls with mean value
  - Non-numeric columns: drops rows with null values
- Saves cleaned data and duplicate records as separate files

## Requirements

- Python 3.x
- pandas library
- openpyxl (for Excel file support)
- xlrd (for Excel file support)

## Installation

1. Clone this repository or download the script
2. Install required packages:
   ```bash
   pip install pandas openpyxl xlrd
Usage
Run the script:

bash
python data_cleanser.py
When prompted:

Enter the full path to your dataset file

Enter a name for your dataset (used for output files)

Supported File Formats
CSV (.csv)

Excel (.xlsx)

Output Files
The application generates two output files:

[dataname]_duplicates.csv - Contains all duplicate records found

[dataname]cleaned_data.csv - Contains the cleaned dataset

Example
bash
Enter file path: /path/to/your/dataset.csv
Enter the dataname: customer_data
This will create:

customer_data_duplicates.csv

customer_datacleaned_data.csv

Notes
The application includes random delays to simulate scanning processes

For large datasets, processing may take some time

Original files are not modified - all changes are saved to new files

License
This project is open-source and free to use.
