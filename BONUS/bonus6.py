contents = ["abc decade",
            "sunny day",
            "sadness"]

filenames = ["abc.txt", "weather.txt", "mood.txt"]

for content, filename in zip(contents, filenames):
    file = open(f'../files/{filename}', 'w')
    file.write(content)