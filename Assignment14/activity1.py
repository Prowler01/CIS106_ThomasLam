# The program then calculates the highest, lowest, and average scores
# References: askpython.com, textbook, Techwithtim on youtube
# References: realpython.com, wikiversity, Professor

#import os
#import sys


def read_scores(filename):
    scores = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            name, score = line.strip().split(',')
            scores.append(int(score))
        return scores
    
    
def calculate_highest(scores):
    scores.sort()
    highest = scores[0]
    return highest


def calculate_lowest(scores):
    scores.sort
    lowest = scores[len(scores) - 1]
    return lowest


def calculate_average(scores):
    sum = 0
    for i in range(0, len(scores)):
        sum = sum + scores[i]
    num_elements = len(scores)
    average = sum / num_elements
    return average


def display_result(highest, lowest, average):
    print("Your lowest score is: " + str(highest))
    print("Your highest score is: " + str(lowest))
    print("Your average score is: " + str(average))

    
def main():
    filename = "scores.txt"
    scores = read_scores(filename)
    highest = calculate_highest(scores)
    lowest = calculate_lowest(scores)
    average = calculate_average(scores)
    display_result(highest, lowest, average)
  

main()
