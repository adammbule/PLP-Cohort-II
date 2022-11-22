#Adam Mbule Barasa adammbule98@gmail.com Assignment submission date:20/11/2022
#The assignment comprises of thee questions.

#In each question, you are required to write python code that displays the expected output.

#You are expected to share your source code for review.


#Question one

#Write a python program that will display the number and its square in the following format.

#Number              Square

#1                             1

#2                             4

#3                             9

#4                             14

#5                             25

#6                             36

#Question two

#Write a Python program that prints the length of a string.

#For example of expected results;

#Input Output Explanation

#"" 0 0 because its empty string

#“Jambo” 5, 5 because it has 5 characters

#“Power Learn Project (PLP)” ? ?

 

#Question Three

#Write a Python program that does the following:

#Prints the character at index i in the string "Live happily ".

#my_string = "Live happily ".

#If the index is out of range, the program should print "i is out of range"

#If the string is empty, the program should print "Empty String"
print("Printing Values from the list.")
#Declare the list of values
User_String = input("What is your string?")
#Print the value

#counter
String_Length = len(User_String)
counter = 0
#While loop for the counter
while counter < String_Length:
    print("counting your string value...", String_Length)
    counter = counter + 1
print("'",User_String,"'",String_Length,",",String_Length, "because it has", String_Length, "characters")




