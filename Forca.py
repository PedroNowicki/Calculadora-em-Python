#João Pedro Mendes Nowicki - Matricula: 202308232746.
#Rafael Kahl Konorath - Matricula: 202308232711.
import random
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    tentativas_max = 6
    letras_tentadas = []
    print("Bem-vindo ao jogo da Forca!!!")
    print("Tente adivinhar a palavra relacionada a tecnologia, tenha em mente que algumas palavras estão em Ingles!")
    while tentativas < tentativas_max:
        print("\n" + " ".join(palavra_oculta))
        letra = input("Digite uma letra: ").lower()
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Por Favor tente outra.")
            continue
        letras_tentadas.append(letra)
        if letra in palavra:
            for idx, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[idx] = letra
        else:
            tentativas += 1
        exibir_forca(tentativas)
        
        if "_" not in palavra_oculta:
            print("\nParabéns!! Você adivinhou a palavra:", palavra)
            break
    else:
        print("\nEnforcado! A palavra era:", palavra)
    print("Obrigado por jogar!!")
jogar()

def escolher_palavra():
    palavras = [
        "array", "ascii", "backup", "bit", "bytes", "cache", "chip", "nuvem", "dados", "debug",
        "digito", "domino", "driver", "email", "fibra", "fila", "flood", "frame", "input", "link",
        "login", "memoria", "modem", "rede", "robo", "token", "usb", "virus", "wifi", "Estacio"
    ]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        """
           -----
           |   |
           |
           |
           |
           |
        ---------
        """,
        """
           -----
           |   |
           |   O
           |
           |
           |
        ---------
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           |
        ---------
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        ---------
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |
           |
        ---------
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        ---------
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        ---------
        """
    ]
    print(estagios[tentativas])