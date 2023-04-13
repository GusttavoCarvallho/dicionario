produtos = {
    'banana': 2.50,
    'maçã': 3.00,
    'laranja': 4.50,
    'manga': 3.50
}


#imprimir o preço de uma maça 

print('o preço de uma maça é : R$' + str(produtos['maça']))

#adicione um novo produto

produtos['melancia'] = 6.00

#imprima todos os protutos 

for produtos,price in produtos.items():
    print(produtos + ':R$' +str(produtos))