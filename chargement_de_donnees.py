########## Lire et ecrire des données en format texte ########
import pandas as pd 
import numpy as np
chemin = "D:/Etude/pandas/es1.csv"

# délimiteur est la virgule -> pd.read_csv()
df = pd.read_csv(chemin)
print(df)   

# avec pd.read_table -> on spécifie le délimiteur 
df = pd.read_table(chemin, sep = ',')
print(df)

chemin2 = "D:/Etude/pandas/es2.csv"

# si le fichier n'a pas une ligne d'entete 
df2 = pd.read_csv(chemin2, header = None) 
print(df2)

# pour renomer les colonne d'un DataFrame
df2 = pd.read_csv(chemin2, names = ['a', 'b', 'c', 'd', 'message'])
print(df2)

# utiliser la colonne message comme index pour le Dataframe
names = ['a', 'b', 'c', 'd', 'message']
df2 = pd.read_csv(chemin2, names = names, index_col = 'message' )
print(df2)

# former un index hiérarchique à partir de plusieurs colonnes
chemin3 = "D:/Etude/pandas/csv_mindex.csv"
df3 = pd.read_csv(chemin3, index_col = ['key1', 'key2'])
print(df3)

# si la table se présente sans délimiteur fixe 
chemin4 = "D:/Etude/pandas/es3.txt"
df4 = pd.read_table(chemin4, sep = '\s+')
print(df4)
list(open(chemin4))

# pour sauter des ligne 
chemin5 = "D:/Etude/pandas/es4.csv"
df5 = pd.read_csv(chemin5, skiprows = [0,2,3])
print(df5)
list(open(chemin5))

# traitement des valeurs manquantes 
chemin6 = "D:/Etude/pandas/es5.csv"
df6 = pd.read_csv(chemin6)
print(df6)
list(open(chemin6))
df6.isnull()

# tenir compte d'autres valeurs manquantes 
sentinels = {'message' : ['foo','NA'], 'something' : ['two'], 'c' : ['NULL']}
df6 = pd.read_csv(chemin6, na_values = sentinels)
print(df6)

############### lire les fichiers text en plusieurs morceaux #####
chemin7 = "D:/Etude/pandas/es6.csv"
# lire la totalité de fichier 
df7 = pd.read_csv(chemin7)
print(df7)

# lire seulement un certain nombre de lignes 
df7 = pd.read_csv(chemin7, nrows = 5)
print(df7)

# lire le fichiers en morceaux
df7 = pd.read_csv(chemin7, chunksize = 1000)
print (df7)
tot = pd.Series([])
for piece in df7:
    tot = tot.add(piece['key'].value_counts(), fill_value = 0)

tot = tot.order(ascending = False)
print(tot)

############## ecrire des donnees dans un format texte ##########
data = pd.read_csv(chemin6)
print(data)

# ecrire les donnees en sortie dans un fichier avec la virgule comme séparateur
data.to_csv("D:/Etude/pandas/out.csv")
list(open("D:/Etude/pandas/out.csv"))

# ecrire avec un autre séparateur 
import sys
data.to_csv(sys.stdout, sep = '|') 

# modifier la representation des valeurs manquante de chaine de caractère vides à autre chose 
data.to_csv(sys.stdout, na_rep = 'NULL')

# supprimer les étiquettes des lignes et des colonnes 
data.to_csv(sys.stdout, index = False, header = False)

# ecrire seulement un sous ensemble de colonne dans l'ordre de notre choix
data.to_csv(sys.stdout, index = False, columns = ['c','b','a'])

# ecrire un Series
dat = pd.date_range('1/1/2000', periods = 7, freq = 'D')
print(dat)
ts = pd.Series(np.arange(7), index = dat)
print(ts)

ts.to_csv("D:/Etude/pandas/ts_out.csv")
list(open("D:/Etude/pandas/ts_out.csv"))

################## Travailler à la main avec des formats délimités #######################
chemin8 = "D:/etude/pandas/es7.csv"
df8 = pd.read_csv(chemin8) # erreur ligne 3 à 4 valeurs
# fichier avec un délimiteur à un seul caractère 
import csv
f = open("D:/Etude/pandas/es7.csv")
reader = csv.reader(f)
print(reader)















#################### Données JSON ###############################3
import json
chemin9 = "D:/etude/pandas/es8.json"
df9 = json.loads(chemin9)

df9 = pd.read_json(chemin, lines = True)
print(df9)

print("smail")





















