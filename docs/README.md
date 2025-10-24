# Documentación de Maquinay

Esta carpeta contiene la documentación del proyecto.

## Estructura

- `api/`: Documentación de la API
- `guides/`: Guías y tutoriales
- `contributing/`: Información para contribuidores

## Generar Documentación

Para generar la documentación con Sphinx:

```bash
# Instalar sphinx
pip install sphinx sphinx-rtd-theme

# Inicializar sphinx (solo primera vez)
sphinx-quickstart

# Generar HTML
make html
```

## Ver la Documentación

Después de generar, la documentación estará disponible en `docs/_build/html/index.html`.

## Agregar Documentación

1. Crea archivos `.rst` o `.md` en esta carpeta
2. Agrega referencias en `index.rst`
3. Regenera la documentación
