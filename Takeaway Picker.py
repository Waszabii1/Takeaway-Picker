from bs4 import BeautifulSoup
import requests
import random


def main():
    url = f'https://deliveroo.co.uk/restaurants/london/westminster?postcode={postcode}&collection=all-restaurants'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    tags = doc.find_all("a")

    resturants = []
    for tag in range(5, (len(tags) - 28)):  # removes Nones and Social Medias
        individual = tags[tag].get("aria-label")
        try:
            resturants.append(individual)
        except TypeError:
            pass
    choice = random.choice(resturants)
    amount = len(resturants)
    print("Out of " + str(amount) + " restaurants, the random restaurant for " + postcode + " is " + choice)


if __name__ == '__main__':
    postcode = ""
    while len(postcode) != 6:
        postcode = input("What is your postcode? ")
        if len(postcode) != 6:
            print("Please enter a valid postcode")
    main()
