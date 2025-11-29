#!/bin/bash
# Script para ejecutar todos los tests y verificaciones

set -e

echo "=============================="
echo "Ejecutando formateo de código"
echo "=============================="
black src/ tests/ examples/
isort src/ tests/ examples/

echo ""
echo "========================"
echo "Ejecutando linters"
echo "========================"
flake8 src/ tests/
mypy src/

echo ""
echo "===================="
echo "Ejecutando tests"
echo "===================="
pytest --cov=maquinay --cov-report=html --cov-report=term

echo ""
echo "================================"
echo "Todas las verificaciones pasaron"
echo "================================"
