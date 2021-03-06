# coding: utf-8
import csv
from pathlib import Path

"""
Part 1: Automate the Calculations.
    Automate the calculations for the loan portfolio summaries.
"""

loan_costs = [500, 600, 200, 1000, 450]

#   Print the number of loans from the list
number_of_loans = len(loan_costs)
print(f"Number of loans: {number_of_loans}.\n")


#   Print the total value of the loans
sum_of_loans = sum(loan_costs)
print(f"Sum of loan: {sum_of_loans}.\n")

#   Print the average loan amount
average_loan_price = sum_of_loans / number_of_loans
print(f"The average loan price: {average_loan_price}.\n")


"""
Part 2: Analyze Loan Data.
    Analyze the loan to determine the investment evaluation.
"""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#   Extract the Future Value and the Remaining Months
face_value = loan.get("future_value")
month_remaining = loan.get("remaining_months")

print(f"The future value: {face_value}.\n")
print(f"The remaining months: {month_remaining}.\n")

#   Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

present_value = face_value / (1 + (.20/12)) ** month_remaining

#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

if present_value >= face_value:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")


"""
Part 3: Perform Financial Calculations.
    Perform financial calculations using functions.
"""


new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#   Define a new function that will be used to calculate present value.


def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / \
        (1 + annual_discount_rate / 12) ** remaining_months
    return present_value


#   Calculate the present value of the new loan given below.
annual_discount_rate = .20
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate
)

print(f"The present value of the loan is: {present_value:.02f}\n")


"""
Part 4: Conditionally filter lists of loans.
    Looping to iterate through a series of loans and select only the inexpensive loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#   New list: `inexpensive_loans`
inexpensive_loans = []

#   Looping through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan.get('loan_price') <= 500:
        inexpensive_loans.append(loan)

print(inexpensive_loans)


"""
Part 5: Save the results.
    Output this list of inexpensive loans to a csv file
"""

#   Output header
header = ["loan_price", "remaining_months",
          "repayment_interval", "future_value"]

#   Output file path
output_path = Path("inexpensive_loans.csv")

print("\n")
with open(output_path, 'w', newline='') as csvwriter:
    csvwriter = csv.writer(csvwriter)

    csvwriter.writerow(header)

    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
