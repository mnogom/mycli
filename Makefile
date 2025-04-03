tox:
	uvx tox

test:
	uvx tox run -e 3.11

format:
	uvx ruff format mycli tests
