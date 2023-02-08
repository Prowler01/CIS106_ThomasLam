# This program converts user age from 
# years to months, days, hours, and seconds.

# References: Programming fundamentals textbook 
# and office hours with Professor Braunsweig

print("Enter user age in years: ")
years = float(input())

months = years * 12
days = years * 365
hours = days * 24
seconds = hours * 60 * 60

print("User is " + str(months) + " months old")
print("User is " + str(days) + " days old")
print("User is " + str(hours) + " hours old")
print("User is " + str(seconds) + " seconds old")
