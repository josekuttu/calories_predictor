from django import forms

class PolynomialRegressionForm(forms.Form):
    duration = forms.FloatField(
        label='Exercise Duration (minutes)',
        min_value=0,
        max_value=120,
        help_text='Enter the duration of your exercise in minutes (0-120)'
    )
    intensity = forms.FloatField(
        label='Exercise Intensity (1-10)',
        min_value=1,
        max_value=10,
        initial=5,
        help_text='Rate your exercise intensity from 1 (light) to 10 (very intense)'
    )

class KNNForm(forms.Form):
    duration = forms.FloatField(
        label='Exercise Duration (minutes)',
        min_value=0,
        max_value=120,
        help_text='Enter the duration of your exercise in minutes (0-120)'
    )
    intensity = forms.FloatField(
        label='Exercise Intensity (1-10)',
        min_value=1,
        max_value=10,
        initial=5,
        help_text='Rate your exercise intensity from 1 (light) to 10 (very intense)'
    )
    weight = forms.FloatField(
        label='Weight (kg)',
        min_value=30,
        max_value=200,
        help_text='Enter your weight in kilograms (30-200)'
    )
    age = forms.IntegerField(
        label='Age (years)',
        min_value=18,
        max_value=100,
        help_text='Enter your age in years (18-100)'
    )

class SimpleLinearRegressionForm(forms.Form):
    duration = forms.FloatField(
        label='Exercise Duration (minutes)',
        min_value=0,
        max_value=120,
        help_text='Enter the duration of your exercise in minutes (0-120)'
    )

class MultipleLinearRegressionForm(forms.Form):
    duration = forms.FloatField(
        label='Exercise Duration (minutes)',
        min_value=0,
        max_value=120,
        help_text='Enter the duration of your exercise in minutes (0-120)'
    )
    intensity = forms.FloatField(
        label='Exercise Intensity (1-10)',
        min_value=1,
        max_value=10,
        initial=5,
        help_text='Rate your exercise intensity from 1 (light) to 10 (very intense)'
    )
    weight = forms.FloatField(
        label='Weight (kg)',
        min_value=30,
        max_value=200,
        help_text='Enter your weight in kilograms (30-200)'
    )
    age = forms.IntegerField(
        label='Age (years)',
        min_value=18,
        max_value=100,
        help_text='Enter your age in years (18-100)'
    )

class LogisticRegressionForm(forms.Form):
    duration = forms.FloatField(
        label='Exercise Duration (minutes)',
        min_value=0,
        max_value=120,
        help_text='Enter the duration of your exercise in minutes (0-120)'
    )
    intensity = forms.FloatField(
        label='Exercise Intensity (1-10)',
        min_value=1,
        max_value=10,
        initial=5,
        help_text='Rate your exercise intensity from 1 (light) to 10 (very intense)'
    )
    weight = forms.FloatField(
        label='Weight (kg)',
        min_value=30,
        max_value=200,
        help_text='Enter your weight in kilograms (30-200)'
    )
    age = forms.IntegerField(
        label='Age (years)',
        min_value=18,
        max_value=100,
        help_text='Enter your age in years (18-100)'
    ) 