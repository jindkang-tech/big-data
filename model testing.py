import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def test_model(trips_by_distance_path, trips_full_data_path):
    # Load datasets
    trips_by_distance = pd.read_csv(trips_by_distance_path, parse_dates=['Date'])
    trips_full_data = pd.read_csv(trips_full_data_path, parse_dates=['Date'])

    # Merge datasets on 'Date' column
    merged_data = pd.merge(trips_by_distance, trips_full_data, on='Date')
    
    # Check if merged data is empty
    if merged_data.empty:
        raise ValueError("Merged data is empty. Check the merge keys and data.")
    
    # Remove rows with NaN values in the target column
    merged_data = merged_data.dropna(subset=['Population Not Staying at Home'])

    # Select features and target variable
    X = merged_data[['Trips 1-3 Miles']]  # Adjust as needed
    y = merged_data['Population Not Staying at Home']  # Adjust as needed

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict the values for the test set
    predictions = model.predict(X_test)
    
    # Calculate and print the performance metrics
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Model Performance Metrics:\nMSE: {mse}\nR^2 Score: {r2}")

if __name__ == "__main__":
    # Define file paths
    data1 = r"C:\Users\HP\Desktop\ai\New folder\Trips_Full Data.csv"
    data2 = r"C:\Users\HP\Desktop\ai\New folder\Trips_by_Distance.csv"
    
    # Train and test the model
    test_model(data1, data2)
