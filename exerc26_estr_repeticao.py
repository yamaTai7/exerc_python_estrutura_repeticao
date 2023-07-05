#Q26_https://wiki.python.org.br/EstruturaDeRepeticao
# eleição
n_eleit = int(input("Informe o número de eleitores: ") )
t_candA=0
t_candB=0
t_candC=0
t_eleit=0
venc=' '
while t_eleit < n_eleit:
    esc=input('Escolha seu candidato (A),(B),(C)? ')
    t_eleit+=1
    if esc =='A':
          t_candA+=1
    if esc =='B':
          t_candB+=1
    if esc =='C':
          t_candC+=1   
          
          
#print(t_candA)
#print(t_candB)
#print(t_candC)
if t_candA > t_candB > t_candC or  t_candA > t_candC > t_candB: 
    venc='A'
    print('O VENCEDOR É O CANDIDATO: ', venc, 'com ', t_candA,' VOTOS.')
if t_candB > t_candC > t_candA or t_candB > t_candA > t_candC:      
    venc='B'
    print('O VENCEDOR É O CANDIDATO: ', venc, 'com ', t_candB,' VOTOS.' )
if t_candC > t_candA > t_candB or  t_candC > t_candB > t_candA:
    venc='C'
    print('O VENCEDOR É O CANDIDATO: ', venc, 'com ', t_candC,' VOTOS.')
if  t_candA == t_candB == t_candC: 
    print('Deu empate! Será feita outra eleição.')   