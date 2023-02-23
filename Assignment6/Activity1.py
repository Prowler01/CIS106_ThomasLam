# This program calculates pay based on rate and hours
# Program calculates weekly, monthly, and annual pay

# References: 
    #program plan
    
def getPay():
    print("Enter hourly pay: ")
    pay = float(input())
    return pay

def getHours():
    print("Enter hours worked per week: ")
    hours = float(input())
    return hours

def calculateWeekly(pay, hours):
    weekly = pay * hours
    return weekly

def calculateMonthly(pay, hours):
    weekly = pay * hours
    monthly = weekly * 4
    return monthly

def calculateAnnual(pay, hours):
    weekly = pay * hours
    monthly = weekly * 4
    annual = monthly * 12
    return annual

def displayResult(pay, hours, weekly, monthly, annual):
    print("You make $" +str(pay) + " an hour.")
    print("You work $" + str(hours) + " hours a week.")
    print("You make $" + str(weekly) + " a week.")
    print("You make $" + str(monthly) + " a month.")
    print("You make $" + str(annual) + " a year")
    
def main():
    pay = getPay()
    hours = getHours()
    weekly = calculateWeekly(pay, hours)
    monthly = calculateMonthly(pay, hours)
    annual = calculateAnnual(pay, hours)
    displayResult(pay, hours, weekly, monthly, annual)
    
main()

