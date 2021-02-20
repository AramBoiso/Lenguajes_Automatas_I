# [a-z]+([,][a-z]+)+|[a-z]+

def getString(alphabet):

    string = input("Ingrese una cadena par concoer su posicicion: ")[::-1]
    n = len(alphabet)
    increment = 1
    result = 0

    for item in string:
        print(increment, "* ",(alphabet.index(item) + 1) )
        result += increment * (alphabet.index(item) + 1)
        increment *= n
    return result

def getPosition(alphabet):

    position = int(input("Ingrese la posicion de la palabra que desea concocer: "))
    n = len(alphabet)
    positions = 0
    exponent = 0
    before_position = 0
    row_down = []
    row_up = []

    while before_position < position:
        positions = n**exponent
        row_down.append(positions)
        row_up.append(positions + before_position) 
        before_position = positions + before_position
        exponent += 1

    residue = 0
    operation = 0
    pointer = len(row_down) -1
    item = n
    lexeme = []

    while residue != position:
        
        for i in range(n):

            if pointer -1 < 0:
                operation = residue + item * row_down[pointer]
            else:
                operation = residue + item * row_down[pointer] + row_up[pointer -1]

            if operation > position:
                item -= 1
                continue
            else:
                residue = residue + item * row_down[pointer]
                lexeme.append(alphabet[item -1])
            
        item = n        
        pointer -= 1

    return (' '.join(map(str, lexeme)))          

print("\nPor favor ingrese los miembros del alfabeto por comas y sin espacios entre ellos, ejemplo: 'a,b,c,...'")
alphabet = str(input("\nIngrese los mimbros del alfabeto: ")).split(',', -1)
option = 0

while option != 4:

    print("\n alfabeto actual: ", alphabet)

    print("\n1) Conocer posición del lexema: ")
    print("2) Conocer lexema por su posición: ")
    print("3) Cambiar alfabeto")
    print("4) Salir")
    option = int(input("Ingrese una opcion: "))

    if option == 1:
        print(getString(alphabet))
    elif option == 2:
        print(getPosition(alphabet))
    elif option == 3:
        print("\nPor favor ingrese los miembros del alfabeto por comas y sin espacios entre ellos, ejemplo: 'a,b,c,...'")
        alphabet = str(input("\nIngrese los mimbros del alfabeto: ")).split(',', -1)
    elif option == 4:
        print("\nHasta luego :)")
    else:
        print("Por favor, ingrese una opción válida.")
