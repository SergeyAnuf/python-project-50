install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

lint:
	uv run ruff check

check: test lint

build:
	uv build
	
package-install:
	uv tool install dist/*.whl
	
.PHONY: install run test lint test-coverage check build package-install
