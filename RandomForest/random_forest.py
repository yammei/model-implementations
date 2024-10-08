# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load the breast cancer dataset
cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions
y_pred = rf_model.predict(X_test)

################################################################################################

# Evaluate dataset
print(f"\nDataset Features & Actual Values ____________\n")
print(f"type(X): {type(X)}\n         X[0] = ...")
i = 0
for feature in cancer.feature_names[0:len(cancer.feature_names)]:
    print(f"         {feature} = {X[0][i]}")
    i += 1
print(f"\ntype(y): {type(y)}\n         y[0] = ...")
print(f"         Actual = {y[0]}")
print(f"_____________________________________________\n")

# Evaluate the model
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(f"Confusion Matrix: True (+): {tp}")
print(f"                  True (-): {tn}")
print(f"                  False (+): {fp}")
print(f"                  False (-): {fn}")
print(f"_____________________________________________\n")
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print(f"Accuracy Score:", accuracy_score(y_test, y_pred), "\n")
