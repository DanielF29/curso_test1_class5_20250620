"""
Módulo de Calculadora Básica

Este módulo permite realizar operaciones matemáticas básicas:
suma, resta, multiplicación y división.
"""

from typing import Union

Number = Union[int, float]


def sumar(a: Number, b: Number) -> Number:
    """Devuelve la suma de dos números."""
    return a + b


def restar(a: Number, b: Number) -> Number:
    """Devuelve la resta de dos números."""
    return a - b


def multiplicar(a: Number, b: Number) -> Number:
    """Devuelve el producto de dos números."""
    return a * b


def dividir(a: Number, b: Number) -> Number:
    """
    Devuelve el cociente de dos números.

    Lanza una excepción si se intenta dividir entre cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def main() -> None:
    """Función principal para interactuar con la calculadora."""
    print("Calculadora Básica")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")

    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    operacion = input("Introduce la operación: ").strip().lower()

    try:
        if operacion == "suma":
            resultado = sumar(a, b)
        elif operacion == "resta":
            resultado = restar(a, b)
        elif operacion == "multiplicacion":
            resultado = multiplicar(a, b)
        elif operacion == "division":
            resultado = dividir(a, b)
        else:
            print("Operación no válida.")
            return

        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()