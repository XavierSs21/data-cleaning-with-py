import pandas as pd
import re

df = pd.read_excel('PAN Number Validation Dataset.xlsx')

# Check if it was correctly read
# print(df.head(10))
# print('Total records = ', len(df))
total_records = len(df)

# DATA CLEANING

# Convert to string data type, remove white space and convert to uppercase
df["Pan_Numbers"] = df["Pan_Numbers"].astype('string').str.strip().str.upper()
# print(df.head(10))

# Detect null values and missing values
# print(df[df['Pan_Numbers'] == ''])
# print(df[df['Pan_Numbers'].isna()])

# Replace empty strings with NA values and drop rows with missing PAN numbers
df = df.replace({"Pan_Numbers": ''}, pd.NA).dropna(subset='Pan_Numbers')
# print('Total records = ', len(df))

# Count unique values
# print('Unique values = ', df["Pan_Numbers"].nunique())

# Remove duplicate values but keep the first occurence
df = df.drop_duplicates(subset='Pan_Numbers', keep='first')
# print('Total records = ', len(df))

# VALIDATION

def has_adjacent_repitition(pan):
    """Check if a PAN number contains adjacent repeated characters.
    
    Args:
        pan (str): The PAN number string to validate.
    
    Returns:
        bool: True if consecutive duplicates exist, False otherwise.
    
    Example:
        >>> has_adjacent_repitition("AABCD1234F")
        True
    """
    return any((pan[i] == pan[i+1] for i in range(len(pan) - 1)))

def is_sequential(pan):
    """Check if all characters in a PAN number are sequential.
    
    Verifies whether consecutive characters follow a sequential pattern in 
    ASCII order (e.g., 'ABC', '123', 'XYZ').
    
    Args:
        pan (str): The PAN number string to validate.
    
    Returns:
        bool: True if all characters are in sequential order, False otherwise.
    
    Example:
        >>> is_sequential("ABC")
        True
        >>> is_sequential("XYZ123")
        False
        >>> is_sequential("ABCDE1234F")
        False
    """
    return all(ord(pan[i + 1]) - ord(pan[i]) == 1 for i in range(len(pan) - 1))

def is_valid_pan(pan):
    """Validate if a PAN number meets all required criteria.
    
    A valid PAN number must satisfy the following conditions:
    - Exactly 10 characters long
    - Format: 5 letters + 4 digits + 1 letter (e.g., ABCDE1234F)
    - No adjacent repeated characters
    - No sequential characters
    
    Args:
        pan (str): The PAN number string to validate.
    
    Returns:
        bool: True if the PAN number is valid, False otherwise.
    
    Example:
        >>> is_valid_pan("ABCDE1234F")
        True
        >>> is_valid_pan("AABCD1234F")
        False
        >>> is_valid_pan("ABC1234567")
        False
    """
    if len(pan) != 10:
        return False
    
    if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
        return False
    
    if has_adjacent_repitition(pan):
        return False
    
    if is_sequential(pan):
        return False
    
    return True

# Add status column to DataFrame based on PAN validarion rules 
df["Status"] = df["Pan_Numbers"].apply(lambda x: "Valid" if is_valid_pan(x) else "Invalid")
# print(df.head(10))

# Calculate validation statistics
valid_pan_numbers = (df['Status'] == 'Valid').sum()
invalid_pan_numbers = (df['Status'] == 'Invalid').sum()
missing_pan_numbers = total_records - (valid_pan_numbers + invalid_pan_numbers)

# Create summary DataFrame with validation counts
df_summary = pd.DataFrame({"Total Processed Records": [total_records],
                           "Total Valid Count": [valid_pan_numbers],
                           "Total Invalid Count": [invalid_pan_numbers],
                           "Total Missing Count": [missing_pan_numbers]})
# Filter valid records
df_valid = df[df['Status'] == 'Valid']

# Export the results to Excel with separate sheets for data and summary
with pd.ExcelWriter("PAN Number Validated.xlsx") as writer:
    df_valid.to_excel(writer, sheet_name="Valid PAN Numbers", index=False)
    df.to_excel(writer, sheet_name="PAN Validations", index=False)
    df_summary.to_excel(writer, sheet_name="Summary PAN Validations", index=False)