# ==========================================
# SESSION ONE: INTRODUCTION TO PYTHON
# ==========================================

print("I hate pizza")


# ==========================================
# 1. VARIABLES & DATA TYPES
# ==========================================
# A variable is a container used to store data. They behave exactly like the value they contain.
# Python has four primary basic data types: strings, integer, Float, Boolean

name = "Jhon"         # String
age = 22              # Integer
height = 5.7          # Float
is_available = True   # Boolean

print(name, age, height, is_available)
print(f"I am {name} and I have {age} years old and height {height} meters away.")


# ==========================================
# 2. TYPE CASTING
# ==========================================
# Type casting is the process of converting a variable from one data type to another datatype

age = 21
print(age)

kolagach = float(age)
print(kolagach)

age_str = str(age)
print(age_str)

print(type(age_str))
print(type(age))


# ==========================================
# 3. USER INPUT
# ==========================================
# (Note: Commented out to prevent pausing the script)

# name = str(input("Enter your name:"))
# age= int(input("Enter your age: "))
# print(age)

# print(f"My name is {name}, and my age is {age+12}")


# ==========================================
# 4. ARITHMETIC AND MATH
# ==========================================

a = 100
b = 12

sum = a + b
print(sum)

sub = a - b
print(sub)

mul = a * b
print(mul)

div = a / b
print(div)


# --- Convert negative into positive ---
import math

print(abs(34))
print(abs(sub))             # positive
print(round(div))           # 8
print(math.ceil(div))       # 8.3333333333334 -> 9
print(math.floor(div))      # 8.33333333334 -> 8
print(pow(3,2))             # 9
print(int(math.sqrt(100)))  # 10
print(max(1,2,3,34))        # 34


# ==========================================
# 5. CONDITIONAL STATEMENTS (IF/ELSE)
# ==========================================

if(age>18):
    print("You are older than 18.")
    if(age>18):
          print("You are older than 18.")
elif(age<18):
    print("You are younger than 18.")


# ==========================================
# 6. STRING METHODS & SLICING
# ==========================================

name = "yousuf is good Man"

print(len(name))            # 6
print(name.capitalize())    # Yousuf ali apel is a good guy
print(name.upper())         # YUSUF
print(name.lower())
print(name.count('x'))      # 3
print(name.replace("o","a"))

# --- Indexing ---
first_char = name[6]
print(first_char)

# --- Slicing ---
s = name[3:6]
print(s)