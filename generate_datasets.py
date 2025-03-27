import numpy as np
import pandas as pd
import os

def create_datasets_directory():
    if not os.path.exists('ml_app/datasets'):
        os.makedirs('ml_app/datasets')

def generate_polynomial_dataset():
    # Generate polynomial data for calories burned based on exercise duration
    # More realistic polynomial relationship between duration and calories
    duration = np.random.rand(100, 1) * 120  # Duration in minutes (0-120)
    calories = 0.1 * duration**2 + 5 * duration + 50 + np.random.randn(100, 1) * 10
    
    # Create DataFrame
    df = pd.DataFrame({
        'Duration': duration.flatten(),
        'Calories': calories.flatten()
    })
    
    # Save to CSV
    df.to_csv('ml_app/datasets/polynomial_data.csv', index=False)
    
    # Save example data
    example_data = pd.DataFrame({
        'Duration': [30, 45, 60],
        'Calories': [0.1 * 30**2 + 5 * 30 + 50,
                   0.1 * 45**2 + 5 * 45 + 50,
                   0.1 * 60**2 + 5 * 60 + 50]
    })
    example_data.to_csv('ml_app/datasets/polynomial_examples.csv', index=False)

def generate_knn_dataset():
    # Generate classification data for high/low calorie burn
    # Features: Duration, Intensity, Weight, Age
    n_samples = 100
    duration = np.random.rand(n_samples) * 120  # Duration in minutes
    intensity = np.random.rand(n_samples) * 10  # Intensity level (1-10)
    weight = np.random.rand(n_samples) * 50 + 50  # Weight in kg
    age = np.random.rand(n_samples) * 40 + 20  # Age in years
    
    # Calculate calories (simplified formula)
    calories = 0.1 * duration**2 + 5 * duration + 0.5 * intensity * weight + 0.1 * age
    
    # Classify as high (1) or low (0) calorie burn
    y = (calories > np.median(calories)).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Duration': duration,
        'Intensity': intensity,
        'Weight': weight,
        'Age': age,
        'Calories': calories,
        'Class': y
    })
    
    # Save to CSV
    df.to_csv('ml_app/datasets/knn_data.csv', index=False)
    
    # Save example data
    example_data = pd.DataFrame({
        'Duration': [30, 45, 60],
        'Intensity': [7, 8, 9],
        'Weight': [70, 75, 80],
        'Age': [30, 35, 40],
        'Calories': [0.1 * 30**2 + 5 * 30 + 0.5 * 7 * 70 + 0.1 * 30,
                   0.1 * 45**2 + 5 * 45 + 0.5 * 8 * 75 + 0.1 * 35,
                   0.1 * 60**2 + 5 * 60 + 0.5 * 9 * 80 + 0.1 * 40],
        'Class': [0, 1, 1]
    })
    example_data.to_csv('ml_app/datasets/knn_examples.csv', index=False)

def generate_simple_linear_dataset():
    # Generate linear data for calories burned based on duration
    duration = np.random.rand(100, 1) * 120  # Duration in minutes
    calories = 8 * duration + 50 + np.random.randn(100, 1) * 10
    
    # Create DataFrame
    df = pd.DataFrame({
        'Duration': duration.flatten(),
        'Calories': calories.flatten()
    })
    
    # Save to CSV
    df.to_csv('ml_app/datasets/simple_linear_data.csv', index=False)
    
    # Save example data
    example_data = pd.DataFrame({
        'Duration': [30, 45, 60],
        'Calories': [8 * 30 + 50,
                   8 * 45 + 50,
                   8 * 60 + 50]
    })
    example_data.to_csv('ml_app/datasets/simple_linear_examples.csv', index=False)

def generate_multiple_linear_dataset():
    # Generate multiple linear data for calories burned
    # Features: Duration, Intensity, Weight, Age
    n_samples = 100
    duration = np.random.rand(n_samples) * 120  # Duration in minutes
    intensity = np.random.rand(n_samples) * 10  # Intensity level (1-10)
    weight = np.random.rand(n_samples) * 50 + 50  # Weight in kg
    age = np.random.rand(n_samples) * 40 + 20  # Age in years
    
    # Calculate calories (simplified formula)
    calories = 8 * duration + 5 * intensity + 0.5 * weight + 0.1 * age + 50 + np.random.randn(n_samples) * 10
    
    # Create DataFrame
    df = pd.DataFrame({
        'Duration': duration,
        'Intensity': intensity,
        'Weight': weight,
        'Age': age,
        'Calories': calories
    })
    
    # Save to CSV
    df.to_csv('ml_app/datasets/multiple_linear_data.csv', index=False)
    
    # Save example data
    example_data = pd.DataFrame({
        'Duration': [30, 45, 60],
        'Intensity': [7, 8, 9],
        'Weight': [70, 75, 80],
        'Age': [30, 35, 40],
        'Calories': [8 * 30 + 5 * 7 + 0.5 * 70 + 0.1 * 30 + 50,
                   8 * 45 + 5 * 8 + 0.5 * 75 + 0.1 * 35 + 50,
                   8 * 60 + 5 * 9 + 0.5 * 80 + 0.1 * 40 + 50]
    })
    example_data.to_csv('ml_app/datasets/multiple_linear_examples.csv', index=False)

def generate_logistic_dataset():
    # Generate classification data for high/low calorie burn
    # Features: Duration, Intensity, Weight, Age
    n_samples = 100
    duration = np.random.rand(n_samples) * 120  # Duration in minutes
    intensity = np.random.rand(n_samples) * 10  # Intensity level (1-10)
    weight = np.random.rand(n_samples) * 50 + 50  # Weight in kg
    age = np.random.rand(n_samples) * 40 + 20  # Age in years
    
    # Calculate calories (simplified formula)
    calories = 0.1 * duration**2 + 5 * duration + 0.5 * intensity * weight + 0.1 * age
    
    # Classify as high (1) or low (0) calorie burn
    y = (calories > np.median(calories)).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Duration': duration,
        'Intensity': intensity,
        'Weight': weight,
        'Age': age,
        'Calories': calories,
        'Class': y
    })
    
    # Save to CSV
    df.to_csv('ml_app/datasets/logistic_data.csv', index=False)
    
    # Save example data
    example_data = pd.DataFrame({
        'Duration': [30, 45, 60],
        'Intensity': [7, 8, 9],
        'Weight': [70, 75, 80],
        'Age': [30, 35, 40],
        'Calories': [0.1 * 30**2 + 5 * 30 + 0.5 * 7 * 70 + 0.1 * 30,
                   0.1 * 45**2 + 5 * 45 + 0.5 * 8 * 75 + 0.1 * 35,
                   0.1 * 60**2 + 5 * 60 + 0.5 * 9 * 80 + 0.1 * 40],
        'Class': [0, 1, 1]
    })
    example_data.to_csv('ml_app/datasets/logistic_examples.csv', index=False)

if __name__ == '__main__':
    create_datasets_directory()
    generate_polynomial_dataset()
    generate_knn_dataset()
    generate_simple_linear_dataset()
    generate_multiple_linear_dataset()
    generate_logistic_dataset()
    print("All datasets have been generated successfully!") 