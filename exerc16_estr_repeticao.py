#Q16_https://wiki.python.org.br/EstruturaDeRepeticao
# série de Fibonacci até 501
n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1
count=3
print(1)
print(1)
while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        if termo <= 501:
            print(termo)
            count += 1
