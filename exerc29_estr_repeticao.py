#Q29_https://wiki.python.org.br/EstruturaDeRepeticao
# TABELA DE PREÇOS
print('Bem-vindo a loja Quase 2.')
print   ('TABELA DE PREÇOS')
n_itens = int(input("Informe o número de itens: ") )
if n_itens>50:
        print('Quntidade inválida. Escolha até 50.\n')
        exit()
i=0        
for i in range(1,51):
    print(i,'-- R$ ',1.99*i)
    if i==n_itens:
        print('Total R$ ',1.99*n_itens,'\n')
        exit()
        