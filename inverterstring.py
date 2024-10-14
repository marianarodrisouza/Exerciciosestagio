def inverter_string(string):
    string_invertida = ""
    for char in string:
        string_invertida = char + string_invertida
    return string_invertida

texto = input("Informe a string: ")
print("String invertida:", inverter_string(texto))
