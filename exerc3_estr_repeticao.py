#Q3_https://wiki.python.org.br/EstruturaDeRepeticao
# validação de cadastro
nm=input('Digite seu nome:')
while len(nm) <3: 
    print('Nome deve ter mais de três letras.')
    nm=input('Digite seu nome:')

idade=int(input('Digite sua idade:'))
while idade<0 or idade>150:
    print('A idade deve ser até 150 anos.')
    idade=int(input('Digite sua idade:'))

sl=float(input('Digite seu salário R$:'))
while sl<0:
    print('Seu salário deve ser maior que zero.')
    sl=float(input('Digite seu salário R$:'))

sex=input('Digite seu sexo (m)(f):')
while sex!='m'and sex!='f':
     print('Digite sexo válido.Letra minúscula.')
     sex=input('Digite seu sexo (m)(f):')

est_civ=input('Estado civil (s)(c)(d)(v):')
while est_civ!='s'and est_civ!='c'and est_civ!='d'and est_civ!='v':
    print('Digite estado civil válido. Letra minúscula.')
    est_civ=input('Estado civil (s)(c)(d)(v):')
    
    
    
print(nm,'. Seus dados foram cadastrados com sucesso!')
    

     