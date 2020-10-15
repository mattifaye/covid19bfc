# coding: utf-8
import pandas as pd

#Import fichiers
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675", sep=";", dtype={"dep":object})

# Description filtre
depBFC = ["21","25","39","58","70","71","89","90"]
age = ["0"]

# Filtre données BFC et toutes classes d'âge
df = df[df["dep"].isin(depBFC) & df["cl_age90"].isin(age)]
df["taux_positivite_quotidien"] = df["P"]/df["T"]*100

# Calcul taux de positivité sur sept jours glissants par département
for dep in depBFC:
    df2 = df[df["dep"] == dep]
    df2["positif_7j"] = df2["P"].rolling(7).sum()
    df2["tests_7j"] = df2["T"].rolling(7).sum()
    df2["taux_incid_7j"] = df2["positif_7j"]/df2["tests_7j"]*100
    df2.to_csv(dep+"_positivite7j.csv", index = False)
    
df_21 = pd.read_csv("21_positivite7j.csv")
df_25 = pd.read_csv("25_positivite7j.csv")
df_39 = pd.read_csv("39_positivite7j.csv")
df_58 = pd.read_csv("58_positivite7j.csv")
df_70 = pd.read_csv("70_positivite7j.csv")
df_71 = pd.read_csv("71_positivite7j.csv")
df_89 = pd.read_csv("89_positivite7j.csv")
df_90 = pd.read_csv("90_positivite7j.csv")

# Regroupement dans un seul fichier et export
df_bfc = pd.concat([df_21,df_25,df_39,df_58,df_70,df_71,df_89,df_90])
df_bfc["dep_ok"] = df_bfc["dep"].replace({21:"Côte-d'Or",25:"Doubs",39:"Jura",58:"Nièvre",70:"Haute-Saône",71:"Saône-et-Loire",89:"Yonne",90:"Territoire de Belfort"})
df_bfc.to_csv("bfc_positivite7j.csv",index=False)