venv:
		virtualenv venv

install: venv
		. venv/bin/activate; pip install .

test: venv
		. venv/bin/activate; pip install -r test/requirements.txt; nosetests

clean:
		rm -rf venv/

.PHONY: test clean
