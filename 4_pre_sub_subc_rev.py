


#All prefixs of the string


#All subprefixs of the string


#All substrings of the string

#String reverse


def getSubStr( limit, string ):
    for char in range(limit + 1):
        if(char == 0):
            response = string[char]
        else:
            response += string[char]
    return response

string = input('Plase, enter any string: ')

for x in range(len(string)):
    #sub string
    aux = getSubStr( x, string)

    for c in string:
        
