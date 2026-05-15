temperaturas = [
    [28, 31, 34, 33], # Sala 1
    [25, 27, 29, 28], # Sala 2
    [32, 35, 36, 34], # Sala 3
    [24, 26, 25, 27]  # Sala 4
]

arraymedias = []
arraycriticos = [0, 0, 0, 0]

for i in range(len(temperaturas)):
    media = 0

    for j in range(len(temperaturas)):
        if temperaturas[i][j] >= 33:
            arraycriticos[i] += 1

        media += temperaturas[i][j]
    
    arraymedias.append(media / len(temperaturas))

for i in range(len(temperaturas)):
    print(f"Sala: {i + 1}")
    print(f"Media: {arraymedias[i]}")
    print(f"Criticos: {arraycriticos[i]}")
    print()

maiorrisco = 1
for i in range(len(arraycriticos)):
    if(arraycriticos[i] > maiorrisco):
        maiorrisco = arraycriticos[i];

print(f"Sala com maior risco: {maiorrisco}")


# print(temperaturas)