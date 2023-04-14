# This program asks the user how many testscores
# they would like to enter. The program then
# uses a loop to add the scores to the array
# Highest, lowest, and average score are calculated
# The program uses a sort function to sort the scores
# from highest to lowest
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
            #print("End program")
            break
        array.append(score)
    return array

def calculate_highest(array):
    array.sort()
    highest = array[0]
    return highest

def calculate_lowest(array):
    array.sort
    lowest = array[len(array)-1]
    return lowest

def calculate_average(array):
    sum = 0
    for i in range(0, len(array)):
        sum = sum + array[i]
    num_elements = len(array)
    average = sum / num_elements
    return average

def sort_array(array):
    sorted = array
    sorted.sort(reverse=True)
    return sorted


def display_result(sorted):
    print("Sorted array: " , sorted)
    

def main():
    array = get_score_array()
    highest = calculate_highest(array)
    lowest = calculate_lowest(array)
    average = calculate_average(array)
    sorted = sort_array(array)
    display_result(sorted)
    
main()
