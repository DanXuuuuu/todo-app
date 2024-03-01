import csv

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))

city = input("Please enter the city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])