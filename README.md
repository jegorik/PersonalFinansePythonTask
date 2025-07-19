# Personal Finance Python Task

A comprehensive Python application designed for personal finance management and tracking. This project provides essential tools for managing your financial data, creating budgets, tracking expenses, and performing financial analysis.

## 🚀 Features

- **Expense Tracking**: Record and categorize your daily expenses
- **Budget Management**: Create and monitor budgets across different categories
- **Financial Analysis**: Generate reports and insights from your financial data
- **Data Visualization**: Visual charts and graphs for better understanding of spending patterns
- **Import/Export**: Support for various data formats (CSV, JSON, etc.)

## 📋 Requirements

- Python 3.7 or higher
- Required Python packages (see `requirements.txt`)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/jegorik/PersonalFinansePythonTask.git
cd PersonalFinansePythonTask
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the main application:
```bash
python main.py
```

2. Follow the on-screen prompts to:
   - Add new expenses
   - Set up budgets
   - View financial reports
   - Export data

## 📊 Project Structure

```
PersonalFinansePythonTask/
├── main.py                 # Main application entry point
├── src/                    # Source code directory
│   ├── finance/            # Core finance modules
│   ├── utils/              # Utility functions
│   └── data/               # Data handling modules
├── tests/                  # Unit tests
├── data/                   # Sample data files
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 📈 Example Usage

```python
from src.finance import ExpenseTracker, BudgetManager

# Initialize expense tracker
tracker = ExpenseTracker()

# Add an expense
tracker.add_expense("Groceries", 45.67, "Food")

# Create a budget
budget = BudgetManager()
budget.set_monthly_budget("Food", 300.00)

# Generate report
report = tracker.generate_monthly_report()
print(report)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- GitHub: [@jegorik](https://github.com/jegorik)
- Project Link: [https://github.com/jegorik/PersonalFinansePythonTask](https://github.com/jegorik/PersonalFinansePythonTask)

## 🔄 Version History

- **v1.0.0** - Initial release with basic expense tracking functionality
- More versions to come as the project evolves
