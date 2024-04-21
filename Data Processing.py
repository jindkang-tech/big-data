import pandas as pd
import time
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

# Define a function to calculate total trips for a given distance category
def calculate_total_trips(distance_column):
    df_full = pd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_Full Data.csv")  
    return df_full[distance_column].sum()

# List of distance categories
distance_columns = ['Trips <1 Mile', 'Trips 1-3 Miles', 'Trips 3-5 Miles', 'Trips 5-10 Miles',
                    'Trips 10-25 Miles', 'Trips 25-50 Miles', 'Trips 50-100 Miles',
                    'Trips 100-250 Miles', 'Trips 250-500 Miles', 'Trips 500+ Miles']

def main():
    # Sequential processing
    start_time = time.time()
    total_trips_sequential = {column: calculate_total_trips(column) for column in distance_columns}
    end_time = time.time()
    print(f"Sequential Processing Time: {end_time - start_time} seconds")

    # Parallel processing
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(calculate_total_trips, distance_columns))
    total_trips_parallel = dict(zip(distance_columns, results))
    end_time = time.time()
    print(f"Parallel Processing Time: {end_time - start_time} seconds")

    # Visualization
    plt.figure(figsize=(12, 6))
    plt.bar(total_trips_sequential.keys(), total_trips_sequential.values(), color='blue', alpha=0.6, label='Total Trips')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Number of Trips')
    plt.title('Total Number of Trips by Distance Category')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
