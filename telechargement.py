#coding: utf-8
import pandas as pd

############################
##### TAUX D'INCIDENCE #####
############################

# Import fichiers
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/19a91d64-3cd3-42fc-9943-d635491a4d76", sep=";", dtype={"dep":object,"P":int,"cl_age90":object})

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
df_dep["dep_ok"] = df_dep["dep"].replace({21:"Cote-d'Or",25:"Doubs",39:"Jura",58:"Nievre",70:"Haute-Saone",71:"Saone-et-Loire",89:"Yonne",90:"Territoire de Belfort"})
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
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675", sep=";",dtype={"dep":object,"P":int,"cl_age90":object})

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
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7", sep=";", dtype={"dep":object,"sexe":object},parse_dates=["jour"])


# Description filtre
depBFC = ["21","25","39","58","70","71","89","90"]
sexe = ["0"]

# Filtre données BFC et toutes classes d'âge
df = df[df["dep"].isin(depBFC) & df["sexe"].isin(sexe)]

# Renommage colonnes et départements
df["dep_ok"] = df["dep"].replace({21:"Cote-d'Or",25:"Doubs",39:"Jura",58:"Nievre",70:"Haute-Saone",71:"Saone-et-Loire",89:"Yonne",90:"Territoire de Belfort"})
df2 = df[["dep","sexe","jour","hosp","rea","dc","dep_ok"]]
df_ok = df2.rename(index=str, columns={"hosp":"Personnes hospitalisées","rea":"Personnes en réanimation","rad":"Personnes de retour à domicile (cumul)","dc":"Personnes décédées (cumul)"})

# Export fichier
df_ok.to_csv("dep_hospitalisations.csv",index=False)
for departement in depBFC:
    df3 = df_ok[df_ok["dep"] == departement]
    df3.to_csv(departement+"_hospitalisations.csv",index=False)

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

df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7", sep=";",parse_dates=["jour"],dtype={"dep":object,"sexe":object})

df = df[df["dep"].isin(depBFC) & df["sexe"].isin(sexe)]


tcd = df.pivot_table(index=["jour"],values=["hosp","rea","dc","rad"],aggfunc=sum)


tcd2 = tcd[['hosp', 'rea', 'dc', 'rad']].last("1D").T
tcd2["categorie"] = tcd2.index
tcd3 = tcd2.replace({"dc":"Décès à l'hôpital (cumul)","hosp":"Personnes actuellement hospitalisées", "rea":"Personnes actuellement en réanimation","rad":"Personnes de retour à domicile (cumul)"})
tcd3.to_csv("bfc_hospitalisations_jour.csv")

### Nombre de décès par jour à l'hôpital ###

df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/6fadff46-9efd-4c53-942a-54aca783c30c", sep=";", parse_dates=["jour"])
depBFC = ["21","25","39","58","70","71","89","90"]

df = df[df["dep"].isin(depBFC)]

df = df.replace({"21":"Cote-d'Or","25":"Doubs","39":"Jura","58":"Nievre","70":"Haute-Saone","71":"Saone-et-Loire","89":"Yonne","90":"Territoire de Belfort"})
df = df.pivot_table(index="jour",columns="dep",values="incid_dc",aggfunc=sum,margins=True,margins_name="Bourgogne-Franche-Comte").iloc[:-1]

df[["Bourgogne-Franche-Comte","Cote-d'Or","Doubs","Jura","Nievre","Haute-Saone","Saone-et-Loire","Yonne","Territoire de Belfort"]].to_csv("dep_nouveaux_deces_jour.csv")

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
reg = ["27"]
# Import données hospitalières
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3",sep=";",parse_dates=["jour"],dtype={"reg":object,"cl_age90":object})


df = df[df["reg"].isin(reg)]
df = df[df["cl_age90"] != 0]

df2 = df.pivot_table(index=["jour"],columns="cl_age90",values=["dc","hosp","rea"]).last("1D")
df3 = df2.rename(columns={"hosp":"Hospitalisations en cours","rea":"Réanimations en cours","dc":"Décès depuis mars à l'hôpital"})


hosp = df3.rename(columns={0:"tous",9:"de 0 à 9 ans",19:"de 10 à 19 ans",29:"de 20 à 29 ans",39:"de 30 à 39 ans",49:"de 40 à 49 ans",59:"de 50 à 59 ans",69:"de 60 à 69 ans",79:"de 70 à 79 ans",89:"de 80 à 89 ans",90:"90 ans et plus"})
hosp = hosp[["Hospitalisations en cours","Réanimations en cours","Décès depuis mars à l'hôpital"]]

