.PHONY: qa quality test coverages coverage_report coverage_html pylint

quality:
	isort sopel_8ball
	flake8

test:
	coverage run -m py.test -v .

coverage_report:
	coverage report

coverage_html:
	coverage html

coverages: coverage_report coverage_html

pylint:
	pylint sopel_8ball

pyroma:
	pyroma .

mypy:
	mypy sopel_8ball

qa: quality mypy test coverages pylint pyroma

.PHONY: develop build

develop:
	pip install -r requirements.txt
	python setup.py develop

build:
	rm -rf build/ dist/
	python setup.py sdist bdist_wheel
