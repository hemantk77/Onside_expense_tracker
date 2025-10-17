from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Sum
from .models import Transaction
from decimal import Decimal
from .forms import TransactionForm

# --- Authentication Views ---

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# --- Core App Views ---

@login_required
def dashboard_view(request):
    transactions = Transaction.objects.filter(user=request.user)
    
    # Calculate totals
    total_income = transactions.filter(category='Income').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
    total_expenses = transactions.exclude(category='Income').aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
    net_balance = total_income - total_expenses
    
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_balance': net_balance
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def transaction_create_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'tracker/transaction_form.html', {'form': form})

@login_required
def transaction_update_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'tracker/transaction_form.html', {'form': form, 'transaction': transaction})

@login_required
def transaction_delete_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('dashboard')
    return render(request, 'tracker/transaction_confirm_delete.html', {'transaction': transaction})