# Import données tests de dépistage
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/001aca18-df6a-45c8-89e6-f82d689e6c01",sep=";",parse_dates=["jour"])
reg = ["27"]
df = df[df["reg"].isin(reg)]
df = df[df["cl_age90"] != 0]

df2 = df.pivot_table(index=["jour"],columns="cl_age90",values=["P"]).last("1D")
df3 = df2.rename(columns={"P":"Tests positifs les 7 derniers jours"})
tests = df3.rename(columns={0:"tous",9:"de 0 à 9 ans",19:"de 10 à 19 ans",29:"de 20 à 29 ans",39:"de 30 à 39 ans",49:"de 40 à 49 ans",59:"de 50 à 59 ans",69:"de 60 à 69 ans",79:"de 70 à 79 ans",89:"de 80 à 89 ans",90:"90 ans et plus"})

# Regroupement dans un seul fichier et export
pd.concat([tests.T,hosp.T]).to_csv("classes_age.csv")

##################
##### CARTES #####
##################
# Import données
# df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/c2e2e844-9671-4f81-8c81-1b79f7687de3",dtype=object,sep=";")

# Filtre départements
# depBFC = ["21","25","39","58","70","71","89","90"]

# Calcul nouvelles colonnes
# df["dep"] = df["com2020"].str[:2]
# df["date"] = df["semaine_glissante"].str[-5:]
# df["fin_periode"] = df["date"].str[-2:] + "/" + df["date"].str[:2]

# Données les plus récentes pour la population générale
# age = ["0"]
# age = df[df["dep"].isin(depBFC) & df["clage_65"].isin(age)]
# tcd = age.pivot_table(index="com2020",aggfunc='last')
# carte = pd.read_csv("base_carte.csv",dtype=object)
# carte["NOM_COM_OK"] = carte["NOM_COM"] + " (" + carte["INSEE_DEP"] + ")"
# df2 = carte.merge(tcd,left_on="INSEE_COM",right_on="com2020")

# df2["tp_classe"] = df2["tp_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")
# df2["ti_classe"] = df2["ti_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")
# df2["td_classe"] = df2["td_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")

# df3 = df2[["geometry","INSEE_COM","INSEE_DEP","NOM_COM_OK","fin_periode","clage_65","ti_classe","tp_classe","td_classe"]]
# df3.to_csv("carte_0.csv",index=False)

# Données les plus récentes pour les plus de 65 ans
# age = ["65"]
# age = df[df["dep"].isin(depBFC) & df["clage_65"].isin(age)]
# tcd = age.pivot_table(index="com2020",aggfunc='last')
# carte = pd.read_csv("base_carte.csv",dtype=object)
# carte["NOM_COM_OK"] = carte["NOM_COM"] + " (" + carte["INSEE_DEP"] + ")"
# df2 = carte.merge(tcd,left_on="INSEE_COM",right_on="com2020")

# df2["tp_classe"] = df2["tp_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")
# df2["ti_classe"] = df2["ti_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")
# df2["td_classe"] = df2["td_classe"].str.replace(";"," à ").str.replace("[","").str.replace("]","").str.replace("à Max","et plus")

# df3 = df2[["geometry","INSEE_COM","INSEE_DEP","NOM_COM_OK","fin_periode","clage_65","ti_classe","tp_classe","td_classe"]]
# df3.to_csv("carte_65.csv",index=False)

# Tableaux récap
# df = pd.read_csv("carte_0.csv")
# df = df [["NOM_COM_OK","ti_classe","tp_classe"]]
# df2 = df.rename(columns={"NOM_COM_OK":"Commune","ti_classe":"Taux d'incidence","tp_classe":"Taux de positivité"})
# df2.to_csv("tableau_0.csv",index=False)

# df = pd.read_csv("carte_65.csv")
# df = df [["NOM_COM_OK","ti_classe","tp_classe"]]
# df2 = df.rename(columns={"NOM_COM_OK":"Commune","ti_classe":"Taux d'incidence","tp_classe":"Taux de positivité"})
# df2.to_csv("tableau_65.csv",index=False)

##############################################
##### CARTES avec données séparées par ; #####
##############################################

# Import données
import pandas as pd
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/c2e2e844-9671-4f81-8c81-1b79f7687de3",dtype=object, index_col=None,skiprows=1,sep=";",names=["com2020","semaine_glissante","clage_65","ti_classe_debut","ti_classe_fin","td_classe_debut","td_classe_fin","tp_classe_debut","tp_classe_fin"])
df["dep"] = df["com2020"].str[:2]

# Filtre départements
depBFC = ["21","25","39","58","70","71","89","90"]
age = ["0"]

df = df[df["dep"].isin(depBFC)]

# Calcul nouvelles colonnes

