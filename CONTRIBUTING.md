# Guía de Contribución

Gracias por tu interés en contribuir a Maquinay.

## Cómo Contribuir

### Reportar Bugs

Si encuentras un bug:

1. Verifica que no exista ya un issue sobre el mismo problema
2. Crea un nuevo issue con una descripción detallada
3. Incluye pasos para reproducir el problema
4. Menciona tu versión de Python y sistema operativo

### Sugerir Mejoras

Para sugerir nuevas características:

1. Abre un issue describiendo la característica
2. Explica por qué sería útil
3. Proporciona ejemplos de uso si es posible

### Pull Requests

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Realiza tus cambios
4. Asegúrate de que los tests pasen
5. Agrega tests para tu nueva funcionalidad
6. Actualiza la documentación si es necesario
7. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
8. Push a la rama (`git push origin feature/nueva-caracteristica`)
9. Abre un Pull Request

## Estándares de Código

### Estilo

Seguimos las siguientes guías de estilo:

- [PEP 8](https://pep8.org/) para el estilo de código Python
- Usamos `black` con líneas de 88 caracteres
- Usamos `isort` para ordenar imports
- Usamos type hints cuando sea posible

### Formateo

Antes de hacer commit, ejecuta:

```bash
black src/ tests/
isort src/ tests/
```

### Linting

Asegúrate de que tu código pase los linters:

```bash
flake8 src/ tests/
mypy src/
```

### Tests

- Todos los nuevos features deben incluir tests
- Mantener la cobertura de tests arriba del 80%
- Los tests deben ser claros y bien documentados

```bash
pytest --cov=maquinay --cov-report=term
```

## Estructura de Commits

Usa mensajes de commit claros y descriptivos:

```
tipo: descripción corta

Descripción más detallada si es necesario.

- Punto adicional 1
- Punto adicional 2
```

Tipos de commit:
- `feat`: Nueva característica
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Cambios de formato (sin cambios de código)
- `refactor`: Refactorización de código
- `test`: Agregar o modificar tests
- `chore`: Tareas de mantenimiento

## Proceso de Revisión

1. Un mantenedor revisará tu PR
2. Puede haber comentarios o solicitudes de cambios
3. Una vez aprobado, tu PR será merged

## Preguntas

Si tienes preguntas, no dudes en:
- Abrir un issue
- Contactar a los mantenedores

## Código de Conducta

Este proyecto sigue un código de conducta. Al participar, se espera que lo respetes.

## Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo la misma licencia que el proyecto (MIT).
