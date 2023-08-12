#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
newString = str[str.find("object-oriented programming"):str.find("object-oriented programming") + len("object-oriented programming")]
print(f"{newString} with Python")
