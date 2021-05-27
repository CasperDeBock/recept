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
  nieuwpagina = requests.get('https://www.ah.be/allerhande/recepten-zoeken?query=' + recept)
  soep = BeautifulSoup(nieuwpagina.text, 'html.parser')

  voorstellen = []
  row = soep.find("div",class_="column xxlarge-4 large-6 small-12")
  player_name = row.find_all('p')
  for do in player_name:
    name = do.find('span', class_="line-clamp_root__2z9Ng line-clamp_active__2Jlke card-text_titleText__fr9jI card-text_boldTitle__19dpK")
    voorstellen.append(name.text)

  print("Hier zijn enkele andere voorstellen: ")
  print(voorstellen)



