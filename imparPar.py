impar = []
par = []
contPar = 0
contImpar =0

def linha():
    print('-=' * len(par * 2))

n1 = int(input('Digite quantos numeros voçê deseja ?'))

for x in range(1,n1 + 1):
    if (x % 2) == 0:
        par.append(x)
        contPar += 1

    else:
        impar.append(x)
        contImpar += 1

linha()
print('NUMEROS PARES')
print(par)
print(f'TOTAL DE {contPar} NUMEROS PARES')
linha()
print('NUMEROS IMPARES')
print(impar)
print(f'TOTAL DE {contImpar} NUMEROS IMPARES')
linha()

