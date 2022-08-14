clean:
	rm -rf ./build 
	rm -rf ./dist 
	rm -rf ./th_django_analytics.egg-info 
build: 
	python setup.py sdist 
	python setup.py bdist_wheel 
upload:
	twine  upload  dist/*  
