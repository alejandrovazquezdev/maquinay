# Maquinay

Un proyecto Python con estructura blueprint siguiendo las mejores prácticas.

## Características

- Estructura de proyecto moderna con `src` layout
- Configuración con `pyproject.toml`
- Tests con pytest
- Herramientas de calidad de código (black, flake8, mypy, isort)
- Documentación con Sphinx
- CI/CD ready

## Instalación

### Instalación básica

```bash
pip install -e .
```

### Instalación para desarrollo

```bash
pip install -e ".[dev]"
```

O usando requirements:

```bash
pip install -r requirements-dev.txt
```

## Estructura del Proyecto

```
maquinay/
├── src/
│   └── maquinay/          # Código fuente del paquete
│       ├── __init__.py
│       └── core.py
├── tests/                  # Tests del proyecto
│   ├── __init__.py
│   ├── conftest.py
│   └── test_core.py
├── docs/                   # Documentación
├── scripts/                # Scripts útiles
├── examples/               # Ejemplos de uso
├── pyproject.toml         # Configuración del proyecto
├── setup.py               # Setup para compatibilidad
├── requirements.txt       # Dependencias de producción
├── requirements-dev.txt   # Dependencias de desarrollo
└── README.md              # Este archivo
```

## Uso

```python
from maquinay.core import saludar

# Usar la función
mensaje = saludar("Python")
print(mensaje)  # Output: Hola Python
```

## Desarrollo

### Ejecutar tests

```bash
pytest
```

### Ejecutar tests con cobertura

```bash
pytest --cov=maquinay --cov-report=html
```

### Formatear código

```bash
black src/ tests/
isort src/ tests/
```

### Linting

```bash
flake8 src/ tests/
mypy src/
```

### Ejecutar todas las comprobaciones

```bash
# Formatear
black src/ tests/
isort src/ tests/

# Linting
flake8 src/ tests/
mypy src/

# Tests
pytest --cov=maquinay
```

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para las guías de contribución.

## Licencia

MIT License - ver el archivo [LICENSE](LICENSE) para más detalles.

## Autor

Tu Nombre - tu.email@example.com

## Roadmap

- [ ] Agregar más funcionalidades
- [ ] Mejorar documentación
- [ ] Agregar más tests
- [ ] Configurar CI/CD
