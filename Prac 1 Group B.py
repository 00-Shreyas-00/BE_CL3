# To apply the artificial immune pattern recognition to perform a task of structure damage Classification.

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

# Generate synthetic dataset
X, y = make_classification(n_samples=200, n_features=5, random_state=42)

# Normalize
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize antibodies
num_antibodies = 20
antibodies = X_train[np.random.choice(len(X_train), num_antibodies)]

# Affinity (Euclidean distance)
def affinity(a, b):
    return np.linalg.norm(a - b)

# Classification
def classify(sample):
    distances = [affinity(sample, ab) for ab in antibodies]
    return y_train[np.argmin(distances)]

# Predictions
y_pred = [classify(x) for x in X_test]

print("Accuracy:", accuracy_score(y_test, y_pred))
