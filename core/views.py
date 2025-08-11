from django.shortcuts import render

def home(request):
    return render(request, "core/home.html", {})

def dashboard(request):
    return render(request, "core/dashboard.html")

def add_expense(request):
    if request.method == "POST":
        expense = request.POST.get("expense")
        price = request.POST.get("price")
        date = request.POST.get("date")
        
        # Here you would typically save the expense to the database
        # For example:
        # Expense.objects.create(expense=expense, price=price, date=date)
        
        return render(request, "core/dashboard.html", {"message": "Expense added successfully!"})
    
    return render(request, "core/add_expense.html")