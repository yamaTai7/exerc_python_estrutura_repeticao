#Q30_https://wiki.python.org.br/EstruturaDeRepeticao
# TABELA DE PREÇOS padaria
print('Bem-vindo a PADARIA PÃO CERTO.')
print   ('TABELA DE PREÇOS')
n_itens = int(input("Informe o número de PÃES: ") )
vl_pao  = float(input('Informe o valor do pão (und): '))
vl_paor=round(vl_pao,2)

if n_itens>50:
        print('Quntidade inválida. Escolha até 50.\n')
        exit()
i=0        
for i in range(1,51):
    print(i,'-- R$ ',round(vl_paor*i,2))
    if i==n_itens:
        print('Total R$ ',round(vl_paor*n_itens,2),'\n')
        exit()
        
        