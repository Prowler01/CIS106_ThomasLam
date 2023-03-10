# This program calculates a student's average testscore
# Takes user input for how many test results, and takes average

# References: textbook and Khanacademy video


def get_test_count():
    print("How many test scores would you like to enter: ")
    test_count = int(input())
    return test_count


def get_total(test_count):
    total = 0
    for count in range(1, test_count + 1, 1):
        print("Testscore: ")
        testscore = int(input())
        total = total + testscore        
    return total
        
        
def calculate_average(test_count, total):
    average = float(total / test_count)
    return average


def display_result(average):
    print("Average test score: " + str(average))
  

def main():
    test_count = get_test_count()
    total = get_total(test_count)
    average = calculate_average(test_count, total)
    display_result(average)
 

main()
