# This programmer ges the user's first and last name
# The first and last name is inputted as a single line
# The program outputs the string in 
# Lastname, Firstname Initial form
# References: tutorialswebsite.com, flexiple.com
# References: freecodecamp, geeksforgeeks, w3schools
# References: Wikiversity

def get_name():
    print("What's your fullname: ")
    full_name = (input())
    index = full_name.find(" ")
    if index == 0:
        full_name = get_name()
    return full_name


def get_lastname(full_name):
    all_names = full_name.split()
#    length = len(all_names)
#    if length < 1:
#        main()
    last_name = all_names[len(all_names) - 1]
    last_name = last_name.capitalize()
    return last_name


def get_first_letter(full_name):
    all_names = full_name.split()
    first_name = all_names[0]
    first_letter = first_name[0]
    first_letter = first_letter.upper()
    return first_letter


def create_string(last_name, first_letter):
    name_string = " "
    name_string = last_name + ", "
    name_string += first_letter
    name_string += "."
    return name_string
    

def display_result(name_string):
    print(name_string)

    
def main():
    full_name = get_name()
    last_name = get_lastname(full_name)
    first_letter = get_first_letter(full_name)
    name_string = create_string(last_name, first_letter)
    display_result(name_string)
 

main()
