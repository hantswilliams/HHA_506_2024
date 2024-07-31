name_Last = 'Williams'  # this is EHR last name of patient  
name_First = "Hants"

testFString = f'Patient lastname: {name_Last}, Patient First Name: {name_First}' 
combinedName = name_First + ' ' + name_Last
print(combinedName)
print('This is a message to the ender user')

name_Story = """
This is where hants' story might go 
he is originally from california 
"""

name_Address_Street = "Bishop"

secret007 = 'bond'


# Examples that you cant call variables (e.g., reserved words: def, if, else, elif, for, while, etc.)
# in addition to these, you can't start a variable with a number, or use special characters, 

# Vars are also case sensitive 

# Variables can be assigned to other variables, and can be reassigned

# Variables can be of different types, and can be reassigned to different types



##### Variables - Types #####

# Variables can be of different types, and can be reassigned to different types

num1 = 5
number1 = 5
numberOne = 5

# Integers - whole numbers, e.g., 1

number2 = 5.52342342434343434

type(number1)


# Floats - floating point numbers, e.g., 3.14

# Strings - defined with single or double quotes, e.g., 'hello' or "hello", f strings are also available

# Booleans - True or False

hants = False
williams = True


# Lists - mutable lists that are defined with square brackets, e.g., [1, 2, 3], you can change the values in a list

# bloodPressureSystolicValues
bp_systolic = [
    '140.23', 
    100, 
    50.5,
    120, 
    '150',
    300.243,
    23,
    ]


bp_systolic[4]
bp_systolic[:10]
len(bp_systolic)

# Tuples: immutable lists that are defined with parentheses, e.g., (1, 2, 3) - you can't change the values in a tuple

hants = (1, 2, 3)

# Dictionaries - key-value pairs that are defined with curly braces, e.g., {'key': 'value'}, you can change the values in a dictionary

pat1 = {
    'firstName': 'Hants',
    'lastName': 'Williams',
    'middleName': 'Andrew',
    'age': 40, 
    'demographics': {
        'sex': 'male',
        'race': 'white'
    },
    'lab_plt': [150, 180, 300, 350],
    'address': {
        'street': 'Bishop',
        'number': 1910,
        'city': 'Belmont'
    }
}

type(pat1)

pat1['demographics'].keys()
pat1['address'].keys()

pat1['address']['city']

# pat1['socialsecuritynumber']

pat1.get('address')
pat1.get('socialsecuritynumber')



pat1['lab_plt'][:2]

pat1['middleName'] + ' ' + pat1['firstName']

# Sets - unordered collections of unique elements that are defined with curly braces, e.g., {1, 2, 3}, you can change the values in a set



##### Variables - Operations #####

# Variables can be used in operations

var1 = 500
var2 = 0

# var1 / var2 

var3 = [500, 200, 500]
var4 = 500.01

type(var3)
type(var4)

# var3 + var4 

# Addition - +, e.g., 1 + 1

# Subtraction - -, e.g., 1 - 1

# Multiplication - *, e.g., 2 * 2

# Division - /, e.g., 4 / 2

# Exponentiation - **, e.g., 2 ** 3



####### Conditional Statements #####

# Conditional statements - if, elif, else

# If statements - if a condition is met, then do something

# Elif statements - if the first condition is not met, but the second condition is met, then do something else

# Else statements - if none of the conditions are met, then do something else

##### Conditional Statements - Comparison Operators #####

# Comparison operators - ==, !=, >, <, >=, <=

# Equal - ==, e.g., 1 == 1

# Not equal - !=, e.g., 1 != 2

# Greater than - >, e.g., 2 > 1

# Less than - <, e.g., 1 < 2

# Greater than or equal to - >=, e.g., 2 >= 2

# Less than or equal to - <=, e.g., 1 <= 2


## Loops ##

# Loops - for, while

zipcodes = ['34343', '202023', '343434', '31212']

print('Zipcode 1: ', zipcodes[0])
print('Zipcode 2: ', zipcodes[1])
print('Zipcode 3: ', zipcodes[2])
print('Zipcode 4: ', zipcodes[3])

print(f'Zipcode 1: {zipcodes[0]}')
print(f'Zipcode 2: {zipcodes[1]}')
print(f'Zipcode 3: {zipcodes[2]}')
print(f'Zipcode 4: {zipcodes[3]}')

for x in zipcodes: 
    print('Zipcode is: ', x)

for value in zipcodes:
    print(f'Zipcode is {value}')

ages = [50, 60, 54, 34, 53, 20]

count = 0
for x in ages: 
    print('We are looking at: ', count)
    count+= 1 
    age_plus10 = x + 10
    print('Original age: ', x)
    print('Your age in 10 years is: ', age_plus10)

value1_org = ages[0] 
value1_new = value1_org + 10 

for x in ages: 
    if x >= 59:
        age_plus10 = x + 10
        print('Original age: ', x)
        print('Your age in 10 years is: ', age_plus10)
    else:
        print('Number is no good')


# For loops - for each item in a collection, do something

# While loops - while a condition is met, do something


listofDictionarys = [
    {
        'name': 'Student 1'
    },
    {
        'name': 'Student 2'
    },
    {
        'name': 'Student 3'
    },
]

type(listofDictionarys)
type(listofDictionarys[0])

for x in listofDictionarys:
    print('Object type: ', type(x))
    print('Student name', x['name'])




##### Variables - Functions #####

# Variables can be used in functions

# Functions are defined with the def keyword, followed by the function name, and then parentheses with any arguments

# Functions can return a value with the return keyword

def function(x, y ,z): 
    # do your thing 
    return x 

def bloodpressure(x, y):
    print(f'Your BP is {x} / {y}')

def bloodpressure(sys, dia):
    print(f'Your BP is {sys} / {dia}')
    if sys >= 130:
        print('Your systolic value is too high')
    else:
        print('Your systolic is fine....')

    if dia >= 80:
        print('Your diastolic is a bad value...')
    else:
        print('Your diastolic appears to be ok.....')


bloodpressure(120, 80)
bloodpressure(500, 500)