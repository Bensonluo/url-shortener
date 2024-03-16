.PHONY: style check-style start install develop test load-test
style:
	# apply opinionated styles
	@black api
	@isort api

	# tests are production code
	@black tests
	@isort tests

check-style:
	@black api --check
	@flake8 api --count --show-source --statistics --ignore=E203,W503

start:
	@bash bin/run.sh

install:
	@pip install -r requirements/common.txt

develop:
	@pip install -r requirements/common.txt -r requirements/develop.txt

test:
	@pytest tests
