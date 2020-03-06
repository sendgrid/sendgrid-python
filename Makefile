.PHONY: venv install test-install test clean nopyc

venv:
	@python --version || (echo "Python is not installed, please install Python 2 or Python 3"; exit 1);
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; pip install -r requirements.txt

test-install:
	. venv/bin/activate; pip install -r test/requirements.txt

test: test-install
	./test/prism.sh &
	sleep 2
	. venv/bin/activate; python -m unittest discover -v

clean: nopyc
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete
