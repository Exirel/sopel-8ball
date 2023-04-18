.PHONY: qa quality test coverages coverage_report coverage_html pylint

quality:
	isort sopel_8ball
	flake8

test:
	coverage run -m pytest -v .

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
	pip install -e .

# DO NOT RUN INSIDE VIRTUALENV
build:
	rm -rf build/ dist/
	python3 -m build --sdist --wheel --outdir dist/ .
