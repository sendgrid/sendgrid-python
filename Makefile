.PHONY: venv install test-install test test-integ test-docker clean nopyc

venv: clean
	@python --version || (echo "Python is not installed, please install Python 2 or Python 3"; exit 1);
	pip install virtualenv
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; pip install -r requirements.txt

test-install: install
	. venv/bin/activate; pip install -r test/requirements.txt

test: test-install
	. venv/bin/activate; coverage run -m unittest discover -s test/unit

test-integ: test
	. venv/bin/activate; coverage run -m unittest discover -s test/integ

version ?= latest
test-docker:
	curl -s https://raw.githubusercontent.com/sendgrid/sendgrid-oai/HEAD/prism/prism.sh -o prism.sh
	version=$(version) bash ./prism.sh

clean: nopyc
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete
