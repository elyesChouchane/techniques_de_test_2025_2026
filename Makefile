.PHONY: install test unit_test perf_test coverage lint doc run

install:
	pip install -r requirements.txt
	pip install -r dev_requirements.txt

test:
	python -m pytest -v

unit_test:
	python -m pytest -v -m "not perf"

perf_test:
	python -m pytest -v -m perf

coverage:
	coverage run -m pytest
	coverage report -m
	coverage html

lint:
	ruff check .

doc:
	pdoc3 --html --output-dir docs src --force

run:
	python src/app.py