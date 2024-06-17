import pandas as pd

#ATTENTION, UTILISER CE PRGRAMME UNIQUEMENT AVEC LES CSV COMPATIBLES

# Lire le fichier CSV dans un DataFrame

file_name = 'individual-men-final-round' #sans l'extension

table = pd.read_csv('data/' + file_name + '.csv')

match_id = 1
idev = 2
manche_id = 3

table.columns = ['Match','Date/Time','Competitor','NOC','Result','Competitor2','NOC']

def separer_nom_prenom(nom_complet):
    parties = nom_complet.split(' ')
    prénom = parties[0]
    nom = ' '.join(parties[1:])
    return pd.Series([prénom, nom])

# Appliquer la fonction à la colonne 'nom_complet' et créer deux nouvelles colonnes
table[['Prenom1', 'Nom1']] = table['Competitor'].apply(separer_nom_prenom)
table[['Prenom2', 'Nom2']] = table['Competitor2'].apply(separer_nom_prenom)

print("DataFrame avec les colonnes séparées:")
print(table)

with open('queries/'+file_name+'.sql', 'w', newline='', encoding='utf-8') as sqlfile:
    for index, row in table.iterrows():
        athlete1_query = f"(SELECT idAthlete FROM athlete WHERE nomAthlete = '{row["Nom1"]}' AND prenomAthlete = '{row["Prenom1"]}') "
        athlete2_query = f"(SELECT idAthlete FROM athlete WHERE nomAthlete = '{row["Nom2"]}' AND prenomAthlete = '{row["Prenom2"]}') "

        query = f"INSERT INTO match_individuel VALUES ({match_id}, {idev}, {manche_id}, {athlete1_query}, {athlete2_query}, '{row['Result']}');"
        sqlfile.write(query + '\n')