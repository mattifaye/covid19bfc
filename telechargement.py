# -*-coding:Latin-1 -*
import pandas as pd

url = "https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"
dptBFC = ["21", "25", "39", "58", "70", "71", "89", "90"]

# On importe les données depuis l'url
source = pd.read_csv(url,sep=";")

# On filtre ce qui nous intéresse
filtre = source[(source["sexe"] == 0) & (source["dep"].isin(dptBFC))].filter(["jour","dep","dc","rea","hosp","rad"])

# On renomme les colonnes pour que ce soit plus lisible
donneesOK = filtre.rename(index=str, columns={"jour":"Date","dep":"Code","hosp":"Personnes hospitalisées","rea":"Personnes en réanimation","rad":"Personnes de retour à domicile (cumul)","dc":"Personnes décédées (cumul)"})

# On créé le fichier bfc et on l'enregistre
bfc = pd.pivot_table(donneesOK, values=["Personnes décédées (cumul)","Personnes en réanimation","Personnes hospitalisées"], index=["Date"], aggfunc="sum")
bfc.to_csv("bfc.csv")

# On créé le fichier retourdom et on l'enregistre
retourdom = pd.pivot_table(donneesOK, values=["Personnes de retour à domicile (cumul)","Personnes décédées (cumul)"], index=["Date"], aggfunc="sum")
retourdom.to_csv("retourdom.csv")

# On trouve la valeur maximale dans tous les départements et on l'enregistre
maximum = ((source[(source["sexe"] == 0) & (source["dep"].isin(dptBFC))].filter(["dc","rea","hosp"]).max()).max()+10)
f = open("max.csv", "w")
f.write(str(maximum))
f.close()

# On récupère les décès pour la carte et on les enregistre
sourcecarte = pd.read_csv("sourcecarte.csv",sep=",",dtype={"Code": object})
decespardpt = pd.pivot_table(donneesOK, values=["Personnes décédées (cumul)"], index=["Code"], aggfunc="last")
carte = pd.merge(sourcecarte, decespardpt, left_on="Code", right_index= True, how="outer")
carte.to_csv("carte.csv", index= False)

# On créé un fichier pour chaque département et on les enregistre
for dpt in dptBFC:
    filtre = source[(source["sexe"] == 0) & (source["dep"] == dpt)].filter(["jour","dep","dep","dc","rea","hosp"])
    donneesOK = filtre.rename(index=str, columns={"jour":"Date","dep":"Code","hosp":"Personnes hospitalisées","rea":"Personnes en réanimation","rad":"Personnes de retour à domicile (cumul)","dc":"Personnes décédées (cumul)"})
    donneesOK.to_csv(dpt+".csv", index = False)