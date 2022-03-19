""" 
    Author    :  Andrew Jackson
    Class     :  Intorduction to Computing and Programming Concepts
    Section   :  CSCI 1523-92
    File      :  laboratoryProgram5.py
    Date Due  :  02/27/2022
    Professor :  Phil Lamb
    About     :  Write a program that inputs a text file.
                 The program should print the unique words in the file
                 in alphabetical order.
"""
# Variables
fileName = input("Enter text file name: ")

# Opens file and reads it
f = open(fileName, 'r')
wordsList = []

for line in f:

    for word in line.split():
        item = word.upper()
        wordsList.append(item)

wordsList.sort()

for item in wordsList:
    print(item)
    
f.close()