from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense', 'date', 'price')
    ordering = ('date',)
    search_fields = ('expense', 'price')