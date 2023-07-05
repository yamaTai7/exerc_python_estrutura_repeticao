#Q1_https://wiki.python.org.br/EstruturaDeRepeticao
# NOTA VÁLIDA
n=float(input('Entre com a nota:'))

while n < 0.0 or n > 10.0: 
    print('Informe uma nota válida de 0 a 10.')
    n=float(input('Entre com a nota:'))
    if n >=0.0 and n<=10.0:
       print('Nota válida!')