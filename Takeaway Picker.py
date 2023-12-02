from bs4 import BeautifulSoup
import requests
import random

restaurants = []


def list_maker():
    url = f'https://deliveroo.co.uk/restaurants/london/westminster?postcode={postcode}&collection=all-restaurants'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    tags = doc.find_all("a")

    for tag in range(5, (len(tags) - 28)):  # removes Nones and Social Medias
        individual = tags[tag].get("aria-label")
        try:
            restaurants.append(individual)
        except TypeError:
            pass
    
    return restaurants

def pick():
    amount = len(restaurants)
    choice = random.choice(restaurants)    
    print("Out of " + str(amount) + " restaurants, the random restaurant for " + postcode + " is " + choice)
    re_roll()
    
def re_roll():
    question = input("Want to pick again? (Y/N)")
    global answer
    answer = question.upper()
    if answer == "Y":
        answer = True
    else:
        answer = False
    return answer


if __name__ == '__main__':
    postcode = ""
    while len(postcode) != 6:
        postcode = input("What is your postcode? ")
        if len(postcode) != 6:
            print("Please enter a valid postcode")
    list_maker()
    pick()
    while answer == True:
        pick()
        if answer == False:
          print("Enjoy your meal!")
    
