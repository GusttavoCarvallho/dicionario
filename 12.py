votos = {}

while True:
    candidato = input("Digite o nome do candidato(ou 'fim' para encerrar):")
    if candidato == "fim":
        break 
    
    
    # verificar se o candidato ja recebeu  votos antes 
    
    if candidato in votos:
        votos[candidato] +=1
        
    else:
        votos[candidato] = 1
        
# imprime o resultado

print('Resultado da votaçao:')
for candidato, quantidade in votos.items():
    print(candidato,"-",quantidade ,'votos')
     
print(votos)