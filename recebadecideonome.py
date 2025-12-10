import csv
import os

# Lê o CSV principal e guarda tudo em uma lista
pokemons = []
with open("pokemons_1_150.csv", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        pokemons.append(linha)

print("Digite '1' para mostrar toda a lista de Pokémon.")
print("Digite 'n N' para ver o pokémon número N (ex: n 1).")
print("Digite 't tipo' para ver pokémon daquele tipo (ex: t fire).")
print("Tipos: fire, water, grass, bug, electric, ground, ice, ghost, psychic, normal, steel, poison, rock, flying, fighting, dragon")
print("Digite 'sair' para encerrar.\n")

while True:
    comando = input("Digite aqui >  ").strip().lower()

    if comando == "sair":
        break

    # Exibir lista inteira
    if comando == "1":
        for p in pokemons:
            print(f"{p['Número']}, {p['Nome']}, {p['Tipos']}")
        print()
        continue

    # Buscar por número: n 25
    if comando.startswith("n "):
        numero = comando.split()[1]

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

    # ---- LISTAR POR TIPO: t fire ----
    if comando.startswith("t "):
        tipo = comando.split()[1]

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
