from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50, default='tablet')
    stock = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=10)
    updated_at = models.DateTimeField(auto_now=True)

    def is_low_stock(self):
        return self.stock <= self.low_stock_threshold

    def __str__(self):
        return f"{self.name} ({self.stock} {self.unit})"

# Create your models here.
