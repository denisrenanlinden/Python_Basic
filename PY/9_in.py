# Função de String in no Python

print("===============================================")

# Recebe um texto do usuário
texto = input("Digite um texto: ")

# Recebe uma palavra para verificar se está no texto
palavra = input("Digite uma palavra para verificar se está no texto: ")

# Verifica se a palavra está no texto
if palavra in texto:
    print(f"A palavra '{palavra}' está no texto.")
else:
    print(f"A palavra '{palavra}' não está no texto.")

print("===============================================")
