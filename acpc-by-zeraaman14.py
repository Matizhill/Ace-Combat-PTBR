# Ace Combat 1 Pointer Calculator
# Código original feito por: ZeraaMan14
# Mais detalhes em: https://matizhill.com.br

print("ACPC - ZeraaMan14")
print("---------------------------------------------")
print("[1] - Localizar Ponteiro (Texto -> Ponteiro)")
print("[2] - Localizar Texto    (Ponteiro -> Texto)")
opc = int(input("\n[*] - Selecione uma opção: "))
if opc > 2:
    print("Isso não é uma opção válida")
else:
    if opc == 1:
        num = input("[*] Digite o valor do offset: ")
        sum = hex(int(num[0:2], 16) + int("28", 16)) # ZZ
        locate = num[2:4] + sum[2:4]
        invert = locate[1] + locate[0] + locate[2:4] # No final é necessário inverter os valores das posições
        print(f"\nEssa é a localização do ponteiro: [0x{invert}]")
    else:
        print("Exemplo: 0333")
        num = input("[*] Digite o valor do offset: ")
        sub = hex(int(num[2:4], 16) - int("28", 16)) # ZZ
        locate2 = sub[2:4] + num[0:2]
        invert = locate2[0:1] + locate2[2] + locate2[1] # No final é necessário inverter os valores das posições
        print(f"\nEssa é a localização do texto: [0x{invert}]")