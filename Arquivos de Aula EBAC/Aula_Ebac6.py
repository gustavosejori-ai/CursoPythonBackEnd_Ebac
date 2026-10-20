import asyncio
import random
import time

async def busca_pokemon_kanto():
    tempo_aleatorio = random.uniform(1, 5)
    await asyncio.sleep(tempo_aleatorio)
    pokemon_aleatorio = random.choice(["Pikachu","Blastoise","Beedrill","Moltres","Mr.Mine"])
    return(pokemon_aleatorio)

async def busca_pokemon_johto():
    tempo_aleatorio = random.uniform(1, 5)
    await asyncio.sleep(tempo_aleatorio)
    pokemon_aleatorio = random.choice(["Floatzel","Tyranitar","Mamoswine","Glalie","Heracross"])
    return(pokemon_aleatorio)

async def busca_pokemon_hoenn():
    tempo_aleatorio = random.uniform(1, 5)
    await asyncio.sleep(tempo_aleatorio)
    pokemon_aleatorio = random.choice(["Gardevoir","Blaziken","Metagross","Aggron","Kyogre"])
    return(pokemon_aleatorio)

async def main():
    tempo_inicial = time.perf_counter()
    resultados = await asyncio.gather(
        busca_pokemon_kanto(),
        busca_pokemon_johto(),
        busca_pokemon_hoenn()
    )
    tempo_final = time.perf_counter()
    tempo_total = tempo_final - tempo_inicial
    print(f"O Pokemon de Kanto e {resultados[0]}")
    print(f"O Pokemon de Johto e {resultados[1]}")
    print(f"O Pokemon de Hoenn e {resultados[2]}")

    print(f"Tempo Total: {tempo_total:.2f} segundos!")

asyncio.run(main())