df["date"] = df["semaine_glissante"].str[-10:]
df["fin_periode"] = df["date"].str[-5:].str[-2:] + "/" + df["date"].str[-5:].str[:2]

# Données les plus récentes pour la population générale
cl_age = ["0"]
age = df[df["clage_65"].isin(cl_age)]

tcd = age.pivot_table(index="com2020",aggfunc='last')

carte = pd.read_csv("base_carte.csv",dtype=object)
carte["NOM_COM_OK"] = carte["NOM_COM"] + " (" + carte["INSEE_DEP"] + ")"
df2 = carte.merge(tcd,left_on="INSEE_COM",right_on="com2020")

df2["tp_classe"] = df2["tp_classe_debut"].str.replace("[","").str.replace("]","") + " à " + df2["tp_classe_fin"].str.replace("[","").str.replace("]","")
df2["ti_classe"] = df2["ti_classe_debut"].str.replace("[","").str.replace("]","") + " à " + df2["ti_classe_fin"].str.replace("[","").str.replace("]","")
df2["td_classe"] = df2["td_classe_debut"].str.replace("[","").str.replace("]","") + " à " + df2["td_classe_fin"].str.replace("[","").str.replace("]","")

df2["tp_classe"] = df2["tp_classe"].str.replace("à Max","et plus")
df2["ti_classe"] = df2["ti_classe"].str.replace("à Max","et plus")
df2["td_classe"] = df2["td_classe"].str.replace("à Max","et plus")

df3 = df2[["geometry","INSEE_COM","INSEE_DEP","NOM_COM_OK","fin_periode","clage_65","ti_classe","tp_classe","td_classe"]]
df3.to_csv("carte_0.csv",index=False)

# Données les plus récentes pour les 65 ans et plus
cl_age = ["65"]
age = df[df["clage_65"].isin(cl_age)]

tcd = age.pivot_table(index="com2020",aggfunc='last')

carte = pd.read_csv("base_carte.csv",dtype=object)
carte["NOM_COM_OK"] = carte["NOM_COM"] + " (" + carte["INSEE_DEP"] + ")"
df2 = carte.merge(tcd,left_on="INSEE_COM",right_on="com2020")

df2["tp_classe"] = df2["tp_classe_debut"].str.replace("[","").str.replace("]","") + " à " + df2["tp_classe_fin"].str.replace("[","").str.replace("]","")
df2["ti_classe"] = df2["ti_classe_debut"].str.replace("[","").str.replace("]","") + " à " + df2["ti_classe_fin"].str.replace("[","").str.replace("]","")
df2["td_classe"] = df2["td_classe_debut"].str.replace("[","").str.replace("]","") + " à " + df2["td_classe_fin"].str.replace("[","").str.replace("]","")

df2["tp_classe"] = df2["tp_classe"].str.replace("à Max","et plus")
df2["ti_classe"] = df2["ti_classe"].str.replace("à Max","et plus")
df2["td_classe"] = df2["td_classe"].str.replace("à Max","et plus")

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

################################
##### CHIFFRES VACCINATION #####
################################

### Données de vaccination pour cartouche BFC et France ###
# Filtres
sexe = ["0"]
reg = ["27","FR"]
clage_vacsi = ["0"]

# Téléchargement des fichiers
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/735b0df8-51b4-4dd2-8a2d-8e46d77d60d8",sep=";",parse_dates=["jour"],dtype={"reg":str},index_col="jour")
nat = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/efe23314-67c4-45d3-89a2-3faef82fae90",sep=";",parse_dates=["jour"],dtype={"reg":str},index_col="jour")

# Filtrage région
df = df[df["reg"].isin(reg)].last("1D")

# Filtrage natio
nat["reg"] = "FR"
nat = nat.last("1D")

# On regroupe tout ça
total = pd.concat([df,nat])[["reg","n_cum_dose1"]]

# Mise en forme de la date pour être plus lisible
total["date"] = total.index
total["jour"] = total["date"].dt.strftime("%d/%m")

# Mise en forme du nombre de vaccinés pour être plus lisible
total["n_cum_dose1"] = total["n_cum_dose1"].map('{:,}'.format)
total["n_cum_dose1"] = total["n_cum_dose1"].str.replace(',', ' ')

# Mise en forme du nom des régions pour être plus lisible
nom = {"27": "Bourgogne-Franche-Comté", "FR":"France"}
total["nom"] = total["reg"].map(nom)

# Export des colonnes qui nous intéressent
total[["nom","n_cum_dose1","jour"]].to_csv("max_vaccins.csv",index=False)

