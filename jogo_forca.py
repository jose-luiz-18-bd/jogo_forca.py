import getpass

import random

# Lista de palavras que podem ser a palavra secreta
palavras_possiveis = [
    "python",
    "abacaxi",
    "computador",
    "teclado",
    "banana",
    "montanha",
    "cachorro",
    "tartaruga",
]

# Sorteia uma palavra da lista
palavra_secreta = random.choice(palavras_possiveis).lower()

# getpass deixará a palavra secreta oculta
# palavra_secreta = getpass.getpass("Digite uma palavra 'SECRETA': ")
print("___________________________________________________")
print()
letras_digitadas = []
chances = 7

while True:
    # se o número de chances chegar a 0 exibe a mensagem e encerra a aplicação
    if chances <= 0:
        print("VOCÊ PERDEU!!!")
        print()
        break

    letra = input("Digite uma letra: ").lower()
    print()
    if len(letra) > 1:
        print("Não vale, digite apenas 1 letra!!!")
        print()
        continue

    letras_digitadas.append(letra)

    if letra in palavra_secreta:
        print(f"WOW!!! a letra '{letra}' existe na palavra secreta.")
        print()
    else:
        print(f"AH NÃO!!! a letra '{letra}' não existe na palavra secreta.")
        print()
        letras_digitadas.pop()  # a ultima letra digt que não existir vai ser
        # deletada

    letra_secreta_temporaria = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            letra_secreta_temporaria += letra_secreta
        else:
            letra_secreta_temporaria += "*"

    if letra_secreta_temporaria == palavra_secreta:
        print("WOW, VOCÊ ACERTOU A PALAVRA 'SECRETA'!!!!")
        print()
        print(f"A palavra secreta que não é mais secreta é '{palavra_secreta}'")
        print("___________________________________________________")
        break
    else:
        print(f" A palavra secreta está assim: {letra_secreta_temporaria}")
        print()
    if letra not in palavra_secreta:
        chances -= 1

    print(f"VOCÊ AINDA TEM '{chances}' chance(s)")
    print("___________________________________________________")
    print()
