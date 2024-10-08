<h1>Learning & Implementation Guides for ML</h1>
<h2>Getting Started</h2>

```bash
git init
git remote add origin https://github.com/yammei/model-implementations.git
git pull origin main
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

<h2>Index</h2>
• <a href="#1">Linear Regression</a><br>
• <a href="#2">Logistic Regression</a><br>
• <a href="#3">Decision Tree</a><br>
• <a href="#4">Random Forest</a><br>

<h2 id="1">1. Linear Regression</h2>

<h3>Visualized & Explained</h3>

<img src="https://github.com/yammei/model-implementations/blob/main/LinearRegression/linear_regression_visualized.png" alt=""/>

<h3>linear_regression.py Terminal Output</h3>

```bash
Dataset Features & Actual Values ____________

type(X): <class 'numpy.ndarray'>
         X[0] = ...
         MedInc = 8.3252
         HouseAge = 41.0
         AveRooms = 6.984126984126984
         AveBedrms = 1.0238095238095237
         Population = 322.0
         AveOccup = 2.5555555555555554
         Latitude = 37.88
         Longitude = -122.23

type(y): <class 'numpy.ndarray'>
         y[0] = ...
         Actual = 4.526
_____________________________________________


Hypotehtical Data & Predicted Value(s) ______

new_home: <class 'numpy.ndarray'>
          X[0] = ...
          MedInc = 10.0
          HouseAge = 20.0
          AveRooms = 5.0
          AveBedrms = 3.0
          Population = 1500
          AveOccup = 4.0
          Latitude = 37.3541
          Longitude = -121.9552

pred_val: <class 'numpy.ndarray'>
          ... = $658560.81
_______________________________________________
```

<h2 id="2">2. Logistic Regression</h2>

<h3>Visualized & Explained</h3>

<img src="https://github.com/yammei/model-implementations/blob/main/LogisticRegression/logistic_regression_visualized.png" alt=""/>

<h3>logistic_regression.py Terminal Output</h3>

```bash
Confusion Matrix:
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]

Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       1.00      1.00      1.00         9
           2       1.00      1.00      1.00        11

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30
```

<h2 id="3">3. Decision Tree</h2>

<h3>Visualized & Explained</h3>
<i>Coming Soon...</i>

<h3>decision_tree.py Terminal Output</h3>

```bash
...
```

<h2 id="4">4. Random Forest</h2>

<h3>Visualized & Explained</h3>
<i>Coming Soon...</i>

<h3>random_forest.py Terminal Output</h3>

```bash
Dataset Features & Actual Values ____________

type(X): <class 'numpy.ndarray'>
         X[0] = ...
         mean radius = 17.99
         mean texture = 10.38
         mean perimeter = 122.8
         mean area = 1001.0
         mean smoothness = 0.1184
         mean compactness = 0.2776
         mean concavity = 0.3001
         mean concave points = 0.1471
         mean symmetry = 0.2419
         mean fractal dimension = 0.07871
         radius error = 1.095
         texture error = 0.9053
         perimeter error = 8.589
         area error = 153.4
         smoothness error = 0.006399
         compactness error = 0.04904
         concavity error = 0.05373
         concave points error = 0.01587
         symmetry error = 0.03003
         fractal dimension error = 0.006193
         worst radius = 25.38
         worst texture = 17.33
         worst perimeter = 184.6
         worst area = 2019.0
         worst smoothness = 0.1622
         worst compactness = 0.6656
         worst concavity = 0.7119
         worst concave points = 0.2654
         worst symmetry = 0.4601
         worst fractal dimension = 0.1189

type(y): <class 'numpy.ndarray'>
         y[0] = ...
         Actual = 0
_____________________________________________

Confusion Matrix:
[[40  3]
 [ 1 70]]

Classification Report:
              precision    recall  f1-score   support

           0       0.98      0.93      0.95        43
           1       0.96      0.99      0.97        71

    accuracy                           0.96       114
   macro avg       0.97      0.96      0.96       114
weighted avg       0.97      0.96      0.96       114
```
