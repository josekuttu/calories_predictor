from django.db import models

class PredictionResult(models.Model):
    ALGORITHM_CHOICES = [
        ('polynomial', 'Polynomial Regression'),
        ('knn', 'K-Nearest Neighbors'),
        ('slr', 'Simple Linear Regression'),
        ('mlr', 'Multiple Linear Regression'),
        ('logistic', 'Logistic Regression'),
    ]

    algorithm = models.CharField(max_length=20, choices=ALGORITHM_CHOICES)
    input_data = models.JSONField()
    prediction = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.algorithm} - {self.created_at}" 