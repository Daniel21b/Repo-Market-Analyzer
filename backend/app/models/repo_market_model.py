class RepoMarketModel:
    def __init__(self, start_date, end_date, bank, loan_amount):
        self.start_date = start_date
        self.end_date = end_date
        self.bank = bank
        self.loan_amount = loan_amount

    def to_dict(self):
        return {
            'start_date': self.start_date,
            'end_date': self.end_date,
            'bank': self.bank,
            'loan_amount': self.loan_amount
        }
