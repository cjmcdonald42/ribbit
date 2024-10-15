print("This is a string")       # \n, \t, \b

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello", name, ". You are", age, "years old.")        # sep=" ", end="\n"

# print("Hello %s. You are %i years old." % (name, age))

greeting = "Hello"      # String() = array of char()

print(type(greeting))
print(greeting[1])
print(greeting[1:3])    # [0]
print(greeting[:3])
print(greeting[-2:])

text = "  Hello, I am 50 years old today.  "
print(text)
print(text.capitalize())      # text.upper()    .lower()    .title()    .isUpper()  .isLower()
print(text.strip())           # text.leftStrip()    .rightStrip()

y = text.find("Hello")
print(y)

z = ["apple", "pears", "banana"]
y = z.index("pears")
print(y)

try:
    y = z.index("kiwi")
except ValueError:
    print("That is not in our list")

x = "Hello Chuck, welcome to Python coding!"
y = x.find("Chuck")
print(y)

y = x.count("to")
print(y)
