import requests
import pyfiglet

again = "y"

while again == "y" or again == "yes":
    # the website that this program gets the jokes from
    url = "https://icanhazdadjoke.com/search"

    # initializing a list used for checking user input
    nums = []
    for x in range(30):
        nums.append(str(x + 1))

    # prints awesome title
    print(pyfiglet.figlet_format(text="DAD JOKE MACHINE"))

    # asks the user for what term the API searches for
    joke = str(input("What do you want the joke to be about: "))
    while not joke:     # checks if the user typed anything
        joke = str(input("Please type what you want the joke to be about: "))
    limit = input("How many jokes do you want: ")   # asks user how many jokes they want
    while limit not in nums:    # if limit is in the list
        limit = input("Please type a number (non-letter format): ")
    limit = int(limit)    # changes the limit from an int to a str

    # requests the certain parameters in the headers
    res = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": joke, "limit": limit}   # passing parameters
    )

    # changes the websites api to python code
    data = res.json()

    # lots of checks so that it will print the right verbiage
    if limit == 1 and len(data["results"]) == 1:
        print("printing 1 joke...")
    elif limit <= len(data["results"]):
        print(f"printing {limit} jokes...")
    elif len(data["results"]) == 1:
        print("only found 1 joke...")
    elif limit > len(data["results"]) != 0:
        print(f"only found {len(data['results'])} jokes...")
    else:
        print("I have no jokes about that")
    print()

    # iterates through the list from the api
    for joke in data["results"]:
        print(joke["joke"])
        print()

    again = input("Would you like to go again ('yes' or 'no'): ")
    while again != "yes" and again != "no":
        again = input("Please say 'yes' or 'no': ")
