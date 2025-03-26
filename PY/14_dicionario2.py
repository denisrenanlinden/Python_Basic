# Continuano Dicionário no Python


lista_de_alunos = {
    'nome': 'Matheus',
    'idade': 25,
    'altura': 1.75,
    'peso': 80,
    'sexo': ('Masculino', 'Feminino', 'Outros'),
}

print('==================================================================================================')
# Adicionando um novo elemento no Dicionário
lista_de_alunos['cor_dos_olhos'] = 'Castanho'
print(lista_de_alunos)

# Removendo um elemento do Dicionário
del lista_de_alunos['cor_dos_olhos']
print(lista_de_alunos)
print('==================================================================================================')
