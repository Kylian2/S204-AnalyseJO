import pandas as pd

#ATTENTION, UTILISER CE PRGRAMME UNIQUEMENT AVEC LES CSV COMPATIBLES

# Lire le fichier CSV dans un DataFrame

file_name = 'individual-men-ranking-round' #sans l'extension

table = pd.read_csv('data/' + file_name + '.csv')

id_resultat = "(SELECT COUNT(*)+1 FROM resultat)"
id_resultat_for_perf = "(SELECT COUNT(*) FROM resultat)"
#idev = 90016771
#manche_id = 2

def separer_nom_prenom(nom_complet):
    parties = nom_complet.split(' ')
    prénom = parties[0]
    nom = ' '.join(parties[1:])
    return pd.Series([prénom, nom])

print(table)
i=0
with open('queries/'+file_name+'.py', 'w', newline='', encoding='utf-8') as sqlfile:
    for index, row in table.iterrows():

        query1 = f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4) VALUES ({id_resultat},{"{idev}"}, {"{id_manche}"}, '{row['Points']}', '{row['Targets Hit']}', '{row['10s']}', '{row['9s']}')"
        commande1 = f'curseur.execute(f"{query1}")'
        query2 = f"INSERT INTO performance_individuelle VALUES ({"{idev}"}, {"{id_manche}"}, {row['Competitor']}, '{row['Points']}', 'Points', null, {id_resultat_for_perf})"
        commande2 = f'curseur.execute(f"{query2}")'
        sqlfile.write(commande1 + '\n')
        sqlfile.write(commande2+ '\n\n')
        i+=1

print(i)