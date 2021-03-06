"""
ð Python: Basic Data Types ð

â Numbers
  â® Integers
  â® Floating Points
  â® Complex

â Boolean

â String
--------------------------------

1. Integers 

â¤ include all positive and negative whole numbers

â¤ occupy an amount of memory depending on their value

--------------------------------

2. Floating Points

â¤ include all positive and negative decimal numbers

â¤ occupy 24 bytes of memory (16 for the reference counter and 8 for the number)

--------------------------------

3. Complex

â¤ support complex numbers made up of a real and an imaginary part

â¤  created using complex() with 2 arguments: the 1st is the real part, while the 2nd is the imaginary part

--------------------------------

4. Boolean

â¤ a data type with only 2values: True and False

â¤ the first letter of a bool needs to be capitalized

--------------------------------

5. Strings 

â¤ a collection of characters closed within single, double or triple quotation marks

â¤ triple quotes are used to add a multi-line string

â¤ the len() built-in function retrieve the length of a string

â¤ every character has a numerical index based on its position

â¤ every character can be accessed using its index closed within square brackets

â¤ negative indices access characters from the end of the string

â¤ strings are immutable: once you assign a value to a string, you canât update its characters

â¤ but you can assign a new string to a string varable

â¤ From Python 3.x, all strings are unicode

"""

def numbers():

    print(10)  # A positive integer
    print(-5)  # A negative integer

    # Assigning an integer to a variable
    num = 12345  
    print(num)

    # Assigning a new integer
    num = -54321  
    print(num)

    print(1.009)  # A positive float
    print(-3.68)  # A negative float

    # Assigning a float to a variable
    flt_pt = 1.2345
    print(flt_pt)

    # Represents the complex number (4 + 5j))
    print(complex(4, 5))  

    # Assigning a complex to a variable
    complex_num = complex(0, 2)
    print(complex_num)


def bools():
    print(True)  

    # Assigning a boolean to a variable
    bool_var = False
    print(bool_var)

def strings():
    print("I am Franco")  # Double quotation marks

    country = 'I am italian'  # Single quotation marks
    print(country)

    empty = ""
    print(empty)  # Prints an empty line

    multiple_lines = '''Triple quote for
    multi-line strings'''
    print(multiple_lines)

    print(len(country)) # 12 characters

    first = country[0]  # Accessing the first character
    print(first)

    space = country[4]  # Accessing the 2nd empty space 
    print(space)

    last = country[len(country) - 1]
    print(last)
    print(country[-1])  # Corresponds to country[11]

    # country[0] = 'S' will give error

    print(id(country))
    country = "switzerland"
    print(id(country))  # id is changed