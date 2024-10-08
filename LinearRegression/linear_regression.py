from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing

# Load dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Evaluate dataset
print(f"\nDataset Features & Actual Values ____________\n")
print(f"type(X): {type(X)}\n         X[0] = ...")
i = 0
for feature in data.feature_names[0:len(data.feature_names)]:
    print(f"         {feature} = {X[0][i]}")
    i += 1
print(f"\ntype(y): {type(y)}\n         y[0] = ...")
print(f"         Actual = {y[0]}")
print(f"_____________________________________________\n")

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Hypothetical house data for Santa Clara, CA
new_home = [[
    10.0,    # MedInc
    20.0,    # HouseAge
    5.0,     # AveRooms
    3.0,     # AveBedrms
    1500,    # Population
    4.0,     # AveOccup
    37.3541, # Latitude
    -121.9552# Longitude
]]

# Predict the price for the new house
pred_val = model.predict(new_home)

# Evaluate model
print(f"\nHypotehtical Data & Predicted Value(s) ______\n")
print(f"new_home: {type(X)}\n          X[0] = ...")
i = 0
for feature in data.feature_names[0:len(data.feature_names)]:
    print(f"          {feature} = {new_home[0][i]}")
    i += 1
print(f"\npred_val: {type(y)}\n          ... = ${(pred_val[0]*100000):.2f}")
print(f"_______________________________________________\n")