n1 = int(input('Digite A Nota De Av1 !'))
n2 = int(input('Digite A Nota De Av2 !'))
media = (n1 + n2)/2
if media >= 6:
    print('Aprovado\nNota de Av1 = {}, Nota de Av2 = {}, media = {}'.format(n1,n2,media))
else:
    print('Reprovado\nNota de Av1 = {}, Nota de Av2 = {}, media = {}'.format(n1,n2,media))
