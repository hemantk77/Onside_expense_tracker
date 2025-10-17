from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Bills', 'Bills'),
        ('Entertainment', 'Entertainment'),
        ('Shopping', 'Shopping'),
        ('Income', 'Income'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.description} - €{self.amount}"

    class Meta:
        ordering = ['-date'] # Show newest transactions first
