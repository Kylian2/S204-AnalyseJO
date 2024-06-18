import requests
from bs4 import BeautifulSoup
import csv

#Url for men : https://www.olympedia.org/results/41079
#Url for women : https://www.olympedia.org/results/41175

#File for men : pages_web/Olympedia – Individual, Men.html
#File for women : pages_web/Olympedia – Individual, Women.html

fichier = 'pages_web/Olympedia – Individual, Men.html'
dossier_csv = "data/"

with open(fichier, 'r', encoding='utf-8') as file:
    content = file.read()  

soup = BeautifulSoup(content, 'html.parser')

def remove_useless_columns(table):
    if not table or not table[0]:
        return table

    # Trouver les index des colonnes vides
    empty_columns = []
    for i in range(len(table[0])):
        if table[0][i] == '':
            empty_columns.append(i)

    # Supprimer les colonnes vides de chaque ligne
    for i in reversed(empty_columns):
        for row in table:
            row.pop(i)

    return table

def getId(links):
    champs = links.split('/')
    return champs[len(champs)-1]

# Permet de distinguer l'évenement, servira pour le nom du ficher csv
event = soup.find('h1')
event = (((event.get_text(strip=True)).replace(" ", "-")).replace(",","")).lower()

titles = soup.find_all('h2')

for title in titles:
    # Trouver le tableau des scores après chaque type de manche 
    # Il est contenu dans un table avec la classe table-striped
    table = title.find_next('table', class_='table-striped')
    if table:
        
        table_data = list()
        # Parcourir les lignes du tableau
        for ligne in table.find_all('tr'):
            ligne_data = list()
            for i, colonne in enumerate(ligne.find_all(['th', 'td'])):
                # Extraire l'URL dans la deuxième colonne (index 1)
                    link = colonne.find('a', href=True)
                    if link:
                        ligne_data.append(getId(link['href']))
                    else:
                        ligne_data.append(colonne.get_text(strip=True))

            table_data.append(ligne_data)     
        csv_file_name = ((title.get_text(strip=True)).replace(" ", "-")).lower() + '.csv'

        table_data = remove_useless_columns(table_data)

        with open(dossier_csv+event+'-'+csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(table_data)

    else:
        print(f"Aucun tableau trouvé après le titre: {title.get_text(strip=True)}")
