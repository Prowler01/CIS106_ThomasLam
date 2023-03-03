# This programs determines the user's sock size
# Based on user's shoesize input
# References: textbook

def get_shoesize():
    print("What is your shoe size: ")
    shoesize = int(input())
    return shoesize


def calculate_socksize(shoesize):
    if shoesize < 4:
        socksize = "Extra Small"
        return socksize
    elif shoesize  < 7:
        socksize = "Small"
        return socksize
    elif shoesize < 9:
        socksize = "Medium"
        return socksize
    elif shoesize < 12:
        socksize = "Large"
        return socksize
    else:
        socksize = "Extra Large"
        return socksize

def display_result(shoesize, socksize):
        print("Socksize: " + str(socksize))
        
def main():
       shoesize = get_shoesize()
       socksize = calculate_socksize(shoesize)
       display_result(shoesize, socksize)

    
main()
