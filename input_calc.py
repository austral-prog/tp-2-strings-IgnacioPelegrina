def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass
    base = int( input("base:"))
    altura = int (input("altura:"))

    area = base * altura
    perimetro = (base + altura)*2

    print (f"\n base: {base} \n altura: {altura} \n area: {area} \n perimetro: {perimetro}")