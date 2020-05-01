.PHONY: venv install test-install test test-integ test-docker clean nopyc

venv:
	@python --version || (echo "Python is not installed, please install Python 2 or Python 3"; exit 1);
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; pip install -r requirements.txt

test-install: install
	. venv/bin/activate; pip install -r test/requirements.txt

test: test-install

test-integ: test
	. venv/bin/activate; coverage run -m unittest discover

version ?= latest
test-docker:
	curl -s https://raw.githubusercontent.com/sendgrid/sendgrid-oai/master/prism/prism.sh | version=$(version) bash

clean: nopyc
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete
