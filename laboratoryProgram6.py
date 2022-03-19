"""
    Author    :  Andrew Jackson
    Class     :  Intorduction to Computing and Programming Concepts
    Section   :  CSCI 1523-92
    File      :  laboratoryProgram6.py
    Date Due  :  03/20/2022
    Professor :  Phil Lamb
    About     :  Package Newton's Raphson Method
"""
# Import math method
import math

# The main() function - Below
def main():
    while condition(): # While the codition() function holds 
        condition()    # Then execute the codition() function

# The condition() function to run program
def condition():
    # Variables
    ask = input("Do you want to run the program (y or n)? ")  # Ask if user wants to run program.
    yes = "y"                                                 # yes value
    no = "n"                                                  # no value
    
    # Ask if person wants to continue with the program
    if ask == yes:                                            # If (ask = "y")
        getNumber = float(input("Enter a positive number: ")) # Get the number from user.
        return newton(getNumber)                              # Use of the Newton Raphson Method function.
    elif ask == no:                                           # If (ask = "n") 
        print("You have choosen to exit program. ")           # Then print "You have choosen to exit program."
        raise SystemExit                                      # End program by raising SystemExit without (import sys).

# Newton Method Function - Below
def newton(num):
    # Variables
    tolerance = 0.00001                             # tolerance value.
    estimate = 1.0                                  # estimate value.
    x = num                                         # getting the main input number.

    while True:
        estimate = (estimate + x / estimate) / 2    # Transforms the estimate
        difference = abs(x - estimate ** 2)         # Use the abs() function to obtain its absolute value/difference. 

        if difference <= tolerance:                 # Check if the difference is less than or equal to the  tolerance.
            break

    print("The program's estimate: ", estimate)     # Print the program's estimate.
    print("Python's estimate:      ", math.sqrt(x)) # Print Python's estimate.
    return estimate                                 # Return the estimate of the number.

# def newton(num):
#     # Variables
#     tolerance = 0.00001                   # tolerance value
#     x = num                               # Assuming the sqrt of n as n only
#     count = 0                             # To count the number of iterations
    
#     while (tolerance) :
#         count += 1                        # Update count each rotation by 1
#         root = 0.5 * (x + (num / x))      # Use of Neton Method - Calculate more closed x

#         # Check for closeness of the root
#         if (abs(root - x) < 1) :
#             break

#         x = root                          # Update root value
    
#     print(root)
#     return root

# The entry point for program execution - Below
if __name__ == "__main__":
    main()