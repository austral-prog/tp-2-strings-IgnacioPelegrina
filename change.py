def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = float (input())
    print(gasto)
    print("Dinero recibido")
    dinero = int (input())
    print(dinero)
    print("\nVuelto\n")
    pesos = int (dinero - gasto)
    centavos = round(((dinero - gasto) - pesos)*100)

    print ( f"Pesos:\n{pesos}" )
    print(f"Centavos:\n{centavos}")