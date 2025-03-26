# Dicionário no Python (Muito parecido com um JSON)


lista_de_alunos = {
    'nome': 'Matheus',
    'idade': 25,
    'altura': 1.75,
    'peso': 80,
    'sexo': ('Masculino', 'Feminino', 'Outros'),
}

print('==================================================================================================')
print(lista_de_alunos)  # Imprime a lista de alunos
print(lista_de_alunos['nome'])
print(lista_de_alunos['idade'])
print(lista_de_alunos['altura'])
print(lista_de_alunos['peso'])
print(lista_de_alunos['sexo'])
print(lista_de_alunos.get('nome'))
print(lista_de_alunos.get('idade'))
print('==================================================================================================')

# imprimir um elemneto da tupla que existe dentro do dicionário
print(lista_de_alunos['sexo'][0])  # Imprime o primeiro elemento da tupla
print('==================================================================================================')
