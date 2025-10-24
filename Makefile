.PHONY: help install install-dev test coverage lint format clean build docs

help:
	@echo "Comandos disponibles:"
	@echo "  make install      - Instalar el paquete"
	@echo "  make install-dev  - Instalar con dependencias de desarrollo"
	@echo "  make test         - Ejecutar tests"
	@echo "  make coverage     - Ejecutar tests con reporte de cobertura"
	@echo "  make lint         - Ejecutar linters (flake8, mypy)"
	@echo "  make format       - Formatear código (black, isort)"
	@echo "  make clean        - Limpiar archivos generados"
	@echo "  make build        - Construir el paquete"
	@echo "  make docs         - Generar documentación"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	pytest

coverage:
	pytest --cov=maquinay --cov-report=html --cov-report=term

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/ examples/
	isort src/ tests/ examples/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

docs:
	cd docs && make html
