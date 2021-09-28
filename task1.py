#Micheal O' SUllivan
#R00128516
#Systems Scripting - Assignment 2
#
#The purpose of this task was to write a Python Script that implements two functions where each accepts a single list parameter containing strings.
#
#The first function queMark was to check and output the items within the list that contained a "?". Within the function I declared the list global as we want #to use the same list in the second fucntion. For this task we were given a list of items to use, so I left this in comments for future reference, this items #were to be seperated by using a comma and then we iterated through each individual item in the list and which ever items contained a "?" were to be printed 
#confirming they contained a "?"
#
#The second function characters was to check and output all charcters that appear in each of the list items. Similar to the first function
#we used the same list as it was declared global. We then iterate through each item and then each letter within the list, followed by counting the number of #times each letter appears by using the .count() method. We then print each individual item followed by the letter it contains and how many times that letter #appears within the item.



#Create function to output items in list which contain a "?"
def queMark():
    #list below to be used when asked for input 
    #refList = [farshad,ghassemi?d,madam,?radar?,duration,con?tained]
    global list
    userInput = input("Please enter items seperated by a comma: ")
    print()
    list = userInput.split(",")
    
    for string in list:
        if "?" in string:
            print(string, "contains a question mark")
queMark()

print("\n")

#Create function to output items which contain characters that appear in each item in list
def characters():
    for string in list:
        for letter in string:
            i = string.count(letter)
            print(string, "contains", i, letter)

characters()
