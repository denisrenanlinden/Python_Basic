# Utilizando o Input com Python

nome_do_filme = input("Nome do Filme: ")
ano_lancamento = int(input("Ano de Lançamento: "))
nota_do_filme = float(input("Nota do Filme: "))
streaming_disponivel = input("Streaming Disponivel: ")
#multiplataforma = bool(input("Multiplataforma: ")) Maneira incorreta de tratar Boleano

print("\n")
print("Exibindo os Tipos de Dados: \n")
print(type(nome_do_filme))
print(type(ano_lancamento))
print(type(nota_do_filme))
print(type(streaming_disponivel))
# print(type(multiplataforma)) Não adianta imprimir esse Boleano, sempre terá True no resultado

print("\n")
print("Exibindo os Dados: \n")
print("Nome do Filme:", nome_do_filme)
print("Ano de Lançamento:", ano_lancamento)
print("Nota do Filme:", nota_do_filme)
print("Streaming Disponível:", streaming_disponivel)
# print("Multiplataforma:", multiplataforma) Vai imprimir sempre True

# Recebendo um valor booleano corretamente
valor_booleano = input("Digite 'True' ou 'False': ").strip().capitalize()
if valor_booleano == "True":
    valor_booleano = True
elif valor_booleano == "False":
    valor_booleano = False
else:
    valor_booleano = None  # Valor inválido

print("Valor Booleano Recebido:", valor_booleano)
