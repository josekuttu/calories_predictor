from django.urls import path
from .views import (
    HomeView,
    PolynomialRegressionView,
    KNNView,
    SimpleLinearRegressionView,
    MultipleLinearRegressionView,
    LogisticRegressionView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('polynomial-regression/', PolynomialRegressionView.as_view(), name='polynomial_regression'),
    path('knn/', KNNView.as_view(), name='knn'),
    path('simple-linear-regression/', SimpleLinearRegressionView.as_view(), name='simple_linear_regression'),
    path('multiple-linear-regression/', MultipleLinearRegressionView.as_view(), name='multiple_linear_regression'),
    path('logistic-regression/', LogisticRegressionView.as_view(), name='logistic_regression'),
] 