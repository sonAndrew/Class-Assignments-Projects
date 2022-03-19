""" 
    Author    :  Andrew Jackson
    Class     :  Intorduction to Computing and Programming Concepts
    Section   :  CSCI 1523-92
    File      :  laboratoryProgram4.py
    Date Due  :  02/20/2022
    Professor :  Phil Lamb
    About     :  Lets the user enter two intergers and the prints each step in the process.
"""
# Get File Names
file1 = input("Enter first text file: ")
file2 = input("Enter second text file: ")

# Open Files
f = open(file1, 'r')
f2 = open(file2, 'r')

if file1 == file2:
    print("Yes")
else:
    print("No")
    print("")
    for line in f:
        print(line)
        for line2 in f2:
            print(line2)
            if line == line2:
                print("")
            else:
                print(line, "and", line2, " are not the same.")
                print("")
                break
            break

# Close Files
f.close()
f2.close()