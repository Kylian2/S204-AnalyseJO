import pandas as pd

#ATTENTION, UTILISER CE PRGRAMME UNIQUEMENT AVEC LES CSV COMPATIBLES

# Lire le fichier CSV dans un DataFrame

file_name = 'individual-men-round-three' #sans l'extension

table = pd.read_csv('data/' + file_name + '.csv')

id_match = "(SELECT COUNT(*) FROM match_individuel)"
#idev = 90016771
manche_id = 2

table.columns = ['Match','Date/Time','Competitor','NOC','Result','Competitor2','NOC']

def separer_nom_prenom(nom_complet):
    parties = nom_complet.split(' ')
    prénom = parties[0]
    nom = ' '.join(parties[1:])
    return pd.Series([prénom, nom])

print("DataFrame avec les colonnes séparées:")
print(table)

with open('queries/'+file_name+'.py', 'w', newline='', encoding='utf-8') as sqlfile:
    for index, row in table.iterrows():

        query = f"INSERT INTO match_individuel VALUES ({id_match}, {"{idev}"}, {"{id_manche}"}, {row['Competitor']}, {row['Competitor2']}, '{row['Result']}')"
        commande = f'curseur.execute(f"{query}")'
        sqlfile.write(commande + '\n')