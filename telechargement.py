#coding: utf-8
import pandas as pd

### Fichiers source
# Hôpital
donnees_hospitalieres_covid19 = "https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"
donnees_hospitalieres_nouveaux_covid19 = "https://www.data.gouv.fr/fr/datasets/r/6fadff46-9efd-4c53-942a-54aca783c30c"
## A FAIRE donnees_hospitalieres_classe_age_covid19 = "https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3"

# Dépistage
sp_pos_quot_dep = "https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675"
sp_ti_tp_7j_dep = "https://www.data.gouv.fr/fr/datasets/r/d1c1846c-f2d1-43cb-ad84-b46c40d1bec8"
sp_ti_tp_7j_reg = "https://www.data.gouv.fr/fr/datasets/r/df2f66d3-ef9b-48e0-abdf-f33a6a7ff2fa"
sp_ti_tp_7j_fra = "https://www.data.gouv.fr/fr/datasets/r/c1167c4e-8c89-40f2-adb3-1954f8fedfa7"
sg_com_opendata = "https://www.data.gouv.fr/fr/datasets/r/c2e2e844-9671-4f81-8c81-1b79f7687de3"

# Vaccination
vacsi_tot_reg = "https://www.data.gouv.fr/fr/datasets/r/9b1e6c8c-7e1d-47f9-9eb9-f2eeaab60d99"
vacsi_tot_fra = "https://www.data.gouv.fr/fr/datasets/r/131c6b39-51b5-40a7-beaa-0eafc4b88466"
vacsi_tot_dep = "https://www.data.gouv.fr/fr/datasets/r/7969c06d-848e-40cf-9c3c-21b5bd5a874b"
vacsi_tot_a_reg = "https://www.data.gouv.fr/fr/datasets/r/2dadbaa7-02ae-43df-92bb-53a82e790cb2"
vacsi_reg  = "https://www.data.gouv.fr/fr/datasets/r/735b0df8-51b4-4dd2-8a2d-8e46d77d60d8"


# Lieux de vaccination
centres_vaccination = "https://www.data.gouv.fr/fr/datasets/r/5cb21a85-b0b0-4a65-a249-806a040ec372"

# Rendez-vous vaccinations
prise_rdv_par_reg = "https://www.data.gouv.fr/fr/datasets/r/3c3565e5-8e50-482d-b76a-fe07599ab4a0"

# Stock vaccin
livraisons_regional = "https://www.data.gouv.fr/fr/datasets/r/c3f04527-2d19-4476-b02c-0d86b5a9d3da"

vacsi_reg = "https://www.data.gouv.fr/fr/datasets/r/735b0df8-51b4-4dd2-8a2d-8e46d77d60d8"

# Filtres
code_dep = ["21","25","39","58","70","71","89","90"]
code_reg = ["27"]
sexe = ["0"]
cl_age90 = ["0"]

# Définitions
nom_dep = {"21":"Côte-d'Or",
           "25":"Doubs",
           "39":"Jura",
           "58":"Nièvre",
           "70":"Haute-Saône",
           "71":"Saône-et-Loire",
           "89":"Yonne",
           "90":"Territoire de Belfort"}

nom_reg = {"27":"Bourgogne-Franche-Comté",
          "FR":"France"}

pop_bfc = {"0":2228187, ## <-- total population uniquement 18 et plus
           "9":310831,
           "17":272405,
           
           "24":206308,
           "29":146612,
           "39":318460,
           "49":360444,
           "59":379032,
           "64":189118,
           "69":187345,
           "74":135474,
           "79":105926,
           "80":199468}

clage_vacsi = {"0":"Tous âges",
         "9":"0-9 ans",
         "17":"10-17 ans",
         "24":"18-24 ans",
         "29":"25-29 ans",
         "39":"30-39 ans",
         "49":"40-49 ans",
         "59":"50-59 ans",
         "64":"60-64 ans",
         "69":"65-69 ans",
         "74":"70-74 ans",
         "79":"75-79 ans",
         "80":"80 ans et plus"}



