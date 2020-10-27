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
df_dep["dep_ok"] = df_dep["dep"].replace({21:"Cote-d'Or",25:"Doubs",39:"Jura",58:"Nievre",70:"Haute-Saone",71:"Saone-et-Loire",89:"Yonne",90:"Territoire de Belfort"})
df_dep.to_csv("dep_incidence7j.csv",index=False)


####### Taux incidence avec accents pour test
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
df_dep.to_csv("dep_incidence7j_accents.csv",index=False)


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
df_dep["dep_ok"] = df_dep["dep"].replace({21:"Cote-d'Or",25:"Doubs",39:"Jura",58:"Nievre",70:"Haute-Saone",71:"Saone-et-Loire",89:"Yonne",90:"Territoire de Belfort"})
df_dep.to_csv("dep_positivite7j.csv",index=False)

# Calcul taux d'incidence régional sur 7 jours glissants
tcd = df.pivot_table(index=["jour"],values=["P","T"],aggfunc=sum)
tcd["positifs_7j"] = tcd["P"].rolling(7).sum()
tcd["tests_7j"] = tcd["T"].rolling(7).sum()
tcd["taux_positivite_7j"] = tcd["positifs_7j"]/tcd["tests_7j"]*100
tcd.to_csv("bfc_positivite7j.csv")


# Chiffres derniers jours taux d'incidence et taux de positivité
df = pd.read_csv("bfc_positivite7j.csv",parse_dates=["jour"],index_col="jour")
df2 = df[["tests_7j","positifs_7j","taux_positivite_7j"]]
df_ok = df2.last("1D")

pos = pd.read_csv("bfc_incidence7j.csv",parse_dates=["jour"],index_col="jour")
pos_ok = pos.last("1D")[["taux_incid_7j"]]

df2 = df_ok.join(pos_ok).T
df2["categorie"] = df2.index
df3 = df2.replace({"tests_7j":"Tests réalisés","positifs_7j":"Tests positifs","taux_positivite_7j":"Pourcentage de tests positifs","taux_incid_7j":"Taux d'incidence"})
df4 = df3.round()
df4.to_csv("bfc_tests_jour.csv",float_format='%.0f')

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

tcd = df.pivot_table(index="jour",values=["incid_hosp","incid_rea","incid_dc","incid_rad"],aggfunc=sum)
tcd2 = tcd[['incid_hosp', 'incid_rea', 'incid_dc', 'incid_rad']].last("1D").T
tcd2["categorie"] = tcd2.index
tcd3 = tcd2.replace({"incid_dc":"Nouveaux décès","incid_hosp":"Nouvelles hospitalisations", "incid_rea":"Nouvelles admissions en réanimation","incid_rad":"Nouveaux retours à domicile"})
tcd3.to_csv("bfc_nouvelles_hospitalisations.csv")

# Total hospitalisations

df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7", sep=";",parse_dates=["jour"])

df = df[df["dep"].isin(depBFC) & df["sexe"].isin(sexe)]

tcd = df.pivot_table(index=["jour"],values=["hosp","rea","dc","rad"],aggfunc=sum)
tcd2 = tcd[['hosp', 'rea', 'dc', 'rad']].last("1D").T
tcd2["categorie"] = tcd2.index
tcd3 = tcd2.replace({"dc":"Décès à l'hôpital (cumul)","hosp":"Personnes actuellement hospitalisées", "rea":"Personnes actuellement en réanimation","rad":"Personnes de retour à domicile (cumul)"})
tcd3.to_csv("bfc_hospitalisations_jour.csv")


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

# Import données hospitalières
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3",sep=";",parse_dates=["jour"])
df = df[df["reg"] == 27]
df = df[df["cl_age90"] != 0]

df2 = df.pivot_table(index=["jour"],columns="cl_age90",values=["dc","hosp","rea"]).last("1D")
df3 = df2.rename(columns={"hosp":"Hospitalisations","rea":"Réanimations","dc":"Décès (cumul)"})
hosp = df3.rename(columns={0:"tous",9:"de 0 à 9 ans",19:"de 10 à 19 ans",29:"de 20 à 29 ans",39:"de 30 à 39 ans",49:"de 40 à 49 ans",59:"de 50 à 59 ans",69:"de 60 à 69 ans",79:"de 70 à 79 ans",89:"de 80 à 89 ans",90:"90 ans et plus"})
hosp = hosp[["Hospitalisations","Réanimations","Décès (cumul)"]]

