#Q15_https://wiki.python.org.br/EstruturaDeRepeticao
# série de Fibonacci
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
        print(termo)
        count += 1