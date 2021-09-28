#Micheal O' SUllivan
#R00128516
#Systems Scripting - Assignment 2
#
#The purpose of this task was to write a Python Script that implements a recursive function named reducer() that accepts an integer parameter named number.
#
#The reducer function first ensures theat the value entered is valid, although this work with any integer, if the value is negative it will get stuck in a #loop, so I used an if statement to ensure that the number was greater than 0. If the number was divisable by 2, it was returned and divided by two, and if #the number was not divisable by 2 it was multipled by 3 and 1 was added to it. This provess works until the number reaches 1 which is shown in the main #function  
#
#The main function was used to get a user to enter an integer which then called the recursive function reducer(). Exception handling was implemented
#in the case of a user entering an invalid value. This recursive function was called until the value reached was equal to 1.



#Create a fucntion to ensure firstly number is valid and then to divide/multiply depending on value
def reducer(number):
    while True:
        if (number < 1):
            number = int(input("Invalid input, enter a number greater than 0: "))
        elif (number % 2 == 0):
            return int(number/2)
        else:
            return (number*3)+1

#Create function to run parameters from user input 
def main():
    while True:
        try:
            number = int(input("Please enter an integer: "))
            break
        except ValueError:
            print("Error, incorrect value, please enter an integer: ")
    while number != 1: 
        number = reducer(number)
        print(number)
main()
