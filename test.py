def greet(massage):
    new_massage = massage.capitalize()
    print("Hey hey")
    return new_massage

user_entry = input("Pleasen enter what you want: ")
greeting = greet(user_entry)
print(greeting)
