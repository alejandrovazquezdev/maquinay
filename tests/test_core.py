"""
Tests para el módulo core.
"""

import pytest
from maquinay.core import saludar


class TestSaludar:
    """Tests para la función saludar."""

    def test_saludar_sin_parametros(self):
        """Test que saludar sin parámetros devuelve 'Hola mundo'."""
        resultado = saludar()
        assert resultado == "Hola mundo"

    def test_saludar_con_nombre(self):
        """Test que saludar con un nombre devuelve el saludo correcto."""
        resultado = saludar("Python")
        assert resultado == "Hola Python"

    def test_saludar_con_nombre_vacio(self):
        """Test que saludar con nombre vacío funciona."""
        resultado = saludar("")
        assert resultado == "Hola "

    @pytest.mark.parametrize("nombre,esperado", [
        ("Alice", "Hola Alice"),
        ("Bob", "Hola Bob"),
        ("世界", "Hola 世界"),
    ])
    def test_saludar_parametrizado(self, nombre, esperado):
        """Test parametrizado para varios nombres."""
        assert saludar(nombre) == esperado
