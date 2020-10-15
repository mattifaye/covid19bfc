# coding: utf-8
import pandas as pd

#Import fichiers
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7", sep=";", dtype={"dep":object})

# Description filtre
depBFC = ["21","25","39","58","70","71","89","90"]
sexe = ["0"]

# Filtre données BFC et toutes classes d'âge
df = df[df["dep"].isin(depBFC) & df["sexe"].isin(sexe)]

# Renommage colonnes et départements
df["dep_ok"] = df["dep"].replace({"21":"Côte-d'Or","25":"Doubs","39":"Jura","58":"Nièvre","70":"Haute-Saône","71":"Saône-et-Loire","89":"Yonne","90":"Territoire de Belfort"})
df_ok = df.rename(index=str, columns={"jour":"Date","dep":"Code","hosp":"Personnes hospitalisées","rea":"Personnes en réanimation","rad":"Personnes de retour à domicile (cumul)","dc":"Personnes décédées (cumul)"})

# Export fichier
df_ok.to_csv("bfc_hospitalisations.csv",index=False)