# Machine Learning Web Application

A Django web application that provides interfaces for various machine learning algorithms including Polynomial Regression, KNN, Simple Linear Regression, Multiple Linear Regression, and Logistic Regression.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Visit http://127.0.0.1:8000/ in your browser

## Features

- Polynomial Regression
- K-Nearest Neighbors (KNN)
- Simple Linear Regression (SLR)
- Multiple Linear Regression (MLR)
- Logistic Regression

Each algorithm has its own page with:
- Input form for predictions
- Example datasets
- Results display
- Navigation menu 