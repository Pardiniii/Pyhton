import time
import Forca
import adivinhacao

def escolha_jogo():
    print("\n**************")
    print("Bem vindo!")
    print("Escolha o que vai jogar hoje:")
    print("**************\n")

    jogo = 0

    while jogo != 1 or jogo != 2 or jogo == 3:
        jogo = int(
            input("\n(1) Jogo da Forca  (2) Jogo da adivinhacao  (3) Sair"))

        if jogo == 1:
            print("Abrindo o jogo da forca...")
            time.sleep(2)
            Forca.jogar()
        elif jogo == 2:
            print("Abrindo o jogo da adivinhacao...")
            time.sleep(2)
            adivinhacao.jogar()
        elif jogo == 3:
            print("Ate logo!")
            time.sleep(1)
            break
        else:
            print("Digite um numero valido.")


if __name__ == "__main__":
    escolha_jogo()
