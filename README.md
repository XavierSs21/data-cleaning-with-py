# PAN Number Validation Project

A Python-based data cleaning and validation tool for Indian PAN (Permanent Account Number) numbers using pandas and regex.

## Overview

This project performs comprehensive validation and cleaning of PAN number datasets, ensuring data quality through multiple validation rules and generating organized Excel reports with clean and dirty data separation.

## Features

- **Data Cleaning**: Removes duplicates, handles missing values, and standardizes format
- **PAN Validation**: Implements strict validation rules including:
  - Length validation (must be 10 characters)
  - Format validation (5 letters + 4 digits + 1 letter)
  - Adjacent character repetition detection
  - Sequential character detection
- **Excel Report Generation**: Exports results to multiple sheets:
  - Valid PAN Numbers (clean data)
  - All PAN Validations (complete dataset with status)
  - Summary statistics

## Technologies Used

- Python 3.x
- pandas
- openpyxl (for Excel operations)
- re (regular expressions)

## Installation
```bash
pip install pandas openpyxl
```

## Usage

Place your PAN dataset as `PAN Number Validation Dataset.xlsx` in the project directory and run the script:
```bash
python pan_validation.py
```

The output file `PAN Number Validated.xlsx` will contain three sheets:
- **Valid PAN Numbers**: Only validated PAN numbers
- **PAN Validations**: Complete dataset with validation status
- **Summary PAN Validations**: Statistics summary

## Validation Rules

A valid PAN number must meet all of the following criteria:

1. **Length**: Exactly 10 characters
2. **Format**: `[A-Z]{5}[0-9]{4}[A-Z]` (e.g., ABCDE1234F)
3. **No Adjacent Repetition**: No consecutive duplicate characters (e.g., AA, 11)
4. **No Sequential Characters**: Characters should not follow ASCII sequential order (e.g., ABC, 123)

## Example
```python
# Valid PAN
is_valid_pan("ABCDE1234F")  # True

# Invalid PANs
is_valid_pan("AABCD1234F")  # False - adjacent repetition
is_valid_pan("ABC1234567")  # False - wrong format
is_valid_pan("ABCDE12345")  # False - wrong format
```

## Project Structure
```
.
├── pan_validation.py
├── PAN Number Validation Dataset.xlsx
└── PAN Number Validated.xlsx (generated)
```

## Author

Xavier Sotomayor Saldívar

GitHub: [@XavierSs21](https://github.com/XavierSs21)  
LinkedIn: [xavier-sotomayor21](https://www.linkedin.com/in/xavier-sotomayor21)

## Acknowledgments

Project inspired by techTFQ's Data Cleaning tutorial series.
