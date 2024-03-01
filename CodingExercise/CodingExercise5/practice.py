member = input("Please enter a new member: ")

file = open('members.txt','r')
members = file.readlines()
file.close()

members.append(member)
file = open('members.txt', 'w')
file.writelines(members)
file.close()
