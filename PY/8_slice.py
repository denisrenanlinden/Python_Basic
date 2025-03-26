# Testando Slices nas Strings com Python

# Definindo uma String
texto = "Testando Slices nas Strings com Python"

print(texto)
print(texto[0:])  # Imprime toda a String
print(texto[:10])  # Imprime do inicio até a posição 10
print(texto[0:6])  # Imprime do inicio até a posição 6
print(texto[7:9])  # Imprime da posição 7 até a posição 9
print(texto[0:20:2])  # Imprime do inicio até a posição 10 pulando de 2 em 2
print(len(texto))  # Imprime o tamanho total da String
print(texto[0:len(texto)])  # Imprime toda a String
print(texto[len(texto)::-1])  # Imprime a String de trás para frente
