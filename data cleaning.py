
import pandas as pd

# Load the datasets
df1 = pd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_Full Data.csv")
df2 = pd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_by_Distance.csv")

# Standardizing column names for merging or comparison
# Mapping similar columns from df1 to df2's naming convention
column_mapping = {
    'Trips <1 Mile': 'Number of Trips <1',
    'Trips 1-3 Miles': 'Number of Trips 1-3',
    'Trips 3-5 Miles': 'Number of Trips 3-5',
    'Trips 5-10 Miles': 'Number of Trips 5-10',
    'Trips 10-25 Miles': 'Number of Trips 10-25',
    'Trips 25-50 Miles': 'Number of Trips 25-50',
    'Trips 50-100 Miles': 'Number of Trips 50-100',
    'Trips 100-250 Miles': 'Number of Trips 100-250',
    'Trips 250-500 Miles': 'Number of Trips 250-500',
    'Trips 500+ Miles': 'Number of Trips >=500',
    'Trips': 'Number of Trips'
}
df1.rename(columns=column_mapping, inplace=True)

# Handling missing values by filling with zero
df1.fillna(0, inplace=True)
df2.fillna(0, inplace=True)

# Removing duplicates
df1.drop_duplicates(inplace=True)
df2.drop_duplicates(inplace=True)

# Converting 'Date' columns to datetime format
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

# Filtering out irrelevant data (example: keeping only trips less than 25 miles)
# Assuming we're interested in short trips for df1
columns_of_interest = ['Date', 'Number of Trips <1', 'Number of Trips 1-3', 'Number of Trips 3-5', 'Number of Trips 5-10', 'Number of Trips 10-25']
df1_filtered = df1[columns_of_interest]

# For df2, let's assume we're interested in analyzing data based on 'County Name'
# Ensure 'County Name' exists in df2 columns, then filter
if 'County Name' in df2.columns:
    df2_filtered = df2[['Date', 'County Name', 'Number of Trips', 'Population Staying at Home']]

# Save the cleaned and filtered dataframes back to new CSV files
df1_filtered.to_csv(r"C:\Users\HP\Desktop\ai\New folder\Cleaned_Trips_Full_Data.csv", index=False)
df2_filtered.to_csv(r"C:\Users\HP\Desktop\ai\New folder\Cleaned_Trips_by_Distance.csv", index=False)

print("Data cleaning and filtering completed.")