# Import données tests de dépistage
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/001aca18-df6a-45c8-89e6-f82d689e6c01",sep=";",parse_dates=["jour"])
reg = ["27"]
df = df[df["reg"].isin(reg)]
df = df[df["cl_age90"] != 0]

df2 = df.pivot_table(index=["jour"],columns="cl_age90",values=["P"]).last("1D")
df3 = df2.rename(columns={"P":"Tests positifs"})
tests = df3.rename(columns={0:"tous",9:"de 0 à 9 ans",19:"de 10 à 19 ans",29:"de 20 à 29 ans",39:"de 30 à 39 ans",49:"de 40 à 49 ans",59:"de 50 à 59 ans",69:"de 60 à 69 ans",79:"de 70 à 79 ans",89:"de 80 à 89 ans",90:"90 ans et plus"})

# Regroupement dans un seul fichier et export
pd.concat([tests.T,hosp.T]).to_csv("classes_age.csv")

##################
##### CARTES #####
##################
# Import données
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/c2e2e844-9671-4f81-8c81-1b79f7687de3",dtype=object)

# Filtre départements
depBFC = ["21","25","39","58","70","71","89","90"]

# Calcul nouvelles colonnes
df["dep"] = df["com2020"].str[:2]
df["date"] = df["semaine_glissante"].str[-5:]
df["fin_periode"] = df["date"].str[-2:] + "/" + df["date"].str[:2]

# Données les plus récentes pour la population générale
age = ["0"]
age = df[df["dep"].isin(depBFC) & df["clage_65"].isin(age)]
tcd = age.pivot_table(index="com2020",aggfunc='last')
carte = pd.read_csv("base_carte.csv",dtype=object)
carte["NOM_COM_OK"] = carte["NOM_COM"] + " (" + carte["INSEE_DEP"] + ")"
df2 = carte.merge(tcd,left_on="INSEE_COM",right_on="com2020")

df2["tp_classe"] = df2["tp_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")
df2["ti_classe"] = df2["ti_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")
df2["td_classe"] = df2["td_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")

df3 = df2[["geometry","INSEE_COM","INSEE_DEP","NOM_COM_OK","fin_periode","clage_65","ti_classe","tp_classe","td_classe"]]
df3.to_csv("carte_0.csv",index=False)

# Données les plus récentes pour les plus de 65 ans
age = ["65"]
age = df[df["dep"].isin(depBFC) & df["clage_65"].isin(age)]
tcd = age.pivot_table(index="com2020",aggfunc='last')
carte = pd.read_csv("base_carte.csv",dtype=object)
carte["NOM_COM_OK"] = carte["NOM_COM"] + " (" + carte["INSEE_DEP"] + ")"
df2 = carte.merge(tcd,left_on="INSEE_COM",right_on="com2020")

df2["tp_classe"] = df2["tp_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")
df2["ti_classe"] = df2["ti_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")
df2["td_classe"] = df2["td_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")

df3 = df2[["geometry","INSEE_COM","INSEE_DEP","NOM_COM_OK","fin_periode","clage_65","ti_classe","tp_classe","td_classe"]]
df3.to_csv("carte_65.csv",index=False)

# Tableaux récap
df = pd.read_csv("carte_0.csv")
df = df [["NOM_COM_OK","ti_classe","tp_classe"]]
df2 = df.rename(columns={"NOM_COM_OK":"Commune","ti_classe":"Taux d'incidence","tp_classe":"Taux de positivité"})
df2.to_csv("tableau_0.csv",index=False)

df = pd.read_csv("carte_65.csv")
df = df [["NOM_COM_OK","ti_classe","tp_classe"]]
df2 = df.rename(columns={"NOM_COM_OK":"Commune","ti_classe":"Taux d'incidence","tp_classe":"Taux de positivité"})
df2.to_csv("tableau_65.csv",index=False)

############################
##### DATE MISE À JOUR #####
############################
df = pd.read_csv("bfc_hospitalisations_total.csv", parse_dates=["jour"],index_col="jour")
df = df.last("1D")
df["Dernière mise à jour"] = df["jour_ok"].str[-2:] + "/" + df["jour_ok"].str[-5:].str[:2]
df[["Dernière mise à jour"]].to_csv("date_maj.csv",index=False)
