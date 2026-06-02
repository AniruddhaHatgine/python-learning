import json
import os

FILE_PATH = "data/expenses.json"

def load_expenses():
    if not os.path.exists(FILE_PATH):
        return[]
    
    with open(FILE_PATH,"r") as f:
        return json.load(f)
    
def save_expenses(expenses):
    with open(FILE_PATH,"w") as f:
        json.dump(expenses, f,indent=4)

