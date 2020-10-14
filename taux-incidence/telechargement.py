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

for dep in depBFC:
    df4 = df3[df3["dep"] == dep]
#    df4["P_decale"] = df4["P"].shift(periods=-3)
    df4["positif_7j"] = df4["P"].rolling(7).sum()
    df4["taux_incid_7j"] = df4["positif_7j"]/df4["pop"]*100000
    df4.to_csv(dep+"_incidence7j.csv", index = False)