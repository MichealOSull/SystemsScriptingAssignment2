#Micheal O' SUllivan
#R00128516
#Systems Scripting - Assignment 2
#
#The purpose of this task was to write a Python Script that implements a function that accepts two parameters. For these parameters to be implements
#certain criteria needed to be met for the purpose of this task. Such as the length of the list, the number of items to be deleted and an updated list
#when this criteria was met. For this to be implement I created 3 other functions called listOption, numberOption and delete.
#
#The listOption fucntion was used to make sure that a minimum of 12 items were entered seperated by a comma(The first parameter in main). If the user did not enter a suffice number of items, this function was called and would loop until 12 items were entered. If this function was needed, the items entered were then #appended(added) to the list
#
#The numberOption function was used to force the user to enter an option between 2-6 if the user enetered a number less than 2 or greater than 6. This was the second paramater in the main function, once the user entered a valid integer, the number was returned.
#
#The delete function was used to created a updated list (tuple) by using the list and number arguments. Once a valid list and number were entered, we copied
#the original list and used to random geneator to generate indexes of where to update the list(remove items). We then returned this updated list as the tuple
#
#The main function was used to implement the two parameters needed for this task. First the user was asked to enter 12 items seperated by a comma, if this was #not met, the listOption function was called until it was met. The second paramater was to enter a number between 2 and 6 which was to be the number of items
#deleted from the list. Since this needed to be a whole integer, error handling was used in case an invalid value was enetered. Also if an integer entered,
#was not between 2-6, the numberOption was called until this condition was met. The updatedList was then declared and the Result Tuple (updated list) and
#also the orginal list were then printed. 



#import random module for use in delete function
import random

#Create function for controlling user input for list
def listOption(list):
    while True:
        #list needs to be minimum of 12 items
        if (len(list) < 12):
            userInput = input("Not enough items in list, minimum 12 needed!: ")
            #use comma to seperate items in list
            addToList = userInput.split(",")
            #add items to list until minimum of 12 is met
            for i in range(len(addToList)):
                list.append(addToList[i])
        else:
            return list

#Create fucntion for controlling number option for items to be deleted(Between 2-6)
def numberOption(number):
    while True:
        if(number<2):
            number = int(input("Invalid input, please enter an integer between 2-6!: "))
        elif(number>6):
            number = int(input("Invalid input, please enter an integer between 2-6!: "))
        else:
            return number

#Create function to delete items from list and create updated List
def delete(list, number):
    #copy original list to use for update
    updatedList=list.copy()
    for x in range(number):
        newVal=random.randint(1,4)
        del updatedList[newVal]
    return tuple(updatedList)

#Create main function to run both parameters of task
def main():
    userInput = input("Please enter a minimum of 12 items into list seperated by a comma: ")
    list = userInput.split(",")
    list = listOption(list)

    while True:
        try:
            number = int(input("Please enter the amount of items to be deleted (Between 2-6): "))
            number = numberOption(number)
            break
        except ValueError:
            print("Value not valid! Enter integer between 2-6!")

    updatedList=delete(list, number)
    print("Result Tuple: ", updatedList)
    print("Original List: ", list)
main()
            
    
