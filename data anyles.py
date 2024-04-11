import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_Full Data.csv")
# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])
# Print column names to verify
print(df.columns)
# Fill missing values if necessary
df.ffill(inplace=True)  # Forward fill for simplicity
# Fill missing values if necessary

# Ensure numeric columns are of the correct data type
numeric_cols = ['Population Staying at Home', 'People Not Staying at Home', 'Trips', 'Trips <1 Mile']  # Corrected column names
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Summary statistics
print(df.describe())

# Distribution of 'Trips'
sns.histplot(df['Trips'])
plt.title('Distribution of Trips')
plt.show()
# Time series plot for 'Population Staying at Home'
df.set_index('Date')['Population Staying at Home'].plot()
plt.title('Population Staying at Home Over Time')
plt.show()
# Assuming you have a column 'Pandemic Period' indicating before and during pandemic
# Add 'Pandemic Period' column to DataFrame
df['Pandemic Period'] = df['Date'].apply(lambda x: 'During Pandemic' if x >= pd.Timestamp('2020-03-11') else 'Before Pandemic')
# Compare mean number of trips before and during the pandemic
mean_trips = df.groupby('Pandemic Period')['Trips'].mean()
print(mean_trips)
# Correlation between 'Population Staying at Home' and 'Number of Trips <1'
correlation = df[['Population Staying at Home', 'Trips <1 Mile']].corr()  # Corrected column name
print(correlation)
# Scatter plot for correlation analysis
sns.scatterplot(data=df, x='Population Staying at Home', y='Trips <1 Mile')  # Corrected column name
plt.title('Correlation between Population Staying at Home and Trips <1 Mile')
plt.show()
