import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_regression, make_classification
import joblib
import os

def create_models_directory():
    if not os.path.exists('ml_app/models'):
        os.makedirs('ml_app/models')

def train_polynomial_regression():
    # Generate sample data
    X = np.random.rand(100, 1) * 10
    y = 3 * X**2 + 2 * X + 1 + np.random.randn(100, 1) * 0.5
    
    # Create polynomial features
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    
    # Train model
    model = LinearRegression()
    model.fit(X_poly, y)
    
    # Save model
    joblib.dump(model, 'ml_app/models/polynomial_regression.pkl')
    joblib.dump(poly, 'ml_app/models/polynomial_features.pkl')

def train_knn():
    # Generate sample data
    X, y = make_classification(n_samples=100, n_features=4, n_classes=2)
    
    # Train model
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X, y)
    
    # Save model
    joblib.dump(model, 'ml_app/models/knn.pkl')

def train_simple_linear_regression():
    # Generate sample data
    X, y = make_regression(n_samples=100, n_features=1)
    
    # Train model
    model = LinearRegression()
    model.fit(X, y)
    
    # Save model
    joblib.dump(model, 'ml_app/models/simple_linear_regression.pkl')

def train_multiple_linear_regression():
    # Generate sample data
    X, y = make_regression(n_samples=100, n_features=4)
    
    # Train model
    model = LinearRegression()
    model.fit(X, y)
    
    # Save model
    joblib.dump(model, 'ml_app/models/multiple_linear_regression.pkl')

def train_logistic_regression():
    # Generate sample data
    X, y = make_classification(n_samples=100, n_features=4, n_classes=2)
    
    # Train model
    model = LogisticRegression()
    model.fit(X, y)
    
    # Save model
    joblib.dump(model, 'ml_app/models/logistic_regression.pkl')

if __name__ == '__main__':
    create_models_directory()
    train_polynomial_regression()
    train_knn()
    train_simple_linear_regression()
    train_multiple_linear_regression()
    train_logistic_regression()
    print("All models have been trained and saved successfully!") 