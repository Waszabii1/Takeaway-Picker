from bs4 import BeautifulSoup

import requests

import random
 
restaurants = dict()

groceries = dict()

def cuisine_asker(): #asks if they want a specific cuisine of food, goes through the list and adds it to the url string if they want it
    global cuisine_choices
    cuisine_choices = str()
    question = input("Want to pick between cuisines? (Y/N)  ").upper()
    if question == "Y":
        for i in cuisine_list:
            print("If you are happy with your cuisine choices type stop")
            question = input(f"Do you want {str(i)} food? (Y/N)  ").upper()
            if question == "STOP":
                break
            if question == "Y":
                if len(cuisine_choices) == 0:
                    i = str(i).lower().replace(" ","+")
                    cuisine_choices += i
                else:
                    i = str(i).lower().replace(" ","+")
                    cuisine_choices += f"&cuisine={i}"
            else:
                pass
        
    else:
        print("Okay. Will generate a random restaurant from all cuisines")

 
def list_maker(postcode):

    url_main = f'https://deliveroo.co.uk/restaurants/london/westminster?postcode={postcode}&cuisine={cuisine_choices}&collection=all-restaurants'

    result_main = requests.get(url_main)

    doc_main = BeautifulSoup(result_main.text, "html.parser")

    tags_main = doc_main.find_all("a")

    for tag in range(5, (len(tags_main) - 28)):  # removes Nones and Social Medias, gets list of all places

        place = tags_main[tag].get("aria-label")

        url = tags_main[tag].get("href")

        try:

            restaurants.update({place : url})

        except TypeError:

            pass
    
    url_groceries = f'https://deliveroo.co.uk/restaurants/london/westminster?postcode={postcode}&cuisine=grocery&collection=all-restaurants'

    result_groc = requests.get(url_groceries)

    doc_groc = BeautifulSoup(result_groc.text, "html.parser")

    tags_groc = doc_groc.find_all("a")

    for tag in range(5, (len(tags_groc) -28)):  # removes Nones and Social Medias, gets list of groceries

        place = tags_groc[tag].get("aria-label")

        url = tags_groc[tag].get("href")

        try:

            groceries.update({place : url})

        except TypeError:

            pass

    grocery_remover(restaurants, groceries)

 

def grocery_remover(restaurants, groceries):

 

    for val in groceries: #removes groceries from main list

      if val in restaurants:

        restaurants.pop(val)
    if len(restaurants) == 0:
        print(f"No available deliveroo restaurants in {postcode}")
    else:
     pick(restaurants)

 

 

 

def pick(restaurants):

    rest = key, val = random.choice(list(restaurants.items()))

    amount = len(restaurants)

    if amount == 1:

        print("Hopefully you like this")

        output = print(f"Out of {amount} restaurants, the random restaurant for {postcode} is {key} \nURL is deliveroo.co.uk{val}")

    else:

        output = print(f"Out of {amount} restaurants, the random restaurant for {postcode} is {key} \nURL is deliveroo.co.uk{val}")
                       
        restaurants.pop(key, val)

        re_roll(restaurants)

   

def re_roll(restaurants):

    question = input("Want to pick again? (Y/N)").upper()

    if question == "Y":

        pick(restaurants)

    else:

        print("Enjoy your meal!")

 

 

if __name__ == '__main__':

    postcode = ""

    cuisine_list = [
"Afternoon tea", "All day breakfast", "American", "Asian", 
"Asian Fusion", "Breakfast", "British", "Brunch", 
"Café", "Chinese","Drinks", "French","Healthy", 
"Indian", "Italian", "Japanese", "Korean", 
"Lebanese", "Mediterranean", "Middle Eastern", "Thai", "Turkish"]
    
    cuisine_asker()

    while len(postcode) <6:

        postcode = input(str.strip(("Please enter a valid postcode:  "))).upper()

        if len(postcode) == 7 or 6:

          list_maker(postcode)