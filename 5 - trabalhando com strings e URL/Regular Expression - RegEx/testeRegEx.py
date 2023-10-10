import re

endereco = "Rua professor guilherme belfort sabino, 04678-002, 1524, 52/2, campininha, SP "

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco) 
if busca:
    cep = busca.group()
    print(cep)
else:
    print("Erro")