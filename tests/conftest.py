"""
Configuración de pytest y fixtures compartidos.
"""

import pytest


@pytest.fixture
def nombre_ejemplo():
    """Fixture que proporciona un nombre de ejemplo."""
    return "Usuario de Prueba"


# Aquí puedes agregar más fixtures que se usarán en varios tests
