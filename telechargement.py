import requests
import time

urlsEtfichiers = {'https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=1095809811&single=true&output=csv': 'retourdom.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=1142885751&single=true&output=csv': 'carte.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=125960350&single=true&output=csv': 'bfc.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=1779906158&single=true&output=csv': '21.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=1018863531&single=true&output=csv': '25.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=1346077964&single=true&output=csv': '39.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=1100340057&single=true&output=csv': '58.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=2032450000&single=true&output=csv': '70.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=224371307&single=true&output=csv': '71.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=1653344045&single=true&output=csv': '89.csv','https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=711918987&single=true&output=csv': "90.csv"}

for url, fichier in urlsEtfichiers.items(): 
    r = requests.get(url, allow_redirects=True)
    open(fichier, 'wb').write(r.content)
    
    with open(fichier, 'r') as file:
        contents = file.read()
        while 'Lignes' in contents:
            print ('On redownload')
            time.sleep(10)
            r = requests.get(url, allow_redirects=True)
            open(fichier, 'wb').write(r.content)
            contents = file.read()
        else:
            print ('Tout est OK')