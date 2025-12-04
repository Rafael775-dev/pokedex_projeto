import csv
import os

def limpar_tela():
    # Limpa o terminal de forma compatível com Windows, Linux e Mac
    os.system('cls' if os.name == 'nt' else 'clear')

# Lê o CSV principal e guarda tudo em uma lista
pokemons = []
with open("pokemons_1_150.csv", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        pokemons.append(linha)

print("Digite '1' para mostrar toda a lista. ")
print("Digite 'pk n' para ver o pokémon do número N, ex: (pk 2). ")
print("Digite '2' para mostrar os pokémon separados por tipo ")
print("Digite 'pkm tipo' para ver pokémon daquele tipo. ")
print("Exemplo: 'pokm ghost'")
print("Digite 'sair' para encerrar.\n")

while True:
    print("Digite '1' para mostrar toda a lista. ")
    print("Digite 'pk n' para ver o pokémon do número N, ex: (pk 2). ")
    print("Digite '2' para mostrar os pokémon separados por tipo ")
    print("Digite 'pkm tipo' para ver pokémon daquele tipo. ")
    print("Exemplo: 'pokm ghost'")
    print("Digite 'sair' para encerrar.\n")
    comando = input("Digite aqui ").strip().lower()

    if comando == "sair":
        break

    # Exibir lista inteira
    if comando == "1":
        for p in pokemons:
            print(f"{p['Número']}, {p['Nome']}, {p['Tipos']}")
        print()
        continue

    # Buscar por número
    if comando.startswith("pk"):
        numero = comando.replace("pk", "").replace("pk", "").strip()

        if numero.isdigit():
            numero = int(numero)

            if 1 <= numero <= len(pokemons):
                pokemon = pokemons[numero - 1]
                print(f"{pokemon['Nome']} ({pokemon['Tipos']})\n")
            else:
                print("Número fora da Pokédex.\n")
        else:
            print("Digite um número válido.\n")
        continue

    # ---- NOVA FUNÇÃO: LISTAR POR TIPO ----
    if comando.startswith("pokm"):
        tipo = comando.replace("pokm", "").replace("pokm", "").strip()

        nome_arquivo = f"pokemons_tipo_{tipo}.csv"

        if not os.path.exists(nome_arquivo):
            print("Tipo não encontrado ou arquivo inexistente.\n")
            continue

        lista_tipo = []
        with open(nome_arquivo, encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                lista_tipo.append(linha)

        print(f"\nPokémon do tipo {tipo.title()}:\n")
        for p in lista_tipo:
            print(f"{p['Número']}, {p['Nome']}")
        print()
        continue

    print("Comando não reconhecido.\n")