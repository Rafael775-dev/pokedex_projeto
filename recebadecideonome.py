import csv
import os

# Lê o CSV principal e guarda tudo em uma lista
pokemons = []
with open("pokemons_1_150.csv", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        pokemons.append(linha)

print("Digite 'todos os pokémon' para mostrar toda a lista.")
print("Digite 'pokémon N' para ver o pokémon do número N (ex: pokémon 1).")
print("Digite 'todos os pokémon de TIPO' para ver pokémon daquele tipo.")
print("Exemplo: todos os pokémon de fire")
print("Tipos existentes na pokédex:")
print("Fire")
print("Water")
print("Grass")
print("Bug")
print("Eletric")
print("Ground")
print("Ice")
print("Ghost")
print("Psychic")
print("Normal")
print("Steel")
print("Poison")
print("Rock")
print("Flying")
print("Fighting")
print("Dragon")
print("Digite 'sair' para encerrar.\n")

while True:
    comando = input(">> ").strip().lower()

    if comando == "sair":
        break

    # Exibir lista inteira
    if comando == "todos os pokémon":
        for p in pokemons:
            print(f"{p['Número']}, {p['Nome']}, {p['Tipos']}")
        print()
        continue

    # Buscar por número
    if comando.startswith("pokémon ") or comando.startswith("pokemon "):
        numero = comando.replace("pokémon", "").replace("pokemon", "").strip()

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
    if comando.startswith("todos os pokémon de ") or comando.startswith("todos os pokemon de "):
        tipo = comando.replace("todos os pokémon de", "").replace("todos os pokemon de", "").strip()

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

    print("Comando não reconhecido, digite um dos comandos da lista.\n")