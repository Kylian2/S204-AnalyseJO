import pandas as pd

#ATTENTION, UTILISER CE PRGRAMME UNIQUEMENT AVEC LES CSV COMPATIBLES

# Lire le fichier CSV dans un DataFrame

file_name = 'individual-men-individual,-men' #sans l'extension

table = pd.read_csv('data/' + file_name + '.csv')

id_match = "(SELECT COUNT(*) FROM match_individuel)"

def separer_nom_prenom(nom_complet):
    parties = nom_complet.split(' ')
    prénom = parties[0]
    nom = ' '.join(parties[1:])
    return pd.Series([prénom, nom])

print("DataFrame avec les colonnes séparées:")
print(table)

with open('queries/'+file_name+'.py', 'w', newline='', encoding='utf-8') as sqlfile:
    for index, row in table.iterrows():

        query = f"BEGIN\n ajouter_resultat_individuel({"{idev}"}, {row['Competitor']}, '{row['NOC']}', '{row['Pos']}'); \n END;"
        commande = f'curseur.execute(f"""{query}""")'
        sqlfile.write(commande + '\n')