colonnes_donnees_hopital = {"nom_dep":"Département",
                           "hosp":"Hospitalisations en cours",
                           "rea":"Réanimations en cours",
                           "dc":"Décès (cumul)",
                           "rad":"Retours à domicile (cumul)",
                           "incid_hosp":"Nouvelles hospitalisations",
                           "incid_rea":"Nouvelles entrées en réanimation",
                           "incid_dc":"Nouveaux décès",
                           "incid_rad":"Nouveaux retours à domicile"}

colonnes_donnees_depistage = {"taux_incidence_7j":"Taux d'incidence",
                             "taux_positivite_7j":"Taux de positivité"}

### Hospitalisations par département
df = pd.read_csv(donnees_hospitalieres_covid19,sep=";",
                 parse_dates=["jour"],
                 dtype={"dep":str,"sexe":str,"hosp":int,"rea":int,"rad":int,"dc":int})
df = df[df["dep"].isin(code_dep) & df["sexe"].isin(sexe)]

df["nom_dep"] = df["dep"].map(nom_dep)
hosp_totales_par_dep_historique = df[["jour","nom_dep","hosp","rea"]].rename(columns=colonnes_donnees_hopital)
hosp_totales_par_dep_historique.to_csv("donnees/hosp_totales_par_dep_historique.csv",index=False)

### Cartouche hospitalisations BFC
reg_plus_recent = df[df["jour"] == max(df["jour"])].pivot_table(index="jour",aggfunc=sum)
reg_plus_recent = reg_plus_recent[["hosp","rea","dc"]].rename(columns=colonnes_donnees_hopital).T
reg_plus_recent.iloc[:,0] = reg_plus_recent.iloc[:,0].map('{:,}'.format)
reg_plus_recent.iloc[:,0] = reg_plus_recent.iloc[:,0].str.replace(',', ' ')
hosp_totales_bfc_plus_recent = reg_plus_recent
hosp_totales_bfc_plus_recent

### Nouvelles hospitalisations par département
df = pd.read_csv(donnees_hospitalieres_nouveaux_covid19,sep=";",
                 dtype={"dep":str,"incid_hosp":int,"incid_rea":int,"incid_dc":int,"incid_rea":int},
                 parse_dates=["jour"])
df = df[df["dep"].isin(code_dep)]
df["nom_dep"] = df["dep"].map(nom_dep)
hosp_nouvelles_par_dep = df[["jour","nom_dep","incid_hosp","incid_rea","incid_dc","incid_rad"]].rename(columns=colonnes_donnees_hopital)
hosp_nouvelles_par_dep.to_csv("donnees/hosp_nouvelles_par_dep.csv",index=False)

### Cartouche nouvelles hospitalisations BFC
reg_plus_recent = df[df["jour"] == max(df["jour"])].pivot_table(index="jour",aggfunc=sum)
reg_plus_recent = reg_plus_recent[["incid_hosp","incid_rea","incid_dc"]].rename(columns=colonnes_donnees_hopital).T
reg_plus_recent.iloc[:,0] = reg_plus_recent.iloc[:,0].map('{:,}'.format)
reg_plus_recent.iloc[:,0] = reg_plus_recent.iloc[:,0].str.replace(',', ' ')
hosp_nouvelles_bfc_plus_recent = reg_plus_recent
hosp_nouvelles_bfc_plus_recent.to_csv("donnees/hosp_nouvelles_bfc_plus_recent.csv")

### Cartouche hôpital BFC
hosp_bfc_recap = pd.concat([hosp_totales_bfc_plus_recent,hosp_nouvelles_bfc_plus_recent])
hosp_bfc_recap.to_csv("donnees/hosp_bfc_recap.csv")

### Taux d'incidence et de positivité par département
df = pd.read_csv(sp_ti_tp_7j_dep,sep=";",
                 dtype={"dep":str,"P":int,"T":int,"pop":float})
