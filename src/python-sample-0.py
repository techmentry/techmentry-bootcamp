# this is a sample file which deals with some basic python constructs that you might find useful

# You might want to comment your code to give it some context maybe. Also, to annotate it correctly. This can be achieved using comments in your code.
# comments in python are of 2 types. Single line comments and multi-line comments.

# Single line comments:
# single line comments start with a pound sign '#', as you can see at the start of this line.
# you do not need to terminate a single line comment. i.e. you do not need to put anything at the end of the comment to mark an end to it

"""
Multi-line comments
Multi line comments are useful when you want to write larger blocks of comments/ annotations in your code.
This is useful when you want to describe and document something useful inside the code itself and it spans more than a few lines,
In this case, adding single line comments would be cumbersome. Multiline comments ease this with their syntax.
The way you write multiline comments are between 3 quotes, as is written here.
Note that there are 3 quotes to start a multiline comment. However, you also have to terminate multiline comments. This is done by writing
3 more quotes at the end of the comment, like below.
"""

# Comments in a program are just for humans to read and understand a program. They mean NOTHING to the computer, and they will not be executed in anyway.
# hence, you can do whatever you want in comments, as they are not a part of the program execution itself, even though they are a part of the program.


# ------------------------------------------------------------------


"""
Variable in python

Variables in Python are similar to variables in mathematics. They are nothing but placeholder values to make writing programs easier.
What can be a variable? any series of a combination of characters from lowercase and uppercase alphabets, '_' character and numbers can form a variable.
e.g. this_is_A_variable. Of course, you would choose to name your variables sensibly, otherwise, you would soon lose track of what a variable holds

the general syntax of assigning value to variables is
<variable name> = <value of that variable>

the value of a variable
1. Can be a constant value e.g. 10, "dosa" or anything else.
2. Can be another variable itself. 
    e.g. variable1 = 10
    variable2 = variable1
3. Can be an expression which results in a value
    e.g. variable1 = 10+2
    variable2 = variable1 * 0.6
    variable3 = math.sin(math.radians(60)) / 5

e.g. in a Banking application, you could have a variable store the amount in your balance
account_balance = 1000.23 USD

in a scientific calculator, you can have a variable to track your values.
sum = 10 + 20 + 56.44

You then just use the variable by its name. That simple.

print(variable1)
print(account_balance)

or, use it in a calculation
account_balance = 1000
deducted_amount = 120
remaining_balance = account_balance - deducted_amount
This will result in remaining_balance being set to 880



Variable naming rules:
1) Variable name can only have a limited series of these characters - a-z, A-Z, 0-9 and _ . All other characters are disallowed.
2) Variables need to start with a non numeric character. i.e. a-z, A-Z, _ . However, they can end with any legal character described in 1.
    e.g. valid variable names
    x1
    value_of_function
    ValidvariaBle9
    ANOTHER_VALID_VARIABLE

    e.g. invalid variable names (these will cause python to throw an error)
    1x (variables cannot start with a number)
    value of function (no spaces allowed)
    invalid-variable (the '-' operator is reserved for subtraction)
    varia:ble (the : operator is reserved for ranges in lists python)

Variable naming convention
1) you want to make your variable names as readable as possible.
2) the best way is to name your variables in simple english. please avoid using single letter variable names.
3) e.g.
amount_in_your_account = 100
amount_in_my_account = 1600
is far far better than
a = 100
b = 1600
and ending up in a soup later if you can't tell what is what.

I will use full variable names. I use underscore to separate words in a variable name like the following

variable_1
value_of_angle
opposite_side_length
side_a

player1_pos
enemy1_pos
"""


"""
Data types in python

What do we mean by data types? We discussed how computers understand only numbers, and more specifically numbers in binary.
We also said that even simple english characters are treated as numbers in Python. Then how do we tell the computer to distinguish between a number and a character?

Enter data types. Data types are an indication to the computer to read the information from a variable in a specified way. I.e.
We instruct the computer to read 65 as a number or as character 'A' by defining the data type of the variable.

So what data types does python supply you with? There are 2 broad categories - single value and multi-value types

Single value types are types which hold, as you guessed, a single value. Here are 3 basic single value types:
    1. You have a data type to denote integers called 'int'. There are no whole numbers or natural numbers in Python. But you can use integers to
    store those values too.
    2. You have plain text/ String data type called "str". All single characters or multiple characters can be represented as this.
    3. You have a data type to denote fractional values, called "float". This is used to denote all decimals to a certain degree of accuracy
    by the computer.

Multi value types are types which hold multiple values within the same variable. There are 3 kinds of multi value types based on how you store data in them
and how you access them.
    1. List :A list is as the name suggests - a continuous sequence of values. This type is used to store multiple values of the same kind. You would
        use this in cases where you have multiple values to denote a certain parameter. Think of continuous block of values, which are separate.
        you can access a value by using the index to that value. The individual values of a list can be any single value data types or multi-value data types.
        the index is nothing but the numeric position of a value. Indexes in python start from 0.
        e.g. my_list = [1,2,3].
        The index of 1 is 0, index of 2 is 1, index of 3 is 2 and so on. The way you access a value is my_list[index]
        If this index is greater than the last index, python will throw an error.
        print(my_list[0]) will print 1
        print(my_list[5]) will throw an error.

    b. Dictionary: A dictionary is slightly exotic - it stores things in a key-value pair. This is useful when you want to have some way of indexing and referencing to data,
        using that index. Think of it like a index of a book - the key is the page number and the value is the content on that page. You can access data in a dictionary by
        using the key, which gets the data. Think of it like a list, where the index is the key here. The key of a dictionary can be any single value data type.
        The value associated with that key, can be any single or multi-valued data type.
        Keys HAVE TO BE UNIQUE i.e. you cannot duplicate keys. Values, don't.
        my_dict = {"key": "value"}
        the way you access this is my_dict["key"]. This will give you the value.

    c. Tuple: A tuple is even more exotic - it is a group of 2 or more values. Think of it like a list above, but you cannot change the number of elements of tuple once you have set it.
        i.e. a list can grow and shrink as you add more values to that list. However, you cannot do this with a Tuple. If you assign 3 values to a tuple, you cannot delete or add values to it.
        However, you can change those 3 values to be anything else.
        Values in a tuple are accessed via their index too.
        Accessing is similar to lists

Please find examples of all of these types below
"""


