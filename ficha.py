def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombre_completo = input("Ingrese nombre: ")
    email = input("Ingrese email: ")
    nota1 = int(input("Ingrese nota 1: "))
    nota2 = int(input("Ingrese nota 2: "))
    nota3 = int(input("Ingrese nota 3: "))

    print("""========================
    FICHA DEL ALUMNO
========================""")
    print(f"Nombre: {nombre_completo.strip().title()}")
    print(f"Email: {email.strip().lower()}")
    print(f"Caracteres en nombre: {len(nombre_completo.strip())}")
    print(f"Iniciales: {nombre_completo.strip().upper()[0]}{nombre_completo.strip().upper()[nombre_completo.strip().find(" ") + 1]}")
    print(f"Usuario: {nombre_completo.strip().lower() [nombre_completo.strip().find(" ") + 1: ]}.{nombre_completo.strip().lower()[0:nombre_completo.strip().find(" ") + 1].strip()}")
    print(f"Email valido: {"@" in email}")
    print(f"Dominio: {email.lower()[email.find("@") + 1:]}")
    print( f"Nombre para archivo: {nombre_completo.strip().title().replace(' ','_')}")
    print(f"Cantidad de a: {nombre_completo.lower().strip().count('a')}")
    print(f"Codigo secreto: {nombre_completo.strip().upper()[ : :-1]}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {nota1 + nota2 + nota3}")
    print(f"Promedio: {(nota1 + nota2 + nota3)/3}")
    print(f"Promedio entero: {(nota1 + nota2 + nota3)//3}")
    print("="*24)