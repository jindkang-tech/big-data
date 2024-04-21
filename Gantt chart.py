import pandas as pd
import dask.dataframe as dd
import plotly.express as px

# Explicitly define data types for columns in the large dataset
dtypes = {
    'County Name': 'object',
    'Number of Trips': 'float64',
    'Number of Trips 1-3': 'float64',
    'Number of Trips 10-25': 'float64',
    'Number of Trips 100-250': 'float64',
    'Number of Trips 25-50': 'float64',
    'Number of Trips 250-500': 'float64',
    'Number of Trips 3-5': 'float64',
    'Number of Trips 5-10': 'float64',
    'Number of Trips 50-100': 'float64',
    'Number of Trips <1': 'float64',
    'Number of Trips >=500': 'float64',
    'Population Not Staying at Home': 'float64',
    'Population Staying at Home': 'float64',
    'State Postal Code': 'object'
}

# Load datasets
df_small = pd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_Full Data.csv")
ddf_large = dd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_by_Distance.csv", dtype=dtypes)

# Handling missing values for the small dataset
df_small['Trips'] = pd.to_numeric(df_small['Trips'], errors='coerce')
df_small['Trips'] = df_small['Trips'].fillna(df_small['Trips'].mean())

# Handling missing values for the large dataset
# Assuming 'Number of Trips' is the column with non-numeric values
ddf_large['Number of Trips'] = ddf_large['Number of Trips'].apply(pd.to_numeric, errors='coerce', meta=('Number of Trips', 'float64'))
ddf_large['Number of Trips'] = ddf_large['Number of Trips'].fillna(0)  # Fill missing values with 0

# Now compute the Dask DataFrame after all transformations
ddf_large = ddf_large.compute()

# Removing duplicates
df_small.drop_duplicates(inplace=True)
ddf_large = ddf_large.drop_duplicates()

# Checking and converting data types
df_small['Date'] = pd.to_datetime(df_small['Date'])
ddf_large['Date'] = pd.to_datetime(ddf_large['Date'])

# Checking for outliers in 'Trips' column as an example for the small dataset
trips_mean = df_small['Trips'].mean()
trips_std = df_small['Trips'].std()
outliers = df_small[(df_small['Trips'] > trips_mean + 3 * trips_std) | (df_small['Trips'] < trips_mean - 3 * trips_std)]
print("Outliers count in small dataset:", len(outliers))

# For the large dataset, ensure you're working with the computed DataFrame
trips_mean_large = ddf_large['Number of Trips'].mean()
trips_std_large = ddf_large['Number of Trips'].std()
outliers_large = ddf_large[(ddf_large['Number of Trips'] > trips_mean_large + 3 * trips_std_large) | (ddf_large['Number of Trips'] < trips_mean_large - 3 * trips_std_large)]
print("Outliers count in large dataset:", len(outliers_large))

# Create a Gantt chart for the small dataset
fig = px.timeline(df_small, x_start="Date", x_end="Date", y="Level", color="Trips")
fig.update_yaxes(autorange="reversed")  # Invert the y-axis order
fig.show()

# Create a Gantt chart for the large dataset
fig_large = px.timeline(ddf_large, x_start="Date", x_end="Date", y="Level", color="Number of Trips")
fig_large.update_yaxes(autorange="reversed")  # Invert the y-axis order
fig_large.show()
