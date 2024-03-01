import webbrowser

user_team = input("Enter the search term: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + user_team)