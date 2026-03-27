def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre = input("nombre:")
    print(f"contiene a: {"a" in nombre.lower()}")
    print(f"contiene e: {"e" in nombre.lower()}")
    print(f"contiene i: {"i" in nombre.lower()}")
    print(f"contiene o: {"o" in nombre.lower()}")
    print(f"contiene u: {"u" in nombre.lower()}")