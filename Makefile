lint:
	uv run ruff check ./mycli ./main.py

mypy:
	uv run mypy ./mycli ./main.py --check-untyped-defs