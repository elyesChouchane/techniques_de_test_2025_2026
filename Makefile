test:
	pytest

unit_test:
	pytest -m "not performance"

perf_test:
	pytest -m performance

coverage:
	coverage run -m pytest -m "not performance"
	coverage report

lint:
	ruff check .

doc:
	pdoc3 src --html --output-dir docs --force