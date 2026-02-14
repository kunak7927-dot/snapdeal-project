# Basic program
print("Hello World")

name = "ABCD"
age = 30

name = "john"
age = 35

x = 2 + 3j
print(name)
print(x)

# Data types
my_list = [1, 2, 3]
my_tuple = (1, 2, 3, 4)
my_set = {2, 5, 7}
my_dict = {"name": "john"}

# Input example
x = input("Enter your name: ")
print(x)
print("Hello " + x)

e = input("Enter your birth year: ")
c = int(e) + 2
print(c)

# Sum of two numbers
x = input("Enter first number: ")
y = input("Enter second number: ")
sum_val = int(x) + int(y)
print(sum_val)

# Tuple count
tup = (10, 33, 45, 54, 45)
print(tup.count(45))

# Function
def great():
    print("hello")

great()

# For loop
for i in range(10):
    print(i)

# List operations
age = [10, 20, 28, 30, 45, 29]
print(age[1])

age.append(50)
age.insert(1, 24)
print(age)
print(len(age))

for a in age:
    if a == 10:
        continue
    print(a)

# While loop
i = 0
while i <= 10:
    print(i)
    i += 1

# String methods
name = "MALATHY"
print(name.islower())
print(name.isupper())
print(name.find("A"))
print(name.replace("A", "E"))
print("T" in name)

# Operators
print(5 + 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)

# Comparison
print(2 == 5)
print(2 == 2)
print(2 != 5)
print(2 > 4 > 3)

# If else
birth_year = 2002
if birth_year > 2000:
    print("new generation")
else:
    print("old generation")