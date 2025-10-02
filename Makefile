.PHONY: qa quality test coverages coverage_report coverage_html pylint pyroma

quality:
	isort -c sopel_8ball tests
	flake8
	mypy sopel_8ball --follow-untyped-imports

test:
	coverage run -m pytest -v .

coverage_report:
	coverage report

coverage_html:
	coverage html

coverages: coverage_report coverage_html

pylint:
	pylint sopel_8ball || exit 0

pyroma:
	pyroma .

qa: quality test coverages pylint pyroma

.PHONY: develop build

develop:
	python -m pip install -U pip
	python -m pip install -U --group dev
	python -m pip install -e .

build:
	rm -rf build/ dist/
	python -m build --sdist --wheel --outdir dist/ .
