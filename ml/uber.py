import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("uber_price.csv")  # change filename if needed
print("Dataset loaded successfully")
print(df.head())

# Drop missing values
df.dropna(inplace=True)

# Remove negative/zero fare and passenger values
df = df[(df['fare_amount'] > 0) & (df['passenger_count'] > 0)]

# Filter unrealistic coordinates (NYC range)
df = df[(df['pickup_longitude'] > -80) & (df['pickup_longitude'] < -70)]
df = df[(df['dropoff_longitude'] > -80) & (df['dropoff_longitude'] < -70)]
df = df[(df['pickup_latitude'] > 35) & (df['pickup_latitude'] < 45)]
df = df[(df['dropoff_latitude'] > 35) & (df['dropoff_latitude'] < 45)]

# Convert pickup_datetime to datetime format
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')

# Extract time features
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year

# Haversine Distance Function
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c

# Create distance column
df['distance_km'] = haversine_distance(df['pickup_latitude'], df['pickup_longitude'],
                                       df['dropoff_latitude'], df['dropoff_longitude'])

# Remove trips with zero or unrealistic distance
df = df[df['distance_km'] > 0]

# Feature selection
X = df[['passenger_count', 'distance_km', 'hour', 'day', 'month']]
y = df['fare_amount']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features for Linear Regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Linear Regression Model
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

# Random Forest Model
rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Evaluation Function
def evaluate(y_true, y_pred, model_name):
    print(f"\n------ {model_name} ------")
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
    print("R² Score:", r2_score(y_true, y_pred))

evaluate(y_test, y_pred_lr, "Linear Regression")
evaluate(y_test, y_pred_rf, "Random Forest")