df = df[df["dep"].isin(code_dep)]
df["debut_7j"] = df.loc[:,"semaine_glissante"].str[:10]
df["fin_7j"] = df.loc[:,"semaine_glissante"].str[-10:]
df["taux_incidence_7j"] = (df["P"]*100000/df["pop"]).round(decimals=1)
df["taux_positivite_7j"] = (df["P"]/df["T"]*100).round(decimals=1)
df["nom_dep"] = df["dep"].map(nom_dep)
incidence_positivite_dep = df[["nom_dep","debut_7j","fin_7j","taux_incidence_7j","taux_positivite_7j"]]

incidence_positivite_dep.loc[:,"debut_7j"] = pd.to_datetime(incidence_positivite_dep.loc[:,"debut_7j"])
incidence_positivite_dep.loc[:,"fin_7j"] = pd.to_datetime(incidence_positivite_dep.loc[:,"fin_7j"])

depistage_incidence_positivite_dep_historique = incidence_positivite_dep.rename(columns=colonnes_donnees_depistage)
depistage_incidence_positivite_dep_historique.to_csv("donnees/depistage_incidence_positivite_dep_historique.csv",index=False)


### Cartouche taux incidence et positivité par département
depistage_incidence_par_dep_plus_recent = incidence_positivite_dep[["nom_dep","debut_7j","fin_7j","taux_incidence_7j"]][incidence_positivite_dep["fin_7j"] == max(incidence_positivite_dep["fin_7j"])]

depistage_positivite_par_dep_plus_recent = incidence_positivite_dep[["nom_dep","taux_positivite_7j"]][incidence_positivite_dep["fin_7j"] == max(incidence_positivite_dep["fin_7j"])]

depistage_incidence_positivite_par_dep_plus_recent = depistage_incidence_par_dep_plus_recent.merge(depistage_positivite_par_dep_plus_recent,left_on="nom_dep",right_on="nom_dep")

depistage_incidence_positivite_par_dep_plus_recent["debut_7j"] = depistage_incidence_positivite_par_dep_plus_recent["debut_7j"].dt.strftime("%d/%m")
depistage_incidence_positivite_par_dep_plus_recent["fin_7j"] = depistage_incidence_positivite_par_dep_plus_recent["fin_7j"].dt.strftime("%d/%m")

depistage_incidence_positivite_par_dep_plus_recent.to_csv("donnees/depistage_incidence_positivite_par_dep_plus_recent.csv")

#### Taux d'incidence et taux de positivité sur 7 jours glissants pour BFC et France
df = pd.read_csv(sp_ti_tp_7j_reg,sep=";",dtype={"reg":str,"P":int,"T":int,"pop":float})
df = df[df["reg"].isin(code_reg)]
df["debut_7j"] = df["semaine_glissante"].str[:10]
df["fin_7j"] = df["semaine_glissante"].str[-10:]
df["taux_incidence_7j"] = (df["P"]*100000/df["pop"]).round(decimals=1)
df["taux_positivite_7j"] = (df["P"]/df["T"]*100).round(decimals=1)
df["nom_reg"] = df["reg"].map(nom_reg)

incidence_positivite_bfc = df[["nom_reg","debut_7j","fin_7j","taux_incidence_7j","taux_positivite_7j"]]

df = pd.read_csv(sp_ti_tp_7j_fra,sep=";",dtype={"P":int,"T":int,"pop":float})
df["reg"] = "FR"
df["debut_7j"] = df["semaine_glissante"].str[:10]
df["fin_7j"] = df["semaine_glissante"].str[-10:]
df["taux_incidence_7j"] = (df["P"]*100000/df["pop"]).round(decimals=1)
df["taux_positivite_7j"] = (df["P"]/df["T"]*100).round(decimals=1)
df["nom_reg"] = df["reg"].map(nom_reg)

incidence_positivite_france = df[["nom_reg","debut_7j","fin_7j","taux_incidence_7j","taux_positivite_7j"]]
incidence_positivite_france_bfc = pd.concat([incidence_positivite_bfc,incidence_positivite_france])
depistage_incidence_positivite_bfc_france_historique = incidence_positivite_france_bfc.rename(columns=colonnes_donnees_depistage)

