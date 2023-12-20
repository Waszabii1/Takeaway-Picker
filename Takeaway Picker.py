from bs4 import BeautifulSoup
import requests
import random

restaurants = dict()


def list_maker():
    url = f'https://deliveroo.co.uk/restaurants/london/westminster?postcode={postcode}&collection=all-restaurants'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    tags = doc.find_all("a")

    for tag in range(5, (len(tags) - 28)):  # removes Nones and Social Medias
        restaurant = tags[tag].get("aria-label")
        url = tags[tag].get("href")
        try:
            restaurants.update({restaurant : url})
        except TypeError:
            pass
    
    return restaurants

def pick():
    rest = key, val = random.choice(list(restaurants.items()))
    amount = len(restaurants)
    print("Out of " + str(amount) + " restaurants, the random restaurant for " + postcode + " is " + str(rest[0]) +  " , URL is deliveroo.co.uk" + str(rest[1]))
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


