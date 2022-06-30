def converte_base_x_para_decimal(numero, simbolos):
    b = len(simbolos)
    t = len(str(numero))
    numero_x = 0

    digits = []
    for i in range (t - 1, -1, -1):
        n = str(numero[i])
        for j in range (b):
            if n == simbolos[j]:
                digits.append(j)

    
    for i in range(t):
        parte = int(digits[i]) * (b ** i)
        numero_x = numero_x + parte
    if len(numero) == 0:
        numero_x = "0"
    return numero_x


def converte_base_decimal_para_base_y(numero, simbolos):
    numero_y = ""
    b= len(simbolos)
    
    while numero > 0:
        d = numero % b
        digit = str(simbolos[d])
        numero_y = digit + numero_y
        numero = int(float(numero) / b)
    if len(numero_y) == 0:
        numero_y = "0"
    return numero_y


def converte_base_x_para_base_y(numero, simbolos_x, simbolos_y):
    decimal = converte_base_x_para_decimal(numero, simbolos_x)
    numero_y = converte_base_decimal_para_base_y(decimal, simbolos_y)
    return numero_y


def main():
    base_x = int(input("Base origem: "))
    if base_x > 1:
        simb_x = input("Símbolos da base origem: ")
        base_y = (input("Base destino: "))
        simb_y = input("Símbolos da base destino: ")
        num = input("Número a converter: ")
        if num != "0":
            num_convertido = converte_base_x_para_base_y(num, simb_x, simb_y)
            print(f"O número na base {base_y} correspondente a {num} da base {base_x} é: {num_convertido}")
        else:
            print(f"O número na base {base_y} correspondente a {num} da base {base_x} é: 0")

if __name__ == "__main__":
    main()