carros = ["fusca", "gol", "uno", "vectra", "peugeout"]
consumo = [7, 10, 12.5, 9, 14.5]

custo_combustivel = 2.25
distancia = 1000

menor_consumo = consumo[0]
indice_menor_consumo = 0

print("Comparativo de Consumo de Combustível\n")
for i in range(len(carros)):
    litros_necessarios = distancia / consumo[i]
    custo_total = litros_necessarios * custo_combustivel
    print(f"{i+1} - {carros[i].capitalize():<15} - {consumo[i]:>5.1f} - {litros_necessarios:>7.1f} litros - R$ {custo_total:.2f}")
    if consumo[i] > menor_consumo:
        menor_consumo = consumo[i]
        indice_menor_consumo = i

print("\nRelatório Final")
print(f"O menor consumo é do {carros[indice_menor_consumo].capitalize()}.")
