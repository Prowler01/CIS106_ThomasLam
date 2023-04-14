# This program asks the user to enter grade scores
# The scores are added to a dynamic array
# The program accepts user input data until a negative value
# is entered, then the program displays the high, low, and average
# scores entered.
# References: Professor, geeksforgeeks.org, w3schools
# Referenes: tutorialspoint.org, en.wikiversity.org

def get_score():
    print("Testscore: ")
    score = int(input())
    return score


def get_score_array():
    array = []
    while True:
        score = get_score()
        if score < 0:
    # print("End program")
            break
        array.append(score)
    return array


def calculate_highest(array):
    array.sort()
    highest = array[0]
    return highest


def calculate_lowest(array):
    array.sort
    lowest = array[len(array) - 1]
    return lowest


def calculate_average(array):
    sum = 0
    for i in range(0, len(array)):
        sum = sum + array[i]
    num_elements = len(array)
    average = sum / num_elements
    return average


def display_result(highest, lowest, average):
    print("Your lowest score is: " + str(highest))
    print("Your highest score is: " + str(lowest))
    print("Your average score is: " + str(average))

    
def main():
    array = get_score_array()
    highest = calculate_highest(array)
    lowest = calculate_lowest(array)
    average = calculate_average(array)
    display_result(highest, lowest, average)
  

main()
