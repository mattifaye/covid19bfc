import pandas as pd

#Import fichiers
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675", sep=";", dtype={"dep":object})
df2 = pd.read_csv("popBFC.csv", dtype={"dep":object})

# Filtres
depBFC = ["21","25","39","58","70","71","89","90"]
age = ["0"]

#Fusion des deux sources de données
df = df[df["dep"].isin(depBFC) & df["cl_age90"].isin(age)]
df3 = pd.merge(df, df2, on="dep")

# Calcul taux d'incidence quotidien
df3["taux_incidence_quot"] = df3["P"]/df3["pop"]*100000

# Calcul taux d'incidence par département sur sept jours glissants
for dep in depBFC:
    df4 = df3[df3["dep"] == dep]
    df4["positif_7j"] = df4["P"].rolling(7).sum()
    df4["taux_incid_7j"] = df4["positif_7j"]/df4["pop"]*100000
    df4.to_csv(dep+"_incidence7j.csv", index = False)

df_21 = pd.read_csv("21_incidence7j.csv")
df_25 = pd.read_csv("25_incidence7j.csv")
df_39 = pd.read_csv("39_incidence7j.csv")
df_58 = pd.read_csv("58_incidence7j.csv")
df_70 = pd.read_csv("70_incidence7j.csv")
df_71 = pd.read_csv("71_incidence7j.csv")
df_89 = pd.read_csv("89_incidence7j.csv")
df_90 = pd.read_csv("90_incidence7j.csv")

# Regroupement de toutes les données dans un seul fichier
df_bfc = pd.concat([df_21,df_25,df_39,df_58,df_70,df_71,df_89,df_90])
df_bfc["dep_ok"] = df_bfc["dep"].replace({21:"Côte-d'Or",25:"Doubs",39:"Jura",58:"Nièvre",70:"Haute-Saône",71:"Saône-et-Loire",89:"Yonne",90:"Territoire de Belfort"})
df_bfc.to_csv("bfc_incidence7j.csv",index=False)