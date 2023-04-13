cadastro = {}
while True:
    nome = input("digite o nome completo")
    if nome == '':
        break
    
    idade = int(input('DIGITE SUA IDADE '))
    cidade = input('digite sua cidade')
    
    #adicionar os dados ao dicionario 
    
    cadastro [nome] = {'idade':idade, 'cidade':cidade}
    
    #imprima o cadastro completo
    
print('cadastro:')
print(cadastro)
for nome, dados in cadastro.items():
    print('-nome:',nome)
    print(' idade:',dados['idade'])
    print('cidade:', dados['cidade'])
    