from models import Expense
from storage import load_expenses, save_expenses
from utils import log_action, validate_amount

@log_action
def add_expense(amount, category, note):
  validate_amount(amount)
  
  expense = Expense (amount, category, note)
  
  expenses = load_expenses()
  expenses.append(expense.to_dict())
  
  save_expenses(expenses)
    
@log_action
def get_all_expenses():
  return load_expenses()
  
def filter_by_category(category):
  expenses = load_expenses()
  return (exp for exp in expenses if exp["category"] == category) 
  
def total_expense():
  expenses = load_expenses()
  return sum(exp["amount"] for exp in expenses)