### Données BFC avec évolution nombre de vaccinés ###
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/735b0df8-51b4-4dd2-8a2d-8e46d77d60d8",sep=";",dtype={"reg":str,"n_dose1":int,"n_cum_dose1":int},parse_dates=["jour"],index_col="jour")
df = df[df["reg"].isin(reg)]
df = df[["n_dose1","n_cum_dose1"]].rename(columns={"n_dose1":"Nombre de personnes ayant reçu une dose de vaccin","n_cum_dose1":"Nombre cumulé de personnes ayant reçu une dose de vaccin"})
df.to_csv("evolution_vaccination_bfc.csv")

### Données pour graphique par tranches d'âge BFC ###

# Import
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/2dadbaa7-02ae-43df-92bb-53a82e790cb2",sep=";",parse_dates=["jour"],dtype={"reg":str,"clage_vacsi":str,"n_cum_dose1":int})

# Filtre
df = df[df["reg"].isin(reg)]
df = df[df["clage_vacsi"] != "0"]

# On explicite les données
df = df.replace({"0":"Tous âges","9":"0-9 ans","17":"10-17 ans","24":"18-24 ans","29":"25-29 ans","39":"30-39 ans","49":"40-49 ans","59":"50-59 ans","64":"60-64 ans","69":"65-69 ans","74":"70-74 ans","79":"75-79 ans","80":"80 ans et plus"})

# On remet tout ça en forme
df = df.pivot_table(columns="clage_vacsi",values="n_cum_dose1",aggfunc=sum,fill_value=0)
df = df.T
df["clage"] = df.index
df = df.rename(columns={"n_cum_dose1":"Nombre cumulé de personnes ayant reçu une dose de vaccin","clage":"Classes d'âge"})

# Et on exporte
df.to_csv("vaccins_bfc_age.csv")

### Données pour tableau détail par régions et comparaison à la population ###

# Import
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/2dadbaa7-02ae-43df-92bb-53a82e790cb2",sep=";",dtype={"reg":str,"n_dose1":int,"n_cum_dose1":int,"clage_vacsi":str})

# Filtre
df = df[df["clage_vacsi"].isin(clage_vacsi)]

# On remet en forme
df.pivot_table(index="reg",values="n_cum_dose1",aggfunc=sum)

# On retrouve les chiffres de population
pop = pd.read_csv("population_reg.csv",sep=",",dtype={"reg":str})

# On fusionne tout ensemble et on calcule
df = df.merge(pop,left_on="reg",right_on="reg")
df["% de la population"] = (df["n_cum_dose1"]/df["pop"]*100).round(decimals=2)

# On trie ça dans l'ordre et on exporte
df.sort_values(by="% de la population", ascending=False)[["Région","n_cum_dose1","% de la population"]].rename(columns={"n_cum_dose1":"Nombre cumulé de personnes ayant reçu une dose de vaccin"}).to_csv("tableau_vaccination_regions.csv",index=False)       


########################################
##### CARTE CENTRES DE VACCINATION #####
########################################

df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/5cb21a85-b0b0-4a65-a249-806a040ec372",sep=";", encoding="utf-8",dtype=str)
df["dep"] = df["com_insee"].str[:2]
df = df[df["dep"].isin(["21","25","39","58","70","71","89","90"])]
df = df[["gid","nom","adr_num","adr_voie","com_cp","com_nom","lat_coor1","long_coor1","_edit_datemaj","lieu_accessibilite","rdv_lundi","rdv_mardi","rdv_mercredi","rdv_jeudi","rdv_vendredi","rdv_samedi","rdv_dimanche","date_fermeture","date_ouverture","rdv_site_web","rdv_tel","rdv_modalites","dep"]]
df.to_json("lieux_vaccination.json",orient="records")


##################################
##### CHIFFRES DOSES VACCINS #####
##################################

# Données cumul livraisons par région
df = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/c3f04527-2d19-4476-b02c-0d86b5a9d3da",sep=";",index_col="date",parse_dates=["date"])
df = df[df["code_region"]==27]
df["region"] = "Bourgogne-Franche-Comté"
df = df.last("1D").pivot_table(index="region",values=["nb_doses_receptionnees_cumul"],aggfunc=sum)

# Données cumul livraisons national
nat = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/6820ff9f-2dbb-4e87-8565-fcd7fa2dfa0f",sep=";",index_col="date",parse_dates=["date"])
nat["region"] = "France"
nat = nat.last("1D").pivot_table(index="region",values=["nb_doses_receptionnees_cumul"],aggfunc=sum)

# On fusionne tout ça, on formate et on exporte
total = pd.concat([df,nat])
total["nb_doses_receptionnees_cumul"] = total["nb_doses_receptionnees_cumul"].map('{:,}'.format)
total["nb_doses_receptionnees_cumul"] = total["nb_doses_receptionnees_cumul"].str.replace(',', ' ')

total.to_csv("livraisons_vaccins.csv")