depistage_incidence_positivite_bfc_france_historique.to_csv("donnees/depistage_incidence_positivite_bfc_france_historique.csv",index=False)

incidence_positivite_france_bfc_plus_recent = incidence_positivite_france_bfc[incidence_positivite_france_bfc["fin_7j"] == max(incidence_positivite_france_bfc["fin_7j"])]

incidence_positivite_france_bfc_plus_recent.loc[:,"debut_7j"] = pd.to_datetime(incidence_positivite_france_bfc_plus_recent["debut_7j"])
incidence_positivite_france_bfc_plus_recent.loc[:,"fin_7j"] = pd.to_datetime(incidence_positivite_france_bfc_plus_recent["fin_7j"])

incidence_positivite_france_bfc_plus_recent.loc[:,"debut_7j"] = incidence_positivite_france_bfc_plus_recent["debut_7j"].dt.strftime("%d/%m")
incidence_positivite_france_bfc_plus_recent.loc[:,"fin_7j"] = incidence_positivite_france_bfc_plus_recent["fin_7j"].dt.strftime("%d/%m")

depistage_incidence_positivite_france_bfc_plus_recent = incidence_positivite_france_bfc_plus_recent

depistage_incidence_positivite_france_bfc_plus_recent.to_csv("donnees/depistage_incidence_positivite_france_bfc_plus_recent.csv")


### Carte taux d'incidence et positivité par commune BFC
df = pd.read_csv(sg_com_opendata,sep=";",skiprows=1,names=["com2020","semaine_glissante","clage_65","ti_classe_debut","ti_classe_fin","td_classe_debut","td_classe_fin","tp_classe_debut","tp_classe_fin"],dtype=str)

df["dep"] = df["com2020"].str[:2]
df = df[df["dep"].isin(code_dep)]
df["debut_7j"] = df.loc[:,"semaine_glissante"].str[:10]
df["fin_7j"] = df.loc[:,"semaine_glissante"].str[-10:]

df["tp_classe"] = df.loc[:,"tp_classe_debut"].str.replace("[","",regex=False).str.replace("]","",regex=False) + " à " + df.loc[:,"tp_classe_fin"].str.replace("[","",regex=False).str.replace("]","",regex=False)
df["ti_classe"] = df.loc[:,"ti_classe_debut"].str.replace("[","",regex=False).str.replace("]","",regex=False) + " à " + df.loc[:,"ti_classe_fin"].str.replace("[","",regex=False).str.replace("]","",regex=False)
df["td_classe"] = df.loc[:,"td_classe_debut"].str.replace("[","",regex=False).str.replace("]","",regex=False) + " à " + df.loc[:,"td_classe_fin"].str.replace("[","",regex=False).str.replace("]","",regex=False)

df["tp_classe"] = df.loc[:,"tp_classe"].str.replace("à Max","et plus",regex=False)
df["ti_classe"] = df.loc[:,"ti_classe"].str.replace("à Max","et plus",regex=False)
df["td_classe"] = df.loc[:,"td_classe"].str.replace("à Max","et plus",regex=False)

depistage_carte_communes_bfc = df[["com2020","dep","debut_7j","fin_7j","clage_65","tp_classe","ti_classe","td_classe"]][df["fin_7j"] == max(df["fin_7j"])]

depistage_carte_communes_bfc.to_csv("donnees/depistage_carte_communes_bfc.csv",index=False)

### Evolution vaccination BFC
df = pd.read_csv(vacsi_reg,dtype={"reg":str,"n_dose1":int,"n_cum_dose1":int,"n_dose2":int,"n_cum_dose2":int},parse_dates=["jour"])
df = df[df["reg"].isin(code_reg)]

vaccin_historique_bfc = df[["jour","n_cum_dose1"]].rename(columns={"n_cum_dose1":"Premières doses (cumul)"})
vaccin_historique_bfc.to_csv("donnees/vaccin_historique_bfc.csv",index=False)

