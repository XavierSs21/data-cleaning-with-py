import pandas as pd

df = pd.read_excel('PAN Number Validation Dataset.xlsx')

# Check if it was correctly read
# print(df.head(10))
print('Total records = ', len(df))

# DATA CLEANING

# Convert to string data type, remove white space and convert to uppercase
df["Pan_Numbers"] = df["Pan_Numbers"].astype('string').str.strip().str.upper()
# print(df.head(10))

# Detect null values and missing values
# print(df[df['Pan_Numbers'] == ''])
# print(df[df['Pan_Numbers'].isna()])

# Replace empty strings with NA values and drop rows with missing PAN numbers
df = df.replace({"Pan_Numbers": ''}, pd.NA).dropna(subset='Pan_Numbers')
print('Total records = ', len(df))

# Count unique values
print('Unique values = ', df["Pan_Numbers"].nunique())

# Remove duplicate values but keep the first occurence
df = df.drop_duplicates(subset='Pan_Numbers', keep='first')
print('Total records = ', len(df))

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
    return any((pan[i] == pan[i+1] for i in range(len(pan)- 1)))
