from BONUS.convert14 import convert
from BONUS.parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("kids is too small")
else:
    print("kids can use it. ")

