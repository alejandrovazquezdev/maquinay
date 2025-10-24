"""
Ejemplo básico de uso del paquete maquinay.
"""

from maquinay.core import saludar


def main():
    """Función principal del ejemplo."""
    # Ejemplo 1: Saludo simple
    print("=== Ejemplo 1: Saludo simple ===")
    mensaje = saludar()
    print(mensaje)
    print()

    # Ejemplo 2: Saludo personalizado
    print("=== Ejemplo 2: Saludo personalizado ===")
    nombres = ["Alice", "Bob", "Charlie", "Python"]
    for nombre in nombres:
        print(saludar(nombre))
    print()

    # Ejemplo 3: Uso interactivo
    print("=== Ejemplo 3: Uso interactivo ===")
    nombre_usuario = input("¿Cómo te llamas? ")
    if nombre_usuario:
        print(saludar(nombre_usuario))
    else:
        print(saludar())


if __name__ == "__main__":
    main()
