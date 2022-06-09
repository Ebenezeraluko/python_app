"""import keyword

#how to create variables and store values in them
first_name = "Ebenezer"
last_name = "Aluko"
middle_name = "Temitope"
full_name = "Ebenezer Aluko"
age = 16
sex = "Male"
isAdult = True

#how to print a variable
print("First name: " +(first_name))
print("Middle name: " + (middle_name))
print(last_name)
print(full_name)
print(age)
print(sex)
print(isAdult)
 
#Multiline and formatting
name = "Adeolu"
greetings = """
    #Hello {}
    #How are you?
    #It's really nice seeing you again!
"""
print(greetings.format(name))

#Reserved keywords
print(keyword.kwlist)

#input functions
name = input("What is your name? ")
age = input("How old are you? ")
course = input("What course do you study? ")
height = input("What is your height? ")
isSex = input("Are you a male? ")

print()
print("My detail")
print("What is your name? "+name)
print("How old are you? "+age+ " " "years")
print("What course do you study? "+course)
print("What is your height? "+height+ "m")
print("Are you a male? "+isSex)

#import math
import math
digit = 4.1
print(math.floor(digit))
print(math.ceil(digit))
print(math.sqrt(digit))
print(pow(digit, 2))

#Arithmetic operators
print(10+2)
print(10-2)
print(10/2)
print(10*2)
print(2**2)
print(10%2)

#Comparison operator
print(2>3)
print(2 >= 3)
print(2 <= 3)
print(2 < 3)
print(2 == 3)
print(2 != 3)
 
#Logical operator
print(10 > 2 and 2 >= 4)
print(3 == 5 or 6 < 7) 
print(8 >= 2 
      and 2 >= 4 
      or "A" == "B" )
print(not("Ebenezer" == "Temitope"))

#If statement
number = 27
if number > 30:
    print("it is ")
else:
    print("it is not!")
    
#ternary statement
number = 28
message = "it is not " if number > 30 else "it is"
print(message)

#List - is with square brackets
fruits = ["mango", "apple", "orange", "pineapple", "cherry"]

#method in list
#fruits.sort()
#fruits.reverse()
#fruits.append("lemon")
#print(len("mango"))
#print("berry" in fruits)

#delete in list
#fruits.clear()
#fruits.remove("apple")
#del fruits[0:3]
print(fruits)

#set is with curly brackets and it is not order guaranteed
fruits_sets = {"apple", "apple", "mango", "guava"}
print(fruits_sets)

#set union| difference- intersection&
letters_a = {"A", "B", "B", "C", "D"}
letters_b = {"A", "B", "E", "E", "F"}

union = letters_a | letters_b
print(f"Union = {union}")

intersection = letters_a & letters_b
print(f"Intersection = {intersection}")

difference = letters_a - letters_b
print(f"Difference = {difference}")"""

#Dictionary
person = {
    "name": "Ebenezer",
    "age": "ageless",
    "address": "Toronto, Canada"
}

"""#methods in dictionary  
print(person["name"])
print(person["age"])
print(person["address"])
print(person.keys())
print(person.values())
print(person.get("name"))
person["address"] = "Ontario, Canada" #to update the address
print(person.items())
print(person)

#for loop
names = ["Adeolu","Temitope","Ebenezer", "Akande"]

for name in names:
    print(name)
    
#loop through dictionary
for key in person:
    print(f"key:{key} value:{person[key]}")"""
    
#Exercise
#sum these values using for loop
result = 0
numbers = [3, 4, 5, 2]

for number in numbers:
    result += number

print(f"Result: {result}")    
















