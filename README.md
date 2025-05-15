# Personal Finance Tracker

## Overview

The Personal Finance Tracker is a simple Python application that helps you manage your personal finances. It allows you to add transactions, view transactions, generate financial summaries, handle missing data gracefully, and save transactions permanently.

## Purpose

The purpose of this project is to provide a basic tool for tracking personal income and expenses. It helps users keep track of their financial activities and provides a summary of their financial status.

## Usage Instructions

### Adding Transactions

To add a transaction, follow these steps:

1. Run the application.
2. Choose the "Add" action from the main menu.
3. Enter the transaction type (income or expense).
4. Enter the amount.
5. Enter the category (e.g., Food, Rent, Salary, Investments).
6. Enter the date in YYYY-MM-DD format.

### Viewing Transactions

To view all stored transactions, follow these steps:

1. Run the application.
2. Choose the "View" action from the main menu.
3. The application will display all stored transactions.

### Generating Financial Summaries

To generate a financial summary, follow these steps:

1. Run the application.
2. Choose the "Summary" action from the main menu.
3. The application will display the total income, total expenses, and balance.

### Handling Missing Data

The application includes error handling for missing data. If required fields are missing or invalid, the application will prompt you to enter the correct information.

### Saving Transactions Permanently

The application saves transactions to a JSON file (`transactions.json`). When you add a new transaction, it is automatically saved to the file. The application also loads existing transactions from the file when it starts.

## Requirements

To run the Personal Finance Tracker, you need the following:

- Python 3.x
- `json` module (included in the Python standard library)
- `os` module (included in the Python standard library)
- `datetime` module (included in the Python standard library)

## Running the Application

To run the application, execute the following command in your terminal:

```bash
python personal_finance.py
```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
