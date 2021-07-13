'''
python program sample : output a simple string to the console
'''
# below is an example of how to print something to the console using the print function.
# print function
print("This is a string or plain text in python.\nIf this is visible on your console, it means you have run this program successfully!")


'''
python program sample : take an input from the command line
this can be achieved bu using the input function which python provides us with
input function accepts 1 argument: a display string asking the user to input a value.
once the user inputs any value via the keyboard, one can press enter the input function will capture that value and pass it to the program.
Note that this value returned by the input function will be a string. If you want to enter numbers, then you will have to use int or float functions as previously discussed to
convert from that string number to an actual number
'''

name = input("Enter your name: ")
print("Hello, " + name)


# input will return a string, and we will convert that to an int
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
# if you don't convert it, the + opeartion will result in joining those two strings together.
# this will print the sum of those numbers
print("The sum of the two numbers is: " + str(num1 + num2))

