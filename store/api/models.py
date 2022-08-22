from django.db import models
from datetime import datetime

from simple_history.models import HistoricalRecords

class Product(models.Model):
      title = models.CharField(max_length=255)
      price = models.DecimalField(max_digits = 5, decimal_places = 2)
      history = HistoricalRecords()
      def __str__(self):
          return self.title
      


class Order(models.Model):
      date = models.DateTimeField()
      products = models.ManyToManyField(Product)
      history = HistoricalRecords()