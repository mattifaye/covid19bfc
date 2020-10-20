#coding: utf-8
import pandas as pd

############################
##### TAUX D'INCIDENCE #####
############################

# Import fichiers
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/19a91d64-3cd3-42fc-9943-d635491a4d76", sep=";", dtype={"dep":object})

# Filtres
depBFC = ["21","25","39","58","70","71","89","90"]
age = ["0"]

# Filtre données BFC et toutes classes d'âge
df = df[df["dep"].isin(depBFC) & df["cl_age90"].isin(age)]

# Calcul taux d'incidence quotidien
df["taux_incidence_quot"] = df["P"]/df["pop"]*100000

# Calcul taux d'incidence par département sur sept jours glissants
for dep in depBFC:
    df2 = df[df["dep"] == dep]
    df2["positif_7j"] = df2["P"].rolling(7).sum()
    df2["taux_incid_7j"] = df2["positif_7j"]/df2["pop"]*100000
    df2.to_csv(dep+"_incidence7j.csv",index=False)

df_21 = pd.read_csv("21_incidence7j.csv")
df_25 = pd.read_csv("25_incidence7j.csv")
df_39 = pd.read_csv("39_incidence7j.csv")
df_58 = pd.read_csv("58_incidence7j.csv")
df_70 = pd.read_csv("70_incidence7j.csv")
df_71 = pd.read_csv("71_incidence7j.csv")
df_89 = pd.read_csv("89_incidence7j.csv")
df_90 = pd.read_csv("90_incidence7j.csv")

df_dep = pd.concat([df_21,df_25,df_39,df_58,df_70,df_71,df_89,df_90])
df_dep["dep_ok"] = df_dep["dep"].replace({21:"Côte-d'Or",25:"Doubs",39:"Jura",58:"Nièvre",70:"Haute-Saône",71:"Saône-et-Loire",89:"Yonne",90:"Territoire de Belfort"})
df_dep.to_csv("dep_incidence7j.csv",index=False)

# Calcul taux d'incidence régional sur sept jours glissants
tcd = df.pivot_table(index=["jour"],values=["P","pop"],aggfunc=sum)
tcd["positif_7j"] = tcd["P"].rolling(7).sum()
tcd["taux_incid_7j"] = tcd["positif_7j"]/tcd["pop"]*100000
tcd.to_csv("bfc_incidence7j.csv")

##############################
##### TAUX DE POSITIVITÉ #####
##############################

# Import fichiers
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
    df2["positifs_7j"] = df2["P"].rolling(7).sum()
    df2["tests_7j"] = df2["T"].rolling(7).sum()
    df2["taux_positivite_7j"] = df2["positifs_7j"]/df2["tests_7j"]*100
    df2.to_csv(dep+"_positivite7j.csv", index=False)
    
df_21 = pd.read_csv("21_positivite7j.csv")
df_25 = pd.read_csv("25_positivite7j.csv")
df_39 = pd.read_csv("39_positivite7j.csv")
df_58 = pd.read_csv("58_positivite7j.csv")
df_70 = pd.read_csv("70_positivite7j.csv")
df_71 = pd.read_csv("71_positivite7j.csv")
df_89 = pd.read_csv("89_positivite7j.csv")
df_90 = pd.read_csv("90_positivite7j.csv")

# Regroupement dans un seul fichier et export
df_dep = pd.concat([df_21,df_25,df_39,df_58,df_70,df_71,df_89,df_90])
df_dep["dep_ok"] = df_dep["dep"].replace({21:"Côte-d'Or",25:"Doubs",39:"Jura",58:"Nièvre",70:"Haute-Saône",71:"Saône-et-Loire",89:"Yonne",90:"Territoire de Belfort"})
df_dep.to_csv("dep_positivite7j.csv",index=False)

