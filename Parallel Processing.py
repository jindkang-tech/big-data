import pandas as pd
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

# Function to load data
def load_data(file_path):
    """Load data from a CSV file."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  # Trim whitespace from column names
    return df

# Function to calculate average staying home per week
def calculate_average_staying_home(args):
    """Calculate the average number of people staying at home per week."""
    df, week_column_name = args
    return df.groupby(week_column_name)['Population Staying at Home'].mean()

def main():
    # Paths to your datasets
    file_paths = [
        r"C:\Users\HP\Desktop\ai\New folder\Trips_Full Data.csv",
        r"C:\Users\HP\Desktop\ai\New folder\Trips_by_Distance.csv"
    ]

    # Using ProcessPoolExecutor to load data in parallel
    with ProcessPoolExecutor() as executor:
        dfs = list(executor.map(load_data, file_paths))

    # Adjust the week column names as per your datasets
    week_column_names = ['Week of Date', 'Week']

    # Calculate the average number of people staying at home per week in parallel
    with ProcessPoolExecutor() as executor:
        avg_staying_home_per_week = list(executor.map(calculate_average_staying_home, zip(dfs, week_column_names)))

    # Visualization for the first dataset (df1)
    plt.figure(figsize=(10, 6))  # Adjusting figure size for better readability
    avg_staying_home_per_week[0].plot(kind='bar', color='skyblue')
    plt.title('Average Number of People Staying at Home per Week (df1)')
    plt.xlabel('Week of Date')
    plt.ylabel('Average Population Staying at Home')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Assuming you want to add a similar visualization for the second dataset (df2)
    plt.figure(figsize=(10, 6))  # Adjusting figure size for better readability
    avg_staying_home_per_week[1].plot(kind='bar', color='lightgreen')
    plt.title('Average Number of People Staying at Home per Week (df2)')
    plt.xlabel('Week')
    plt.ylabel('Average Population Staying at Home')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
