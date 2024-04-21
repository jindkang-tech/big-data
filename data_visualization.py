import pandas as pd
import matplotlib.pyplot as plt
from data_preprocessing import load_and_clean_data

def visualize_travel_data(trips_by_distance_path, trips_full_data_path):
    """
    Visualize the number of participants of travelers by distance-trips and discuss the outcomes.
    
    Parameters:
    trips_by_distance_path (str): The file path for the Trips_by_Distance.csv file.
    trips_full_data_path (str): The file path for the Trips_Full Data.csv file.
    
    Returns:
    None: This function will generate plots.
    """
    # Load and clean data
    trips_by_distance, trips_full_data = load_and_clean_data(trips_by_distance_path, trips_full_data_path)

# Debugging line to print column names
    print(trips_by_distance.columns)
    # Visualize the number of trips by distance from the Trips_by_Distance dataset
    plt.figure(figsize=(10, 6))
    trips_by_distance.groupby('Number of Trips <1')['Number of Trips'].sum().plot(kind='bar')
    plt.title('Total Number of Trips by Distance')
    plt.xlabel('Distance')
    plt.ylabel('Number of Trips')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Visualize the number of travelers by distance from the Trips_Full Data dataset
    plt.figure(figsize=(10, 6))
    trips_full_data.groupby('Distance')['Number of People'].sum().plot(kind='bar')
    plt.title('Number of Travelers by Distance')
    plt.xlabel('Distance')
    plt.ylabel('Number of Travelers')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Define file paths
    trips_by_distance_path = "F:\\Download\\Trips_by_Distance.csv"
    trips_full_data_path = "F:\\Download\\Trips_Full Data.csv"
    
    # Call the visualization function
    visualize_travel_data(trips_by_distance_path, trips_full_data_path)