# Calcul taux d'incidence régional sur 7 jours glissants
tcd = df.pivot_table(index=["jour"],values=["P","T"],aggfunc=sum)
tcd["positifs_7j"] = tcd["P"].rolling(7).sum()
tcd["tests_7j"] = tcd["T"].rolling(7).sum()
tcd["taux_positivite_7j"] = tcd["positifs_7j"]/tcd["tests_7j"]*100
tcd.to_csv("bfc_positivite7j.csv")


############################
##### HOSPITALISATIONS #####
############################

#### Détails par départements ####
# Import fichiers
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7", sep=";", dtype={"dep":object},parse_dates=["jour"])

# Description filtre
depBFC = ["21","25","39","58","70","71","89","90"]
sexe = ["0"]

# Filtre données BFC et toutes classes d'âge
df = df[df["dep"].isin(depBFC) & df["sexe"].isin(sexe)]

# Renommage colonnes et départements
df["dep_ok"] = df["dep"].replace({"21":"Côte-d'Or","25":"Doubs","39":"Jura","58":"Nièvre","70":"Haute-Saône","71":"Saône-et-Loire","89":"Yonne","90":"Territoire de Belfort"})
df_ok = df.rename(index=str, columns={"hosp":"Personnes hospitalisées","rea":"Personnes en réanimation","rad":"Personnes de retour à domicile (cumul)","dc":"Personnes décédées (cumul)"})

# Export fichier
df_ok.to_csv("dep_hospitalisations.csv",index=False)

# Tableau croisé total BFC
tcd = df.pivot_table(index=["jour"],values=["hosp","rea","dc","rad"], aggfunc=sum)
tcd_ok = tcd.rename(index=str, columns={"hosp":"Personnes hospitalisées","rea":"Personnes en réanimation","rad":"Personnes de retour à domicile (cumul)","dc":"Personnes décédées (cumul)"})
tcd_ok["jour_ok"]=tcd.index
tcd_ok.to_csv("bfc_hospitalisations_total.csv",date_format='%Y-%m-%d')


### Synthèse pour la région (dernier jour) ###
# Nouvelles hospitalisations

df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/6fadff46-9efd-4c53-942a-54aca783c30c", sep=";",parse_dates=["jour"])

df = df[df["dep"].isin(depBFC)]

tcd = df.pivot_table(index=["jour"],values=["incid_hosp","incid_rea","incid_dc","incid_rad"],aggfunc=sum)
tcd["jour"] = tcd.index
tcd["date_mois"] = tcd["jour"].dt.month
tcd["date_jour"] = tcd["jour"].dt.day

tcd.last("1D").to_csv("bfc_nouvelles_hospitalisations.csv")


# Total hospitalisations

df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7", sep=";",parse_dates=["jour"])

df = df[df["dep"].isin(depBFC) & df["sexe"].isin(sexe)]

tcd = df.pivot_table(index=["jour"],values=["hosp","rea","dc","rad"],aggfunc=sum)
tcd["jour"] = tcd.index
tcd["date_mois"] = tcd["jour"].dt.month
tcd["date_jour"] = tcd["jour"].dt.day

tcd.last("1D").to_csv("bfc_hospitalisations_jour.csv")

######################
##### METROPOLES #####
######################

# Import fichier
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/61533034-0f2f-4b16-9a6d-28ffabb33a02",sep=";")
epci = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/0fa52fca-4eb3-4786-92f1-6db24273068f",sep=";",encoding="latin")
df = pd.merge(df,epci,left_on="epci2020",right_on="EPCI")

# Filtre
epciBFC = ["242100410"]
age = ["0","65"]

# Application filtre
df = df[df["EPCI"].isin(epciBFC) & df["clage_65"].isin(age)]


df["debut_periode"] = df["semaine_glissante"].str[:10]
df["fin_periode"] = df["semaine_glissante"].str[-10:]
df["clage_ok"] = df["clage_65"].replace({0:"tous âges",65:"65 ans et plus"})

# Renommage
df_ok = df.rename(index=str, columns={"ti":"Taux d'incidence"})

# Export
df_ok.to_csv("epci_incidence7j.csv",index=False)

#########################
##### CLASSES D'AGE #####
#########################

# A faire
