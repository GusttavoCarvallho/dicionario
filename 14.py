estudante = {
    'joao':{
        'idade':18,
        'cidade':'Sao Paulo',
        'notas': [7.5,8.0,9.0]
    },
    'maria':{
        'idade': 20,
        'cidade':'Rio de Janeiro',
        'notas': [6.5,7.0,8.5]
    },
    'pedro':{
        'idade': 19,
        'cidade': 'Belo Horizonte',
        'notas': [8.0,8.5,9.5]
    }
}

print('A idade de joao é:' + str(estudante['joao']['idade']))

# adicionar uma nova nota para maria    

estudante['maria']['notas'].append(9.0)

# imorimir todas as informaçoes 

for estudante, info in estudante.items():
    print(estudante +':')
    print('idade:' + str(info['idade']))
    print('cidade:'+ info['cidade'])
    print('notas:' +str(info['notas']))
    print('media: '+str(sum(info['notas'])/len(info['notas'])))