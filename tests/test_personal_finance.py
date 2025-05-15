import unittest
from personal_finance import Transaction, FinanceTracker

class TestTransaction(unittest.TestCase):
    def test_to_dict(self):
        transaction = Transaction('income', 1000.0, 'salary', '2025-01-01')
        expected_dict = {
            'type': 'income',
            'amount': 1000.0,
            'category': 'salary',
            'date': '2025-01-01'
        }
        self.assertEqual(transaction.to_dict(), expected_dict)

class TestFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = FinanceTracker()
        self.tracker.transactions = []

    def test_add_transaction(self):
        transaction = Transaction('income', 1000.0, 'salary', '2025-01-01')
        self.tracker.transactions.append(transaction)
        self.assertIn(transaction, self.tracker.transactions)

    def test_view_transactions(self):
        transaction = Transaction('income', 1000.0, 'salary', '2025-01-01')
        self.tracker.transactions.append(transaction)
        self.assertEqual(len(self.tracker.transactions), 1)

    def test_generate_summary(self):
        self.tracker.transactions.append(Transaction('income', 2000.0, 'salary', '2025-01-01'))
        self.tracker.transactions.append(Transaction('expense', 500.0, 'food', '2025-01-02'))
        summary = self.tracker.generate_summary()
        self.assertEqual(summary['total_income'], 2000.0)
        self.assertEqual(summary['total_expenses'], 500.0)
        self.assertEqual(summary['balance'], 1500.0)

if __name__ == '__main__':
    unittest.main()
