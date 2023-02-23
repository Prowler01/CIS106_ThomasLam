# This program calculates pay based on rate and hours
# Program calculates weekly, monthly, and annual pay

# References:
# program plan


def get_rate():
    print("Rate: ")
    rate = float(input())
    return rate


def get_hours():
    print("Hours: ")
    hours = float(input())
    return hours


def calculate_weekly(rate, hours):
    weekly = rate * hours
    return weekly


def calculate_monthly(rate, hours):
    weekly = rate * hours
    monthly = weekly * 4
    return monthly


def calculate_annual(rate, hours):
    weekly = rate * hours
    annual = weekly * 52
    return annual


def display_result(rate, hours, weekly, monthly, annual):
    print("You make $" + str(weekly) + " a week.")
    print("You make $" + str(monthly) + " a month.")
    print("You make $" + str(annual) + " a year")


def main():
    hours = get_hours()
    rate = get_rate()
    weekly = calculate_weekly(rate, hours)
    monthly = calculate_monthly(rate, hours)
    annual = calculate_annual(rate, hours)
    display_result(rate, hours, weekly, monthly, annual)


main()
