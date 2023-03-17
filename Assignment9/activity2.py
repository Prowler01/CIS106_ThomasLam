# This program calculates the student's average testscore
# Using a while loop. The program takes the user's input score
# And adds it to the total score every iteration

# References: Program plan


def get_test_count():
    print("How many test scores: ")
    test_count = int(input())
    return test_count


def get_total(test_count):
    count = 1
    total = 0
    while count <= test_count:
        print("Test score " + str(count) + ": ")
        testscore = int(input())
        total = total + testscore
        count = count + 1
    return total


def calcualte_average(test_count, total):
    average = float(total / test_count)
    return average


def display_result(average):
    print("Average test score: " + str(average))
    

def main():
    test_count = get_test_count()
    total = get_total(test_count)
    average = calcualte_average(test_count, total)
    display_result(average)


main()
