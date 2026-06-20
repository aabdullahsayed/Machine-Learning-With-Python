# Python Basics

Python is a high-level, interpreted programming language known for its readability and simplicity. It is widely used for web development, data analysis, artificial intelligence, and automation. Because it is interpreted, you run the code line-by-line, which makes debugging easier.

## Hello World

The first step in any programming language is outputting text to the console.

```python
print("Hello, World!")
print("I Hate pizza.")
```

## 2. Variables

A variable is a container used to store data. They behave exactly like the value they contain. Python has four primary basic data types:

- Strings (`str`): A series of text characters.
- Integers (`int`): Whole numbers.
- Floats (`float`): Decimal numbers.
- Booleans (`bool`): True or False values, often used for conditional logic.

```python
# String
first_name = "Bro"
food = "pizza"

# Integer
age = 21
quantity = 3

# Float
price = 19.99
gpa = 3.2

# Boolean
is_student = True
is_online = False

print(f"Hello {first_name}, you are {age} years old.")
print(f"Your GPA is {gpa}. Are you a student? {is_student}")
```

## 3. Type Casting

Type casting is the process of converting a variable from one data type to another. This is especially useful when you need to perform math on a number that is currently formatted as a string, or when you want to concatenate a number with a string.

```python
name = "Bro Code"
age = 21
gpa = 3.2
is_student = True

# Explicit Type Casting
gpa_int = int(gpa)      # Converts 3.2 to 3 (truncates the decimal)
age_float = float(age)  # Converts 21 to 21.0
age_str = str(age)      # Converts 21 to "21"

print(type(gpa_int))    # Output: <class 'int'>
print("I am " + age_str + " years old.") # String concatenation
```

## 4. User Input

The `input()` function prompts the user to enter data via the console.

**Important:** The `input()` function always returns a string. If you need the user to input a number for math, you must type cast it immediately.

```python
name = input("What is your name?: ")
# Type casting the string input directly to an integer
age = int(input("How old are you?: ")) 

age = age + 1 # Doing math with the input

print(f"Hello {name}!")
print(f"Next year you will be {age} years old.")
```

## 5. Arithmetic & Math

Python can perform standard mathematical operations using arithmetic operators and built-in functions. For more advanced math, you can import the `math` module.

### Basic Operators

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Integer/Floor Division: `//` (drops the decimal)
- Modulo: `%` (returns the remainder)
- Exponent: `**`

```python
friends = 10
friends = friends + 1   # Addition
friends += 1            # Augmented assignment (same as above)
friends **= 2           # Exponent (friends squared)
remainder = friends % 3 # Useful for checking odd/even

print(remainder)
```

### Math Functions

```python
import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))          # Output: 3
print(math.ceil(pi))      # Output: 4 (rounds up)
print(math.floor(pi))     # Output: 3 (rounds down)
print(abs(-14))           # Output: 14 (absolute value)
print(pow(pi, 2))         # Output: 9.8596 (base, exponent)
print(math.sqrt(9))       # Output: 3.0
print(max(x, y, z))       # Output: 3
```

## 6. If Statements

If statements allow your code to make decisions. The code block indented under the `if` statement will only execute if the condition evaluates to `True`. You can chain conditions using `elif` (else if) and provide a fallback using `else`.

```python
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You must be 18+ to sign up.")
```

## 7. Logical Operators

Logical operators are used to evaluate multiple conditions simultaneously.

- `and`: Both conditions must be `True`.
- `or`: At least one condition must be `True`.
- `not`: Inverts the condition (`True` becomes `False`, `False` becomes `True`).

```python
temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today.")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today.")
    print("Stay inside!")

# Using not
is_raining = True
if not is_raining:
    print("It is clear outside.")
else:
    print("Bring an umbrella.")
```

## 8. Conditional Expressions (Ternary Operator)

Conditional expressions offer a one-line shortcut for simple `if-else` statements. They are great for assigning a value to a variable based on a condition without writing multiple lines of code.

**Syntax:** `X if condition else Y`

```python
age = 20
# Assign "Adult" if age >= 18, otherwise assign "Child"
status = "Adult" if age >= 18 else "Child"
print(status)

# Print directly
temperature = 35
print("It's Hot" if temperature > 30 else "It's Cold")
```

## 9. String Methods

Python provides many built-in methods to manipulate strings. These methods do not permanently change the original string unless you reassign it.

```python
name = "bro Code"

print(len(name))          # Output: 8 (Length of the string, including spaces)
print(name.capitalize())  # Output: Bro code (Capitalizes first letter only)
print(name.upper())       # Output: BRO CODE
print(name.lower())       # Output: bro code
print(name.isdigit())     # Output: False (Checks if string contains ONLY numbers)
print(name.isalpha())     # Output: False (Checks if string contains ONLY alphabetical chars. Space makes it False)
print(name.count("o"))    # Output: 2 (Counts occurrences of a character)
print(name.replace("o", "a")) # Output: bra Cade
```

## 10. String Indexing

Indexing allows you to access individual characters or a sequence of characters within a string.

**Syntax:** `[start : stop : step]`

- Indexes in Python start at `0`.
- The stop index is exclusive (it stops right before that index).

```python
name = "Bro Code"

# Accessing single characters
first_char = name[0]      # "B"
last_char = name[-1]      # "e" (Negative indexing starts from the end)

# Slicing
first_name = name[0:3]    # "Bro" (Starts at 0, stops before 3)
last_name = name[4:]      # "Code" (Starts at 4, goes to the end)

# Stepping
every_other = name[0:8:2] # "BoCd" (Skips every 2nd character)
reversed_name = name[::-1]# "edoC orB" (Common trick to reverse a string)

print(first_name)
print(reversed_name)
```

## 11. Format Specifiers

Format specifiers define how values should be displayed within f-strings. They are highly useful for displaying currency, rounding decimals, or aligning text in tables.

**Syntax:** `{value:flags}`

```python
price1 = 3.14159
price2 = -987.65
price3 = 12000.50

# Rounding to 2 decimal places (f)
print(f"Price 1 is ${price1:.2f}")  # $3.14

# Adding commas as thousand separators (,)
print(f"Price 3 is ${price3:,}")    # $12,000.5

# Padding and Alignment
# Allocate 10 spaces, align left (<), right (>), or center (^)
print(f"[{price1:<10}]")  # [3.14159   ] Left justify
print(f"[{price1:>10}]")  # [   3.14159] Right justify
print(f"[{price1:^10}]")  # [ 3.14159  ] Center align

# Combining specifiers (comma separator and 2 decimal places)
print(f"Total: ${price3:,.2f}")     # $12,000.50
```