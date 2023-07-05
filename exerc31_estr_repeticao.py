#Q31_https://wiki.python.org.br/EstruturaDeRepeticao
# lojas tabajara
print('Bem-vindo as LOJAS TABAJARA.')
print   ('CUPOM FISCAL')
#vlp=float()
i=1
soma=0
while True:
      print('Item',i,'R$:')
      vlp=float(input())
      soma+=vlp
      i+=1
      if vlp==0:
           False
           break

print('TOTAL R$: ',soma,'\n')
pg=float(input('Dinheiro R$: '))
troc=float(pg - soma)
trocr=round(troc,2)
print('Troco R$: ',trocr)
        
        