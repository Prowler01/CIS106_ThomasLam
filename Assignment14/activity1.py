# This program reads a text file of scores
# And builds an array of scores based on the file
# The program then calculates the highest, lowest, and average scores
# References: askpython.com, textbook
# Refernces: realpython.com, wikiversity

import os
import sys
import pandas as pd


#def read_scores(file_path):
#    scores = []
#    with open(file_path, "r") as file:
#       for line in file:
#            score = int(line.strip())
#            scores.append(score)
#    return scores

def create_file(filename):
    file = open(filename, "w")
    file.write("C\tF\n")
    for c in range(0, 51):
        f = c * 9 / 5 + 32
        file.write(f"{c:.1f}\t{f:.1f}\n")
    file.close()
    
def read_file(filename):
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        print(line)
    file.close()
    print("")

#def read_scores(file_path):
#    scores = []
#    with open(file_path, "r") as file:
#       for line in file:
#            score = int(line.strip())
#            scores.append(score)
#    return scores

def calculate_highest(scores):
    highest = max(scores)
    return highest

def calculate_lowest(scores):
    low = min(scores)
    return low

def calculate_average_score(scores):
    average = sum(scores) / len(scores)
    return sum(scores) / len(scores)

def display_result(scores):
    print("Scores:", scores)
    print("Highest score:", highest_score)
    print("Lowest score:", lowest_score)
    print("Average score:", average_score)
    

def main():
    score = "-scores.txt"
    scores = read_scores("scores.txt")
    highest_score = calculate_highest_score(scores)
    lowest_score = calculate_lowest_score(scores)
    average_score = calculate_average_score(scores)
    
    
main()
