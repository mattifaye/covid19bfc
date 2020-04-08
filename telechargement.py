import requests


url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTs_XIZk2vydeg_0cw6hn9_YTNAJ9679Uw03aa7PogpQqL6G7a838mrNjZInh_pgthpYBLEa9R7iJcF/pub?gid=1095809811&single=true&output=csv'
r = requests.get(url, allow_redirects=True)

open('retourdom.csv', 'wb').write(r.content)