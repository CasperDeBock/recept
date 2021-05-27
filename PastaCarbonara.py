import requests
from bs4 import BeautifulSoup

recept = input("Welk recept zoek je? ")

try:
    pagina = requests.get('https://www.ah.be/allerhande/recepten/' + recept)
    soep = BeautifulSoup(pagina.text, 'html.parser')


    names = []
    row = soep.find("ul",class_="recipe-details-content_ingredientList__2OeKP")
    player_name = row.find_all('li')
    for derow in player_name:
        name = derow.find("span",class_="typography_root__3N25D typography_variant-paragraph__377x0 recipe-details-content_ingredientName__3jPk4")
        klein = derow.find('span')
        names.append([klein.text ,name.text])
    print("Recept voor spaghetti carbonara:")

    for naam in names:
        print(naam)
except:
  print("Er zijn geen recepten gevonden die: " + recept + " noemen")



