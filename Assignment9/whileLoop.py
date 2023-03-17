# This program calculates the student's average testscore
# Using a while loop. The program takes the user's input score
# And adds it to the total score every iteration
# References: Program plan

def get_num_tests():
    print("How many test scores: ")
    num_tests = int(input())
    return num_tests

def get_total(num_tests):
    count = 1
    total = 0
    while count <= num_tests:
        print("Testscore " + str(count) + ": ")
        testscore = int(input())
        total = total + testscore
        print("Total: " + str(total))
        count = count + 1
    return total

def calcualte_average(num_tests, total):
    average = float(total / num_tests)
    return average

def display_result(average):
    print("Average testscore: " + str(average))
    
def main():
    num_tests = get_num_tests()
    total = get_total(num_tests)
    average = calcualte_average(num_tests, total)
    display_result(average)
    
main()

