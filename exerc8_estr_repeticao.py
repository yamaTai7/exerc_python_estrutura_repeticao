#Q8_https://wiki.python.org.br/EstruturaDeRepeticao
# soma e média

soma=0

for i in range (0,5):
    n=int(input('Digite um número: '))
    soma+=n        
    i+=1
     
print('A somo dos números é ',soma)
print('A média é ',soma/5)