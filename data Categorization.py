import pandas as pd

# Load the datasets
df1 = pd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_Full Data.csv")
df2 = pd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_by_Distance.csv")

# Function to categorize trip distances
def categorize_trip_distance(row):
    if row['Trips <1 Mile'] + row['Trips 1-3 Miles'] > 0:
        return 'Short'
    elif row['Trips 3-5 Miles'] + row['Trips 5-10 Miles'] > 0:
        return 'Medium'
    else:
        return 'Long'

# Apply the categorization function to each row
df1['Trip Category'] = df1.apply(categorize_trip_distance, axis=1)
df2['Trip Category'] = df2.apply(categorize_trip_distance, axis=1)

# Function to categorize based on the population staying at home
def categorize_stay_at_home(row):
    total_population = row['Population Staying at Home'] + row['People Not Staying at Home']
    if total_population == 0:  # Avoid division by zero
        return 'Unknown'
    stay_at_home_ratio = row['Population Staying at Home'] / total_population
    if stay_at_home_ratio > 0.5:
        return 'High Stay at Home'
    elif 0.2 <= stay_at_home_ratio <= 0.5:
        return 'Moderate Stay at Home'
    else:
        return 'Low Stay at Home'

# Apply the stay at home categorization function
df1['Stay at Home Category'] = df1.apply(categorize_stay_at_home, axis=1)
df2['Stay at Home Category'] = df2.apply(categorize_stay_at_home, axis=1)

# Convert 'Date' column to datetime and categorize as Weekend or Weekday
for df in [df1, df2]:
    df['Date'] = pd.to_datetime(df['Date'])
    df['Day Type'] = df['Date'].apply(lambda x: 'Weekend' if x.weekday() >= 5 else 'Weekday')

# Save the categorized dataframes back to new CSV files
df1.to_csv(r"C:\Users\HP\Desktop\ai\New folder\Categorized_Trips_Full_Data.csv", index=False)
df2.to_csv(r"C:\Users\HP\Desktop\ai\New folder\Categorized_Trips_by_Distance.csv", index=False)

print("Data categorization completed.")
