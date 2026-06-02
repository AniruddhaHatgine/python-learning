from datetime import datetime

class Expense:
    def __init__(self, amount, category, note):
        self.amount=amount
        self.category=amount                          #down section also amount,category there so that and this should link so self is used.
        self.note=note
        self.date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "date": self.date
        }
    