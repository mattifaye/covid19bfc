make:
	git pull	
	python telechargement.py
#	python datawrapper.py
	git add .
	git commit -m "Update"
	git push origin master
