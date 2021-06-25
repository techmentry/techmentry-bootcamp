
"""
Conditionals in python

Conditionals are nothing but meant to compare values or check for validity of a statement or expression.
e.g. is a egg round? would be called as a boolean True value.
is 1 equal to 2 would be a boolean False value

Python gives you if.. else .. expression syntax to check for the validity of a statement

the else statement is an optional expression. This is useful when there is a specific condition, and you want to do something special only then but otherwise continue normally

see some examples
"""

num1 = 2
num2 = -2

if num1 == num2:
    print("Same")
else:
    print("Different")


if num1 ** 2 == num2 ** 2:
    print("Squares are same")
else:
    print("Squares are different")

if num1 == 2:
    print("Number is even and prime")

# else continue with everything else


"""
Some comparison operators in python which are used to generate conditions

va1 == val2 checks if 2 values are equal
val1 != val2 - check if val1 is not equal to val2
val1 > val2 - check if val1 is greater than val2
val1 < val2 - check if val1 is less than val2
val1 >= val2 - check if val1 is greater than or equal to val2
val1 <= val2 - check if val1 is less than or equal to val2

Some string operators - 
Basic == and != works on strings too. But To check if some sub-string is present in a string use 'in' operator

e.g.

if 's' in 'saturn':
    print("Found s")

will print "Found s"
Note : be careful about lowercase and uppercase letters. by default, string comparison is case sensitive i.e. s and S are not the same.
In those cases, you use the upper or lower functions and then compare them e.g.

if "S".lower() in "SatURn".lower():
    print("Present")

will print "Present"
"""


"""
you can check for multiple statements in a if elif else ladder too
Note that individual if statements and if elif are different.
if <condition1>:
    # body
if <condition2>:
    # body
if <condition3>:
    # body

will check ALL if conditions sequentially

But, if a if statement in the if elif ladder is true, further elif and ifs are not executed

again, elif is optional and only used when needed
"""

n = 10

if n % 2 == 0:
    print("even")
if n % 5 == 0:  # this will be executed
    print("divisible by 5")

if n % 2 == 0:
    print("even")
elif n % 5 == 0:  # this will not be executed
    print("divisible by 5")


"""
Functions in python.

What are functions? Functions (or routines or methods), are all names of similar entities in computer programming languages, which are a sequence of instructions
meant to do one ore a set of operations. If you have studied functions in mathematics, you already have some background to this.
e.g. trigonometric functions - sin, cos, tan, cot, sec, cosec

Functions in Python are no different. they are basically a set of instructions executed sequentially (i.e. executed in the order that they appear in).
Can you write your own functions in python? absolutely. You will do it all the time.
How does a function in python look like? Have a look below
"""


def add(num1, num2) -> int:
    my_sum = num1 + num2
    return my_sum


def add_fraction(num1, num2) -> float:
    my_sum = num1 + num2
    return my_sum


"""
The way to declare a function in python is following

def <function name>(parameter1, parameter2, parameter3,....)-> <return value type>
    function body here...
    has to follow the indent guide in python.
    The reason is that that is the only way for python to know what instructions are a part of this function.
    e.g. the statement after this will NOT be considered a part of this function.
I am free!
"""

"""
How do you call a function? You have already seen this with print(). Using a function is often termed as "calling" a function in programming.
Let us call this add function we wrote above, give it a couple of parameters and see the output
"""

# example of integer addition
sum1 = add(1, 2)
sum2 = add(50.2, 566)

print(sum1)
print(sum2)


"""
Loops in python

What are loops? in programming, loops are nothing but constructs which allow us to do things over and over again. How many times you ask? That is decided by the looping parameters you set up.

what is an iteration? when the entire loop body is executed, it starts again at the top of the loop.


There are 2 major types of loops in python

1. for loop
2. while loop

for loop works with a range of values. a general syntax would be

for count_variable in <some sequence>:
    # loop body

This is english would be saying
"keep executing the body inside the for loop, till you reach the end of the sequence". Hence the number of times this for loop will execute is the length of the sequence.

2 common uses of for loop is with range function, and over a list

What is a range function? range function generates a series of numbers uniformly spaced excluding the number you specified. e.g.
for num in range(8):
    # loop body
    # will generate numbers from 0 to 7 inside this loop

there are 2 variants of the range function
1. One range function takes 1 argument - the max number you want to go till.
2. Second variant of the range function takes 2 values, and generates integers in the steps specified

e.g. range(1, 11, 2) reads as generate numbers from 1 to 11, excluding 11 in steps of 2
test the below code out

"""

for num in range(1, 11, 2):
    print(num)

# this will print 1 3 5 7 9


"""
While loops are another common form of loops

general syntax : 
while <condition>:
    # loop body

the while loop checks the condition. if the condition is not true anymore, it will break the loop.

e.g.

i = 2
while i < 10:
    i = i + 1

the above while loop checks for every iteration for i < 10
"""

"""
There are 2 more keywords used with loops - break and continue
If you want to break the loop before the loop would naturally exit, you can use the keyword "break". If you use break, your program will not execute the loop any further.
If you want to skip a loop, and go on to the next iteration in the loop, you can use the keyword "continue". Continue returns the execution of the loop to the top of the program. Note that continue has NO effect on the
number of iterations unlike break, where you can stop the loop before all the iterations have been executed.

e.g.

for num in range(10):
    if num % 2 == 0: # break if we find a even number. other statements will be executed
        break

# other statements.

for num in range(10):
    if num % 2 != 0: # continue if number is odd
        continue # this will force the loop to go back at the start. nothing beyond this will be executed
"""


"""
Now let us use all of this, to write some code in our own function

you can pass a variety of parameters to functions. Single valued or multi-valued parameters are acceptable
e.g. let us see an example of a function, which takes a list of numbers, and calculates the average of those numbers
"""


def calculate_average(list_of_num):
    my_sum = 0.0
    for num in list_of_num:
        my_sum = my_sum + num

    return my_sum / len(list_of_num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(calculate_average(numbers))  # this will print 5.5


# let us join multiple strings to form a sentence

def join_strings(list_of_str):
    sentence = ""
    for element in list_of_str:
        sentence = sentence + " " + element
    return sentence.strip()


print(join_strings(["Hello", "Everyone", "this",
      "will", "come", "out", "as", "a", "sentence"]))