### Total vaccination BFC
df = pd.read_csv(vacsi_tot_reg,dtype={"reg":str,"n_tot_dose1":int,"n_tot_dose2":int},parse_dates=["jour"])
df = df[df["reg"].isin(code_reg)]
df["nom_reg"] = df["reg"].map(nom_reg)
vaccin_tot_bfc = df[["nom_reg","jour","n_tot_dose1","n_tot_dose2"]]


### Total vaccination France
df = pd.read_csv(vacsi_tot_fra,dtype={"reg":str,"n_tot_dose1":int,"n_tot_dose2":int},parse_dates=["jour"])
df["reg"] = df["fra"]
df["nom_reg"] = df["reg"].map(nom_reg)
vaccin_tot_fr = df[["nom_reg","jour","n_tot_dose1","n_tot_dose2"]]


### Cartouche vaccination BFC et France
df = pd.concat([vaccin_tot_bfc,vaccin_tot_fr])

df["jour"] = df["jour"].dt.strftime("%d/%m")

df["n_tot_dose1"] = df["n_tot_dose1"].map('{:,}'.format)
df["n_tot_dose1"] = df["n_tot_dose1"].str.replace(',', ' ')

df["n_tot_dose2"] = df["n_tot_dose2"].map('{:,}'.format)
df["n_tot_dose2"] = df["n_tot_dose2"].str.replace(',', ' ')

vaccin_tot_bfc_fr = df


vaccin_tot_bfc_fr.to_csv("donnees/vaccin_tot_bfc_fr.csv",index=False)

### Vaccination par département
df = pd.read_csv(vacsi_tot_dep,dtype={"dep":str,"n_tot_dose1":int,"n_tot_dose2":int},parse_dates=["jour"])

df = df[df["dep"].isin(code_dep)]
df["nom_dep"] = df["dep"].map(nom_dep)
df["n_tot_dose2"] = df["n_tot_dose1"]### a changer quand on pourra
df = df[["nom_dep","jour","n_tot_dose1","n_tot_dose2"]]

df["jour"] = df["jour"].dt.strftime("%d/%m")

df["n_tot_dose1"] = df["n_tot_dose1"].map('{:,}'.format)
df["n_tot_dose1"] = df["n_tot_dose1"].str.replace(',', ' ')

df["n_tot_dose2"] = df["n_tot_dose2"].map('{:,}'.format)
df["n_tot_dose2"] = df["n_tot_dose2"].str.replace(',', ' ')

vaccin_tot_dep = df

vaccin_tot_dep.to_csv("donnees/vaccin_tot_dep.csv",index=False)

### Vaccination par âge BFC
df = pd.read_csv(vacsi_tot_a_reg,dtype={"reg":str,"clage_vacsi":str,"n_tot_dose1":int,"n_tot_dose2":int},parse_dates=["jour"])
df = df[df["reg"].isin(code_reg)]
df = df[df["clage_vacsi"] != "0"]
df["pop"] = df["clage_vacsi"].map(pop_bfc)

df["pct_n_tot_dose1"] = (df["n_tot_dose1"]/df["pop"]*100).round(decimals=2)
df["pct_n_tot_dose2"] = (df["n_tot_dose2"]/df["pop"]*100).round(decimals=2)

df["n_tot_dose1"] = df["n_tot_dose1"].map('{:,}'.format)
df["n_tot_dose1"] = df["n_tot_dose1"].str.replace(',', ' ')

df["n_tot_dose2"] = df["n_tot_dose2"].map('{:,}'.format)
df["n_tot_dose2"] = df["n_tot_dose2"].str.replace(',', ' ')

df["nom_clage_vacsi"] = df["clage_vacsi"].map(clage_vacsi)

df["jour"] = df["jour"].dt.strftime("%d/%m")

vaccin_par_age_bfc = df[["nom_clage_vacsi","n_tot_dose1","pct_n_tot_dose1","n_tot_dose2","pct_n_tot_dose2","jour"]]

vaccin_par_age_bfc.to_csv("donnees/vaccin_par_age_bfc.csv",index=False)


### Données pour tableau détail par régions et comparaison à la population ###

df = pd.read_csv(vacsi_tot_reg,sep=",",dtype={"reg":str,"n_tot_dose1":int,"n_tot_dose2":int})

