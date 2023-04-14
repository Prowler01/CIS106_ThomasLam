# This program asks the user how many test scores
# The program then takes that number of test scores
# and adds those test scores to a static array
# The program then calculates the highest, lowest
# and average test scores.
# References: geeksforgeeks.org, w3schools, khanacademy

def get_num_scores():
    print("How many testscores: ")
    num_scores = int(input())
    return num_scores

def get_scores():
    print("Testscore: ")
    score = int(input())
    return score

def get_score_array(num_scores):
    array = [None] * num_scores
    count = 0
    while True:
        array[count] = get_scores()
        count = count + 1
        if count >= num_scores:
            break
    return array

def calculate_lowest(array):
    array.sort()
    lowest = array[0]
    return lowest

def calculate_highest(array):
    array.sort()
    highest = array[len(array) - 1]
    return highest

def calculate_average(array):
    sum = 0
    for i in range(0, len(array)):
        sum = sum + array[i]
    num_elements = len(array)
    average = sum / num_elements
    return average

def display_result(array):
    print(array)

def display_result2(lowest, highest, average):
    print("Lowest: " , lowest)
    print("Highest: ", highest)
    print("Average: " , average)

def main():
    num_scores = get_num_scores()
    array = get_score_array(num_scores)
    display_result(array)
    lowest = calculate_lowest(array)
    highest = calculate_highest(array)
    average = calculate_average(array)
    display_result2(lowest, highest, average)
    
main()
         
