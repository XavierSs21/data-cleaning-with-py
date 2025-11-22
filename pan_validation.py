import pandas as pd

df = pd.read_excel('PAN Number Validation Dataset.xlsx')

# Check if it was correctly read
# print(df.head(10))
print('Total records = ', len(df))

# DATA CLEANING

# Convert to String data type, remove white space and convert to upper
df["Pan_Numbers"] = df["Pan_Numbers"].astype('string').str.strip().str.upper()
# print(df.head(10))

# Detect null values and non-available values
# print(df[df['Pan_Numbers'] == ''])
# print(df[df['Pan_Numbers'].isna()])

# Replace null values to NA values
df = df.replace({"Pan_Numbers": ''}, pd.NA).dropna(subset='Pan_Numbers')
print('Total records = ', len(df))

# Count unique values
print('Unique values = ', df["Pan_Numbers"].nunique())

# Remove duplicates values but keeps the first record that appears
df = df.drop_duplicates(subset='Pan_Numbers', keep='first')
print('Total records = ', len(df))

# VALIDATION