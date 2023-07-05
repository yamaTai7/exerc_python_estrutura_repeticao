#Q4_https://wiki.python.org.br/EstruturaDeRepeticao
# Tx de crescimento populacional
i=0
j=0
somi=0
somj=0
popA=int(80000)
crescA=float(0.03)
popB=int(200000)
crescB=float(0.015)

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