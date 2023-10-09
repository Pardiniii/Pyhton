import random


def jogar():
    # boas vindas

    print("*************")
    print("Bem vindo ao jogo de adivinhacao!")
    print("*************\n\n")
    print("Vou sortear um numero (entre 1 e 100) e voce precisara acerta-lo em ate 5 tentativas!")
    print("Voce comecara com 1000 pontos, porem a cada chute errado voce vai perdendo pontos.")
    print("Boa sorte!\n")

    # inicializacao de variaveis

    aleatorio = random.randint(1, 100)
    total_de_tentativas = 0
    tentativas = 0
    rodada = 1
    chute = 0
    pontos = 1000

    # steando a dificuldade

    print("Escolha a dificuldade:")
    print("(1) Facil  (2) Medio  (3) Dificil")
    nivel = int(input("Digite sua escolha:"))

    if nivel == 1:
        total_de_tentativas = 10
        tentativas = 10
    elif nivel == 2:
        total_de_tentativas = 5
        tentativas = 5
    else:
        total_de_tentativas = 3
        tentativas = 3

    # laco do jogo

    while tentativas > 0:
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite seu chute:")
        chute = int(chute_str)

        acertou = chute == aleatorio
        maior = chute > aleatorio
        if acertou:
            print("Voce acertou! Pontuacao final: {} pontos.".format(pontos))
            break
        else:
            if maior:
                print("Voce errou! Seu chute foi maior que o numero secreto")
            else:
                print("Voce errou! Seu chute foi menor que o numero secreto")
            tentativas = tentativas - 1
            rodada = rodada + 1
            pontos_perdidos = abs(aleatorio - chute)
            pontos = pontos - pontos_perdidos

    # finalizacao

    if chute == aleatorio:
        print("Fim do jogo, obrigado por jogar.")
    else:
        print("Fim do jogo, o numero aleatorio era {}. Obrigado por jogar.".format(
            aleatorio))


if __name__ == "__main__":
    jogar()
