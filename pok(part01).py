import random
pokebolas = []
pokedex = ['nada','nada','nada','nada']
pokeFloresta = ['Caterpie','Pinsir','Pineco','Wurmple','Wurmple','Wurmple','Silcoon','Silcoon','Silcoon','Cascoon','Volbeat','Illumise','Kricketot','Illumise','Caterpie','Caterpie','Caterpie','Pinsir','Pineco','Pineco']
pokeCaverna = ['Diglett','Cubone','Nosepass','Gigalith','Geodude','Geodude','Geodude','Nosepass','Nosepass','Diglett','Diglett']
while True:
    nome = input("Olá me chame de professor carvalho, seu nome é ?\n")
    print(f"perfeito {nome}, sua jornada pokémon se iniciará agora.... mas antes você precisará de um equipamento próprio para caçar pokémons\n(x4 pokébolas adquiridas)")
    x = ("pokebola")
    pokebolas.append(x)
    pokebolas.append(x)
    pokebolas.append(x)
    pokebolas.append(x)
    while True:
        print("Escolha uma ação:\n|1.Ir para floresta |\n|2.Ir para a caverna|\n|3.     Pokedex     |\n|4.Reiniciar o jogo |\n|5.  Sair do jogo   |\n|6.    Pokebolas    |")
        acao = int(input("Selecione uma ação: "))
        if acao <1 or acao > 6:
            print("Esta função não existe selecione novamente:")
            continue
        if acao == 1:
            if len(pokebolas) == 0:
                print(f"você possui 0 pokebolas para caçar pokémons.")
                continue
            else:
                while True:
                    x = random.randint(0,19)
                    if pokedex[0] == pokeFloresta[x] or pokedex[1] == pokeFloresta[x] or pokedex[2] == pokeFloresta[x]:
                        print(f"Você já capturou o pokémon {pokeFloresta[x]}...retornando para casa.")
                        break
                    else:
                        while True:
                            print(f"Um {pokeFloresta[x]} Selvagem apareceu o que você faz ?\n|1.Tentar capturar.|\n|2.     Fugir.     |")
                            acao2 = int(input("Selecione uma ação: "))
                            if acao2 < 1 or acao2 > 2:
                                print("Ação inválida selecione novamente")
                                continue
                            elif acao2 == 1:
                                y = random.randint(1,2)
                                if y == 1:
                                    pokedex.pop(0)
                                    pokedex.append(pokeFloresta[x])
                                    print(f"você capturou o pokémon {pokeFloresta[x]}....retornando para casa.")
                                    pokebolas.pop()
                                    break
                                else:
                                    print(f"O pokémon {pokeFloresta[x]} fugiu....retornando para casa.")
                                    pokebolas.pop()
                                    break
                            else:
                                print("você volta para casa.")
                                break
                    break
            continue
        if acao == 2:
            if len(pokebolas) == 0:
                print(f"você possui 0 pokebolas para caçar pokémons.") 
                continue
            else:
                while True:
                    x = random.randint(0,9)
                    if pokedex[0] == pokeCaverna[x] or pokedex[1] == pokeCaverna[x] or pokedex[2] == pokeCaverna[x]:
                        print(f"Você já capturou o pokémon {pokeCaverna[x]}...retornando para casa.")
                        break
                    else:
                        while True:
                            print(f"Um {pokeCaverna[x]} Selvagem apareceu o que você faz ?\n|1.Tentar capturar.|\n|2.     Fugir.     |")
                            acao2 = int(input("Selecione uma ação: "))
                            if acao2 < 1 or acao2 > 2:
                                print("Ação inválida selecione novamente")
                                continue
                            elif acao2 == 1:
                                y = random.randint(1,100)
                                if y<=35:
                                    pokedex.pop(0)
                                    pokedex.append(pokeCaverna[x])
                                    print(f"você capturou o pokémon {pokeCaverna[x]}....retornando para casa.")
                                    pokebolas.pop()
                                    break
                                else:
                                    print(f"O pokémon {pokeCaverna[x]} fugiu....retornando para casa.")
                                    pokebolas.pop()
                                    break
                            else:
                                print("você volta para casa.")
                                break
                    break
            continue
        if acao == 3:
            print(pokedex)
            continue
        if acao == 6:
            print(f"{len(pokebolas)} pokebolas no bolso.")
            continue
        if acao == 4 or acao == 5:
            pokedex.pop()
            pokedex.pop()
            pokedex.pop()
            pokedex.pop()
            pokedex.append('nada')
            pokedex.append('nada')
            pokedex.append('nada')
            pokedex.append('nada')
            break
    if acao == 5:    
        break
    if acao == 4:
        continue