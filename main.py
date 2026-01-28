import csv
import os

#Limpar terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


#Carregar Pokémon base
def carregar_pokemons():
    try:
        with open("pokemons_1_150.csv", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print("Arquivo pokemons_1_150.csv não encontrado.")
        exit()
    except Exception as e:
        print("Erro ao carregar pokémons:", e)
        exit()

def carregar_pokemonsdescri():
    try:
        with open("pokemon_fire_red_descricoes.csv", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print("Arquivo pokemon_fire_red_descricoes.csv não encontrado.")
        exit()
    except Exception as e:
        print("Erro ao carregar pokémons:", e)
        exit()

pokemons = carregar_pokemons()

pokemonsdescri = carregar_pokemonsdescri()

#Arquivo do time
ARQUIVO_TIME = "time_pokemon.csv"


#Criar arquivo do time
def criar_arquivo_time():
    try:
        if not os.path.exists(ARQUIVO_TIME):
            with open(ARQUIVO_TIME, "w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow(["Número", "Nome", "Tipos"]) #escreve a primeira coluna
    except Exception as e:
        print("Erro ao criar arquivo do time:", e)


#Menu principal
def mostrar_menu():
    print("=== POKÉDEX FIRE RED ===")
    print("1 - Mostrar todos os Pokémon")
    print("n N - Ver Pokémon pelo número (ex: n 6)")
    print("t tipo - Listar Pokémon por tipo (ex: t fire)")
    print("time - Montar time de 10 Pokémon")
    print("ver_time - Ver time atual")
    print("reset_time - Apagar time")
    print("sair - Encerrar\n")


#Montar time (loop contínuo)
def montar_time():
    criar_arquivo_time()

    while True:
        limpar_tela()
        print("=== MONTAR TIME (máx. 10 Pokémon) ===")
        print("Digite o número do Pokémon para adicionar")
        print("Digite 'sair' para voltar ao menu principal\n")

        try:
            with open(ARQUIVO_TIME, encoding="utf-8") as f:
                time_atual = list(csv.DictReader(f))
        except Exception as e:
            print("Erro ao ler o time:", e)
            input("Pressione ENTER para voltar...")
            return

        print(f"Pokémon no time: {len(time_atual)}/10\n")

        if len(time_atual) >= 10:
            print("Seu time já está completo.")
            input("Pressione ENTER para voltar ao menu...")
            return

        comando = input("Número do Pokémon > ").strip().lower()

        if comando == "sair":
            return

        if not comando.isdigit():
            print("Número inválido.")
            input("Pressione ENTER para continuar...")
            continue

        numero = int(comando)

        if numero < 1 or numero > len(pokemons):
            print("Número fora da Pokédex.")
            input("Pressione ENTER para continuar...")
            continue

        pokemon = pokemons[numero - 1]

        if any(p["Número"] == pokemon["Número"] for p in time_atual):
            print("Esse Pokémon já está no time.")
            input("Pressione ENTER para continuar...")
            continue

        try:
            with open(ARQUIVO_TIME, "a", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow([pokemon["Número"], pokemon["Nome"], pokemon["Tipos"]])
        except Exception as e:
            print("Erro ao salvar Pokémon:", e)
            input("Pressione ENTER para continuar...")
            continue

        print(f"{pokemon['Nome']} adicionado ao time.")
        input("Pressione ENTER para continuar...")


#Ver time
def ver_time():
    if not os.path.exists(ARQUIVO_TIME):
        print("Você ainda não montou um time.")
        return

    try:
        with open(ARQUIVO_TIME, encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            print("\n=== SEU TIME ===")
            for p in leitor:
                print(f"{p['Número']} - {p['Nome']} ({p['Tipos']})")
            print()
    except Exception as e:
        print("Erro ao ler o time:", e)

# Resetar time
def resetar_time():
    try:
        if os.path.exists(ARQUIVO_TIME):
            os.remove(ARQUIVO_TIME)
            print("Time apagado com sucesso.")
        else:
            print("Nenhum time para apagar.")
    except Exception as e:
        print("Erro ao apagar o time:", e)


# Loop principal
while True:
    limpar_tela()
    mostrar_menu()

    comando = input("Digite aqui > ").strip().lower()

    if comando == "sair":
        break

    if comando == "1":
        for p in pokemons:
            print(f"{p['Número']} - {p['Nome']} ({p['Tipos']})")
        input("\nPressione ENTER para continuar...")
        continue

    if comando.startswith("n "):
        num = comando.split()[1] #Segunda parte do comando pego

        if num.isdigit():
            num = int(num)
            if 1 <= num <= len(pokemonsdescri):
                p = pokemonsdescri[num - 1]
                print(f"\n Número: {p['numero']} == {p['Nome']} \n Tipos:{p['Tipo 1']} {p['Tipo 2']} \n Altura/peso: {p['Altura']} m, Kg {p['Peso']} \n Descrição: '{p['Descrição']}' \n")
            else:
                print("Número fora da Pokédex.")
        else:
            print("Número inválido.")

        input("Pressione ENTER para continuar...")
        continue

    if comando.startswith("t "):
        tipo = comando.split()[1]
        print(f"\nPokémon do tipo {tipo.title()}:\n")

        for p in pokemons:
            if tipo in p["Tipos"].lower():
                print(f"{p['Número']} - {p['Nome']}")

        input("\nPressione ENTER para continuar...")
        continue

    if comando == "time":
        montar_time()
        continue

    if comando == "ver_time":
        ver_time()
        input("Pressione ENTER para continuar...")
        continue

    if comando == "reset_time":
        resetar_time()
        input("Pressione ENTER para continuar...")
        continue

    print("Comando não reconhecido.")
    input("Pressione ENTER para continuar...")
