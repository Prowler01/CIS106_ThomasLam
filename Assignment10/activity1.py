# This program takes user test scores and adds it to the total
# The program repeats until the user says stop
# Then the program spits out the average test score
# References: w3schools

def get_score():
    print("Testscore: ")
    score = int(input())
    print("Enter a negative value in to stop program.")
    return score

def get_total(score):
    total = 0
    count = 0
    if score < 0:
        return output
    while score > -1:
        count = count +1
        score = get_score()
        total = total + score
        
    output = [total, count]
    return output

def calculate_average(output):
    average = int(output[0] / output[1])
    print("Total: " + str(output[0]))
    print("Count: " + str(output[1]))
    return average

def display_result(average):
    print("Average test score: " + str(average))

def main():
    score = get_score()
    # total = get_total(score)
    # count = get_total(score)
    output = get_total(score)
    average = calculate_average(output)
    display_result(average)
    
main()
    

        

