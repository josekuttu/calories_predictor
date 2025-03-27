import numpy as np
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import (
    PolynomialRegressionForm,
    KNNForm,
    SimpleLinearRegressionForm,
    MultipleLinearRegressionForm,
    LogisticRegressionForm
)
from .models import PredictionResult
import joblib
import os

class HomeView(TemplateView):
    template_name = 'ml_app/home.html'

class PolynomialRegressionView(TemplateView):
    template_name = 'ml_app/polynomial_regression.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PolynomialRegressionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = PolynomialRegressionForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data['duration']
            intensity = form.cleaned_data['intensity']
            
            # Load the model
            model_path = os.path.join('ml_app', 'models', 'polynomial_regression.pkl')
            model = joblib.load(model_path)
            
            # Make prediction with all required features
            X = np.array([[duration, intensity, duration * intensity]])  # Include interaction term
            prediction = model.predict(X)[0]
            
            # Save result
            PredictionResult.objects.create(
                algorithm='polynomial',
                input_data={'duration': duration, 'intensity': intensity},
                prediction={'calories': float(prediction)}
            )
            
            return render(request, self.template_name, {
                'form': form,
                'prediction': prediction
            })
        return render(request, self.template_name, {'form': form})

class KNNView(TemplateView):
    template_name = 'ml_app/knn.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = KNNForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = KNNForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data['duration']
            intensity = form.cleaned_data['intensity']
            weight = form.cleaned_data['weight']
            age = form.cleaned_data['age']
            
            # Load the model
            model_path = os.path.join('ml_app', 'models', 'knn.pkl')
            model = joblib.load(model_path)
            
            # Make prediction
            X = np.array([[duration, intensity, weight, age]])
            prediction = model.predict(X)[0]
            
            # Calculate calories for display
            calories = 0.1 * duration**2 + 5 * duration + 0.5 * intensity * weight + 0.1 * age
            
            # Save result
            PredictionResult.objects.create(
                algorithm='knn',
                input_data={'duration': duration, 'intensity': intensity, 'weight': weight, 'age': age},
                prediction={'calories': float(calories), 'class': int(prediction)}
            )
            
            return render(request, self.template_name, {
                'form': form,
                'prediction': prediction,
                'calories': calories
            })
        return render(request, self.template_name, {'form': form})

class SimpleLinearRegressionView(TemplateView):
    template_name = 'ml_app/simple_linear_regression.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SimpleLinearRegressionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = SimpleLinearRegressionForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data['duration']
            
            # Load the model
            model_path = os.path.join('ml_app', 'models', 'simple_linear_regression.pkl')
            model = joblib.load(model_path)
            
            # Make prediction
            X = np.array([[duration]])
            prediction = model.predict(X)[0]
            
            # Save result
            PredictionResult.objects.create(
                algorithm='slr',
                input_data={'duration': duration},
                prediction={'calories': float(prediction)}
            )
            
            return render(request, self.template_name, {
                'form': form,
                'prediction': prediction
            })
        return render(request, self.template_name, {'form': form})

class MultipleLinearRegressionView(TemplateView):
    template_name = 'ml_app/multiple_linear_regression.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MultipleLinearRegressionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = MultipleLinearRegressionForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data['duration']
            intensity = form.cleaned_data['intensity']
            weight = form.cleaned_data['weight']
            age = form.cleaned_data['age']
            
            # Load the model
            model_path = os.path.join('ml_app', 'models', 'multiple_linear_regression.pkl')
            model = joblib.load(model_path)
            
            # Make prediction
            X = np.array([[duration, intensity, weight, age]])
            prediction = model.predict(X)[0]
            
            # Save result
            PredictionResult.objects.create(
                algorithm='mlr',
                input_data={'duration': duration, 'intensity': intensity, 'weight': weight, 'age': age},
                prediction={'calories': float(prediction)}
            )
            
            return render(request, self.template_name, {
                'form': form,
                'prediction': prediction
            })
        return render(request, self.template_name, {'form': form})

class LogisticRegressionView(TemplateView):
    template_name = 'ml_app/logistic_regression.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LogisticRegressionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = LogisticRegressionForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data['duration']
            intensity = form.cleaned_data['intensity']
            weight = form.cleaned_data['weight']
            age = form.cleaned_data['age']
            
            # Load the model
            model_path = os.path.join('ml_app', 'models', 'logistic_regression.pkl')
            model = joblib.load(model_path)
            
            # Make prediction
            X = np.array([[duration, intensity, weight, age]])
            prediction = model.predict(X)[0]
            probability = model.predict_proba(X)[0][1] * 100  # Convert to percentage for high calorie class
            
            # Save result
            PredictionResult.objects.create(
                algorithm='logistic',
                input_data={'duration': duration, 'intensity': intensity, 'weight': weight, 'age': age},
                prediction={'class': int(prediction), 'probability': float(probability)}
            )
            
            return render(request, self.template_name, {
                'form': form,
                'prediction': prediction,
                'probability': probability
            })
        return render(request, self.template_name, {'form': form}) 