#Q2_https://wiki.python.org.br/EstruturaDeRepeticao
# login
usr_nm=input('Digite o nome do usuário:')
usr_snh=input('Digite sua senha:')
if usr_nm != usr_snh:
       print('Login realizado com sucesso!')
while usr_nm == usr_snh: 
    print('Senha inválida.')
    usr_snh=input('Digite sua senha:')
    if usr_nm != usr_snh:
       print('Login realizado com sucesso!')