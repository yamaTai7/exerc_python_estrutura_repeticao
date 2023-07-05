#Q5_https://wiki.python.org.br/EstruturaDeRepeticao
# Tx de crescimento populacional
popA=int(input('Informe a população da cidade 1: '))
cresc_A=float(input('Informe a taxa de crescimento(%): '))
popB=int(input('Informe a população da cidade 2: '))
cresc_B=float(input('Informe a taxa de crescimento(%): '))

i=0
j=0
somi=0
somj=0
crescA=float(cresc_A/100)
crescB=float(cresc_B/100)

while popA!=popB:
  a=float(popA*crescA)
  popA+=a
  #print(popA)
  somi+=1
  somir=round(somi,0)
  crescB=float(0.015)
  b=float(popB*crescB)
  popB+=b
  #print(popB)
  somj+=1
if popA==popB or popA > popB:
    popAr=round(popA,0)
    popBr=round(popB,0)
    print(popAr)
    print(popBr)
    print('A primeira cidade igualará ou superará a sua população com a da segunda em ',somi,'anos.')