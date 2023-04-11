# This program takes the user's input for year and month
# Then looks up the corresponding month and number of days
# Program runs until user enters an invalid input
# References: Wikipedia, Textbook, geeksforgeeks.com

def get_year():
    print("What year were you born: ")
    year = int(input())
    return year

def get_month():
    print("What month were you born: ")
    month = int(input())
    return month

def get_day():
    print("What day were you born: ")
    day = int(input())
    return day

def get_k(year):
    k = year % 100
    return k

def get_j(year):
    j = year / 100
    return j

def calculate_day(year, month, day, j, k):
    year = get_year()
    month = get_month()
    day = get_day()
    j = get_j()
    k = get_k()
    term1 = day
    term2 = ((month + 1) * 13) / 5
    term3 = k
    term4 = k / 4
    term5 = j / 4
    term6 = 2 * j
    sum = term1 + term2 + term3 + term4 + term5 - term6
    weekday = sum % 7
    weekday = int(weekday)
    return weekday

def convert_weekday(weekday):
    weekday = calculate_day(year, month, day, j, k)
    days = ["Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_of_week = days[weekday]
    return day_of_week

def display_result(weekday, day_of_week):
    #print("Result: " + str(weekday))
    print("You were born on a " + day_of_week + ".")

def main():
    year = get_year()
    month = get_month()
    day = get_day()
    j = get_j(year)
    k = get_k(year)
    weekday = calculate_day(year, month, day, j, k)
    day_of_week = convert_weekday(weekday)
    display_result(weekday, day_of_week)
    
main()