pop = pd.read_csv("sources/pop_regions.csv",sep=",",dtype={"code_reg":str,"reg":str,"nom_reg":str,"pop":int})

df = df.merge(pop,left_on="reg",right_on="reg")
df["pct_n_tot_dose1"] = (df["n_tot_dose1"]/df["pop"]*100).round(decimals=2)
df["pct_n_tot_dose2"] = (df["n_tot_dose2"]/df["pop"]*100).round(decimals=2)

df["n_tot_dose1"] = df["n_tot_dose1"].map('{:,}'.format)
df["n_tot_dose1"] = df["n_tot_dose1"].str.replace(',', ' ')

df["n_tot_dose2"] = df["n_tot_dose2"].map('{:,}'.format)
df["n_tot_dose2"] = df["n_tot_dose2"].str.replace(',', ' ')

vaccin_comparaison_region = df.sort_values(by="pct_n_tot_dose2", ascending=False)[["nom_reg","n_tot_dose1","pct_n_tot_dose1","n_tot_dose2","pct_n_tot_dose2"]].rename(columns={"nom_reg":"Région","n_tot_dose1":"Premières doses","n_tot_dose2":"Deuxièmes doses","pct_n_tot_dose1":"% de la population","pct_n_tot_dose2":"% de la population"})

vaccin_comparaison_region.to_csv("donnees/vaccin_comparaison_regions.csv",index=False)  

### Données rendez-vous vaccins ###
df = pd.read_csv(prise_rdv_par_reg,parse_dates=["date_debut_semaine"],dtype={"code_region":str,"rang_vaccinal":str,"nb":int})
df = df[df["code_region"].isin(code_reg)]
df = df.pivot_table(index="date_debut_semaine",values="nb",columns="rang_vaccinal",aggfunc=sum)
df["Total"] = df["1"] + df["2"]
df["date"] = df.index
df["jour"] = df["date"].dt.strftime("%d/%m")
df = df[["jour","1","2","Total"]].rename(columns={"jour":"Semaine du ","1":"Rendez-vous pour la première dose","2":"Rendez-vous pour la deuxième dose","Total":"Nombre total de rendez-vous"})
vaccin_nombre_rdv_bfc = df

vaccin_nombre_rdv_bfc.to_csv("donnees/vaccin_nombre_rdv_bfc.csv",index=False)

### Données livraisons vaccins ####
df = pd.read_csv(livraisons_regional,sep=";",dtype={"code_region":str},parse_dates=["date"],index_col="date")
df = df[df["code_region"].isin(code_reg)]
df["date"] = df.index
df["jour"] = df["date"].dt.strftime("%d/%m")
df = df.last("1D").pivot_table(index=["type_de_vaccin","jour"],values="nb_doses_receptionnees_cumul",aggfunc=sum)
df["nb_doses_receptionnees_cumul"] = df["nb_doses_receptionnees_cumul"].map('{:,}'.format)
df["nb_doses_receptionnees_cumul"] = df["nb_doses_receptionnees_cumul"].str.replace(',', ' ')
vaccin_livraisons_doses = df

vaccin_livraisons_doses.to_csv("donnees/vaccin_livraisons_doses.csv")

# Lieux vaccinations
df = pd.read_csv(centres_vaccination,sep=";", encoding="utf-8",dtype=str)
df["dep"] = df["com_insee"].str[:2]
df = df[df["dep"].isin(code_dep)]
df = df[["gid","nom","adr_num","adr_voie","com_cp","com_nom","lat_coor1","long_coor1","_edit_datemaj","lieu_accessibilite","rdv_lundi","rdv_mardi","rdv_mercredi","rdv_jeudi","rdv_vendredi","rdv_samedi","rdv_dimanche","date_fermeture","date_ouverture","rdv_site_web","rdv_tel","rdv_modalites","dep"]]
vaccin_lieux_vaccination = df
vaccin_lieux_vaccination.to_json("donnees/vaccin_lieux_vaccination.json",orient="records")