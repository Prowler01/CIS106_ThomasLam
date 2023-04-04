# This program takes user test scores and adds it to the total
# The program repeats until the user says stop
# Then the program spits out the average test score
# References: w3schools

def get_score():
    print("Testscore?: ")
    score = float(input())
    return score

def get_scores_average():
    total = 0
    count = 0
    while True:
        score = get_score()
        if score < 0:
            break
        count = count +1
        total = total + score
        
    average = total / count
    return average
        
        
    
def display_result(average):
    print("Average testscore: " + str(average))
    
def main():
   average = get_scores_average()
   display_result(average)
    
main()
