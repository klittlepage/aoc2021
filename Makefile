.PHONY: format
format:
	poetry run autopep8 -i -r aoc tests

.PHONY: lint
lint:
	poetry run flake8 aoc tests
	poetry run mypy aoc tests

.PHONY: test
test:
	poetry run pytest
