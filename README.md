# Personal Finance Python Task

A comprehensive Python application designed for personal finance management and tracking. This project provides essential tools for managing your financial data, creating budgets, tracking expenses, and performing financial analysis.

## 🚀 Features

- **Expense Tracking**: Record and categorize your daily expenses
- **Income Management**: Track income from various sources (salary, freelance, investments)
- **Transaction Storage**: Persistent data storage using JSON files
- **Financial Analysis**: Generate reports and insights from your financial data
- **Interactive CLI**: User-friendly command-line interface for easy interaction
- **Data Validation**: Built-in validation for transaction data integrity

## 📋 Requirements

- Python 3.7 or higher
- No external dependencies required (uses Python standard library)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/jegorik/PersonalFinansePythonTask.git
cd PersonalFinansePythonTask
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. No additional dependencies to install - the application uses only Python standard library!

## 💻 Usage

1. Run the main application:
```bash
python personal_finance.py
```

2. Follow the on-screen prompts to:
   - **Add**: Add new income or expense transactions
   - **View**: Display all stored transactions
   - **Summary**: Generate financial reports showing total income, expenses, and balance
   - **Exit**: Close the application

### Interactive Menu Options

- `add` - Add a new transaction (income or expense)
- `view` - View all existing transactions
- `summary` - Generate financial summary report
- `exit` - Exit the application

## 📊 Project Structure

```
PersonalFinansePythonTask/
├── personal_finance.py    # Main application with FinanceTracker class
├── transactions.json      # Transaction data storage (auto-generated)
├── task.md               # Original task requirements
├── .gitignore            # Git ignore configuration
└── README.md             # This file
```

## 🧪 Testing

The application includes built-in validation and error handling:

- Input validation for transaction types (income/expense)
- Date format validation (YYYY-MM-DD)
- Numeric amount validation
- JSON file handling with error recovery

To test the application:
```bash
python personal_finance.py
```

## 📈 Example Usage

### Adding Transactions
```
Enter transaction type (income/expense): income
Enter amount: 2500.00
Enter category: salary
Enter date (YYYY-MM-DD): 2024-01-15
Transaction added successfully.
```

### Viewing Summary
```
Total Income: 4000.0
Total Expenses: 600.0
Balance: 3400.0
```

### Sample Transaction Categories
- **Income**: salary, freelance, investment, bonus
- **Expenses**: food, rent, utilities, entertainment, transportation

## 🏗️ Architecture

The application follows object-oriented design principles:

- **Transaction Class**: Represents individual financial transactions
- **FinanceTracker Class**: Manages transaction collection and operations
- **JSON Persistence**: Automatic saving and loading of transaction data
- **Input Validation**: Robust error handling for user inputs

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

## 🎯 Future Enhancements

- Budget management and alerts
- Data visualization with charts and graphs
- Import/Export functionality for CSV files
- Monthly/yearly reporting
- Category-based spending analysis
- Web interface development

---

*Happy budgeting! 💰*