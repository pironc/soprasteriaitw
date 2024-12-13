##
## SOPRA STERIA ITW
## EVEN OR ODD
##


import random


# Function to generate and store a random number to try our the even or odd function
def read_number():
    return (random.randint(0, 42))


# Checking if the parameter is an integer or not
def is_var_int(num):
    res = isinstance(num, int)

    if res != True:
        print("Error: You need to give a number as paramter.")
        return (-1)
    return (0)



# General function to print from num to N, to avoid code repetition
def print_reverse(num, n):
    while num >= n + 1:
        if num % 2 == 0:
            print(num, end=', ')
        num -= 1
    print(num)


# Even or odd function, to check whether a number is even (in that case printing all other even numbers from N to 0),
# otherwise if odd, same behaviour but from N to 1
def even_odd(num):
    if is_var_int(num) != 0:
        return (-1)

    if num % 2 == 0:
        print_reverse(num, 0)
    else:
        print_reverse(num, 1)
    return (0)


# Main function to run the program and get default variables to use in the program functions
def main():

    # read_number is the "LEER NOMBRE" or "LIRE NOMBRE" instruction from the document
    num = read_number()

    # showing the randomized number used for the program testing, up to 42 included
    print(f"Randomized number: {num}")
    ret = even_odd(num)

    return (ret)

main()