# single value types
int_val: int = 10
frac_val: float = 9.81
some_text: str = "Welcome to Python."

print(int_val)
print(frac_val)
print(some_text)

# how to join 2 strings using the '+' operator

modified_text: str = some_text + " It is an extremely powerful language"
# below will print "Welcome to Python. It is an extremely powerful language"
print(modified_text)


"""
Note: if you want to join a string a number variable, you first need to convert the number to a string and then join them.
if you try to join a string with any other data type using the + operator, and if the second operator is not a string, you will run in to errors.
"""

# num_and_a_str: str = "Earth is the " + 3 + "rd planet of the solar system" will give you an error
num_and_a_str: str = "Earth is the " + str(3) + "rd planet of the solar system"
print(num_and_a_str)




# examples on converting one type to the other
# using the str(), int() and float() functions
int_conv_to_str = str(int_val)
int_conv_to_frac = float(int_val)

number_string = "1234"
str_conv_to_frac = float(number_string)
frac_conv_to_int = int(2.3)

"""
Note: some conversions will give you an error. e.g. str_conv_to_frac = float(some_text) will throw an error because the value stored
in some_text is not a valid number.
similarly, if you try and convert some string to integer which is not a number it will result in an error.

Also note that converting between int <-> float can give you interesting results.
int -> float will result in the final number being a decimal/ fractional number.
e.g. doing a print(float(2)) will print 2.0
float -> int will result in the final number being a integer without any decimal part.
e.g. doing a print(int(4.66)) wil print 4

Be careful using these operations.
"""

"""
Some important string functions, which will help you manipulate text

1. len() - to find the number of characters in a string. 
e.g.
my_str = "Hello"
print(len(my_str)) would print 5

2. str.upper() - to convert the string to upper case

e.g.
my_str = "Hello"
print(my_str.upper()) would print "HELLO"

3. str.lower() - to convert the string to lower case
e.g.
my_str = "HEllO"
print(my_str.lower()) would print "hello"

4. str.strip() - to trim the string of whitespaces at both ends
e.g.
my_str = "  HEllO "
my_str_1 = "  HEllO"
my_str_2 = "HEllO  "
my_str_2 = "HEllO"

print(my_str.strip()) would print "HEllO"
print(my_str_1.strip()) would print "HEllO"
print(my_str_2.strip()) would print "HEllO"
print(my_str_3.strip()) would print "HEllO"
"""

# multi-value types
list_of_int = [1, 2, 3, 4, 5]
list_of_frac = [1.2, 2.5, 35.0, 4.1, 5.3]
list_of_str = ["This", "is", "a", "list",
                "of", "strings", "and", "a", "character"]


print(list_of_str[4])  # will print "of"
print(list_of_frac[2])  # will print 35.0
# print(list_of_frac[10])  # will throw a index out of bounds error

# to add values to a list, use the append function. This will add the element at the end of the list
list_of_frac.append(2.3)
# to remove a value from the list, use the remove function and give it the value you want to remove. it will remove the first occurrence of that value from the list.
list_of_frac.remove(2.5)
# to change the value at an index, you can refer to that value via the index and assign a new value
list_of_int[2] = 10  # will change 3 to 10

dict_of_str = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# invalid dictionary as there are duplicate keys
# dict_of_str = {
#     "key1": "value1",
#     "key1": "value2",
#     "key3": "value3"
# }

dict_of_int = {
    "key1": 1,
    "key2": 2,
    "key3": 3
}

dict_with_int_key = {
    1: "value1",
    2: "value2",
    3: "value3"
}

print(dict_of_int["key2"])  # will print "2"
print(dict_with_int_key[3])  # will print "value3"
# print(dict_with_int_key[4])  # will throw a key not found error

# to add a new key and value to the dictionary, or to change the existing value of a key in a dictionary, you can use indexing
new_key = 98324
dict_with_int_key[new_key] = "value4"
print(dict_with_int_key[new_key])  # will print "value4"

# to remove a key and value from a dictionary use the 'del' operator like so
# will remove the key value pair ("key1": 1) from the dictionary
del dict_of_int["key1"]

# assigning tuples
tuple1 = (1, 2, 3)  # a 3-tuple
coordinates = (5, -9)  # a 2-tuple

# print(coordinates[3]) # will throw an error
print(coordinates[1])  # will print -9

"""
Some important functions to go with multi-value data types.

These functions help you find a lot of things about these multi-value variables

1. Size of these variables - to find out how many elements are in a multi-value variable, use the len() function
e.g.
my_list = [1,2,3]
print(len(my_list)) would print 3

my_dict = {
    "key1": 123,
    "key2": 456,
    "key3": 789,
    "key4": 000
}
print(len(my_dict)) would print 4

2. Minimum value in a list - to find out what is the lowest value in a multi-value variable, using the min() function
my_list = [1,-2,3]
print(min(my_list)) would print -2
"""
