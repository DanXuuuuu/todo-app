password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = True
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit


for i in password:
    if i.isupper():
        upper = True

result["upper-case"] = upper

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
print(result.values())