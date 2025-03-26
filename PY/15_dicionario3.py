# Continuano Dicionário no Python


lista_de_alunos = {
    'nome': 'Matheus',
    'idade': 25,
    'altura': 1.75,
    'peso': 80,
    'sexo': ('Masculino', 'Feminino', 'Outros'),
}

print('==================================================================================================')

# Atualizando um elemento no Dicionário
lista_de_alunos['nome'] = 'João'
lista_de_alunos.update({'idade': 30})
print(lista_de_alunos)
