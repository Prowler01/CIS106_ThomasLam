# This program calculates a student's average testscore
# Takes user input for how many test results, and takes average
# References: textbook and Khanacademy video


def get_numtests():
    print("How many test scores would you like to enter: ")
    num_tests = int(input())
    return num_tests


def get_total(num_tests):
    total = 0
    count = 1
    for count in range(1, num_tests +1, 1):
        print("Testscore: ")
        testscore = int(input())
        total = total + testscore
        
    return total
        
        
def calculate_average(num_tests, total):
    average = float(total / num_tests)
    return average


def display_result(average):
    print("Average test score: " + str(average))
  

def main():
    num_tests = get_numtests()
    total = get_total(num_tests)
    average = calculate_average(num_tests, total)
    display_result(average)
    
main()
