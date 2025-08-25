import random

print ("=====JOGO DE AVENTURA: EM BUSCA DO TESOURO PERDIDO=====")


nome  = input("\nDigite seu nome de usuário: ")

print("\nSelecione sua classe: \n")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Arqueiro")

classe = int(input("\nEu escolho o número: "))

if classe == 1:
    classe = str("Guerreiro")

if classe == 2:
    classe = str("Mago")

if classe == 3:
    classe = str("Arqueiro")


hp = int(10) 

print(f"\nSeja Bem-Vindo! Sr(a) {nome} o(a) grande {classe}. Sua jornada começa agora!")
print(f"Você começa com {hp} pontos de vida.\n")

print(f"Há muitas eras, um tesouro lendário foi escondido nas profundezas da Floresta Sombria. Muitos guerreiros tentaram, mas nenhum retornou. Agora, {nome} o(a) grande {classe}, parte de sua vila com coragem no coração e apenas uma missão: conquistar o tesouro perdido!\n")


while hp > 0:
    print(f"Seguindo pela floresta {nome} se depara com a entrada de uma caverna. Diante disso você escolhe:\n")
    print("1 - Entrar na caverna")
    print("2 - Seguir pela floresta")

    escolha = int(input("\nEscreva sua decisão: "))


    if escolha == 1:

        print(f"\n{nome} entra na caverna... O ar fica denso, as tochas apagam sozinhas e o som de passos pequenos ecoa... De repente,")
        print("PUMMMMM!")
        print("GOBLINS surgem das sombras, gritando em uma língua estranha!\n")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Fugir")
        acao = int(input("\nO que deseja fazer: "))

        if acao == 1:
            print("\nVocê ataca corajosamente e vence, mas sofre ferimentos.")
            hp -= 5
        elif acao == 2:
            print("\nVocê se defende e perde pouca vida.")
            hp -= 3
        elif acao == 3:
            print(f"\nJogador(a) {nome} foge covardemente e abandona a missão.")
            print(f"\nFinal neutro! {nome} o {classe} desistiu da busca pelo tesouro.")
            break
        else:
            print("\nEscolha inválida! O inimigo aproveitou a situação e te atacou.")
            hp -= 7
    
    elif escolha == 2:
        print("\nJogador(a) decide seguir pela floresta... O vento sopra forte entre as árvores. Você sente que está sendo observado... Até que entre troncos retorcidos encontra um baú antigo que está trancado")
        print("Para abrir o baú você deve adivinhar o número secreto que está entre 1 e 5!\n")


        numero_secreto = random.randint(1,5)
        tentativa = 0
        chute = 0

        while chute != numero_secreto:
            chute = int(input("Digite seu palpite: "))
            tentativa += 1

            if chute != numero_secreto:
                print("Errado! Tente novamente...")
        print(f"\nParabéns! Você conseguiu abrir o baú em {tentativa} tentativas. Dentro dele você achou uma poção de vida")
        hp += 2
        print(f"Sua vida aumentou para {hp} pontos.")


    if hp <= 0:
        print(f"Game Over! {nome} o {classe} não resistiu a missão e acabou falecendo...")
        break

    print(f"\n{nome} continua avançando... Cada vez mais perto do Tesouro Lendário!")
    print("Enquanto acampava durante a noite, você enxerga no horizonte uma luz dourada que brilha como se os céus abrissem caminho até o tesouro. Seu coração acelera. Será este o destino final?\n")
    print("1 - Seguir até a luz")
    print("2 - Ignorar e continuar explorando")

    escolha_final = int(input("\nSua decisão é: "))

    if escolha_final == 1:
        print(f"\nPARABÉNS! {nome} o {classe} encontrou o TESOURO LENDÁRIO!")
        print("Fim da aventura! Você se tornou um guerreiro lendário")
        break
    
    else:
        print("Você decide continuar explorando... A aventura segue!\n")

print("\n===== FIM DO JOGO =====")        
