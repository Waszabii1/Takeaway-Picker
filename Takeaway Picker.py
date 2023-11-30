from bs4 import BeautifulSoup
import requests
import random


url = ""     #This is where the url of your postcode inputted in deliveroo goes

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tags = doc.find_all("a")

resturants = []
for tag in range(5, (len(tags)-28)):
    individual = tags[tag].get("aria-label")
    try:
        resturants.append(individual)
    except TypeError:
        pass
choice = random.choice(resturants)
amount = len(resturants)
print("Out of " + str(amount) + " restrurants, the random resturant for XXXXX is " + choice) #XXXXX is city you are in


