def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float ( input("dinero gastado:") )
    dinero = int (input("dinero recibido:"))
    print("\nVuelto\n")
    pesos = int (dinero - gasto)
    centavos = int(((dinero - gasto) - pesos)*100)

    print ( f" pesos:\n\t{pesos} " )
    print(f" centavos:\n\t{centavos} ")