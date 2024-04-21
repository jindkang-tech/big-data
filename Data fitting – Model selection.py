import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer

# Load and preprocess dataset
dataset_2 = pd.read_csv(r"C:\Users\HP\Desktop\ai\New folder\Trips_by_Distance.csv")
# Consider sampling if dataset is very large: dataset_2 = dataset_2.sample(frac=0.1)

# Impute missing values (more efficient than dropping if dataset is large)
imputer = SimpleImputer(strategy='median')
X = dataset_2[['Number of Trips 1-3']].values
y = dataset_2['Population Not Staying at Home'].values
X = imputer.fit_transform(X)
y = imputer.transform(y.reshape(-1, 1)).ravel()

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model with fewer trees and use all cores for speed
model = RandomForestRegressor(n_estimators=10, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Model trained successfully with Mean Squared Error:", mse)

