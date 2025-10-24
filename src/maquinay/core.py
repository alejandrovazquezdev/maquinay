"""
Módulo core con funcionalidad principal del proyecto.
"""


def saludar(nombre: str = "mundo") -> str:
    """
    Función para saludar.

    Args:
        nombre: El nombre a saludar. Por defecto es "mundo".

    Returns:
        Un mensaje de saludo.

    Examples:
        >>> saludar()
        'Hola mundo'
        >>> saludar("Python")
        'Hola Python'
    """
    return f"Hola {nombre}"


def main() -> None:
    """
    Función principal del programa.
    """
    mensaje = saludar()
    print(mensaje)


if __name__ == "__main__":
    main()
