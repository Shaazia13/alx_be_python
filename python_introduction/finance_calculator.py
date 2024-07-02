# finance_calculator.py

# Prompt user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
# Assume annual interest rate (fixed)
annual_interest_rate = 0.05

# Calculate projected savings after one year
projected_savings = monthly_savings * 12 * (1 + annual_interest_rate)
# Print results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
