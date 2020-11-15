def divisao(divisor):
    try:
        print(f'Resultado: {42/divisor}')
    except:
        print('Erro: não pode ser dividido por 0')
print(divisao(2))
print(divisao('x'))
print(divisao(0))
print(divisao(1))
