#Q7_https://wiki.python.org.br/EstruturaDeRepeticao
# maior número

nMaior=0

for i in range (0,5):
    n=int(input('Digite um número: '))
    if n > nMaior:
        nMaior=n
        i+=1
     
print('O número maior é o ',nMaior)