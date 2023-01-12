"""n = int(input())

while n > 0:

    values = input().split()

    aux = ''
    for digit in values[0][::-1]:
        aux += digit
        if aux == values[1][::-1]:
            print('encaixa')
            break
    else:
        print('nao encaixa')

    aux = ''
    n -= 1"""
    
n = int(input())

while(n > 0):
  valores = input().strip().split(" ")
  if len(valores) > 1:
    A, B = valores[0], valores[1]

    if A[len(A) - len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")
    n -= 1