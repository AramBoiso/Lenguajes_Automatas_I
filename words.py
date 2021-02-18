print("Por favor ingrese los miembos del alafabeto por comas y sin espacios entre ellos, ejemplo: 'a,b,c,...'")
alphabet = str(input("Ingrese los mimbros del alfabeto: ")).split(',', -1)
    
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

print(' '.join(map(str, lexeme)))          