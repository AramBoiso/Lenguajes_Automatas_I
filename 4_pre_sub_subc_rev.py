string = input("Enter any string : ")
string = "∈" + string + "∈"
string_length = len(string)

print("\nAll suffixe's of the "+ string[1:string_length-1]+":")
for position in range(string_length):

    sub = string[0:position + 1]
    sub_length = len(sub)
    count = sub_length -1
    res = sub
    
    for i in range(string_length - sub_length):
        
        if sub_length <= 1:
            if string[i + 1] == "∈":
                break
            sub = string[i + 1]
        else:
            if string[count + 1] == "∈":
                break
            sub = sub[1:sub_length] + string[count + 1]
        

        res += ", " + sub
        count += 1

    if position < string_length -1:
        print("{ " + res + " }")


print("\nAll prefix's of the "+ string[1:string_length-1] +":")
for position in range(string_length):

    sub = string[string_length -1 -position:string_length]
    sub_length = len(sub)
    count = sub_length -1
    count_aux = string_length - sub_length
    res = sub

    for i in range(string_length - sub_length):

        if sub_length <= 1:
            if string[count_aux -1] == "∈":
                break

            sub = string[count_aux -1]   
        else:
            if string[count_aux -1] == "∈":
                break
    
            sub = string[count_aux -1] + sub[0:sub_length -1]
        
        count_aux -= 1
        res += ", " + sub

    if position < string_length -1:
        print("{ " + res + " }")

print("\nAll substring's of the "+ string[1:string_length-1]+":")

for position in range(string_length):

    sub = string[0:position + 1]
    sub_length = len(sub)
    count = sub_length -1
    res = sub
    
    for i in range(string_length - sub_length):
        
        if sub_length <= 1:
            if i == string_length:
                break
            sub = string[i + 1]
        else:
            if i == string_length:
                break
            sub = sub[1:sub_length] + string[count + 1]
        

        res += ", " + sub
        count += 1

    if position < string_length -1:
        print("{ " + res + " }")


print("\nReverse "+string+":")

string_aux = string
count = string_length
res = ""

for position in range(string_length):
    
    res = string_aux[position] + res

    print("W^I = " + string_aux[position:string_length] + " -> " + res)

print("W^I = " + res)   
# print(string[::-1])
