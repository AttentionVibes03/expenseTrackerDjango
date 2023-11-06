from django.db import models


class Expense(models.Model):
    expense =  models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    
    def price_display(self):
        return "R%s" + self.price
    
    def __str__(self):
        return self.expense
    