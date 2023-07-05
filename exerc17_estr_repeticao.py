
#Q17_https://wiki.python.org.br/EstruturaDeRepeticao
# fatorial
numero = int(input("Fatorial de: ") )

resultado=1
for n in range(1,numero+1):
    resultado *= n

print(numero,'!=',resultado)
