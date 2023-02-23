# This program calculates pay based on rate and hours
# Program calculates weekly, monthly, and annual pay

# References:
# program plan


def get_pay():
    print("Enter hourly pay: ")
    pay = float(input())
    return pay


def get_hours():
    print("Enter hours worked per week: ")
    hours = float(input())
    return hours


def calculate_weekly(pay, hours):
    weekly = pay * hours
    return weekly


def calculate_monthly(pay, hours):
    weekly = pay * hours
    monthly = weekly * 4
    return monthly


def calculate_annual(pay, hours):
    weekly = pay * hours
    monthly = weekly * 4
    annual = monthly * 12
    return annual


def display_result(pay, hours, weekly, monthly, annual):
    print("You make $" + str(weekly) + " a week.")
    print("You make $" + str(monthly) + " a month.")
    print("You make $" + str(annual) + " a year")


def main():
    pay = get_pay()
    hours = get_hours()
    weekly = calculate_weekly(pay, hours)
    monthly = calculate_monthly(pay, hours)
    annual = calculate_annual(pay, hours)
    display_result(pay, hours, weekly, monthly, annual)


main()


