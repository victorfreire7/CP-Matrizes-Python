temperaturas = [
    [28, 31, 34, 33], # Sala 1
    [25, 27, 29, 28], # Sala 2
    [32, 35, 36, 34], # Sala 3
    [24, 26, 25, 27]  # Sala 4
]

arraymedias = []
arraycriticos = [0, 0, 0, 0]
maiorrisco = 0

for i in range(len(temperaturas)): # acessando cada linha
    media = 0 

    for j in range(len(temperaturas)): # acessando cada valor de cada linha
        if temperaturas[i][j] >= 33: 
            arraycriticos[i] += 1 # se a temperatura for maior ou igual a 33, eu vou adicionar 1 ponto no array

        media += temperaturas[i][j]
    
    arraymedias.append(media / len(temperaturas)) # fazendo a media aritmetica da temperatura...

for i in range(len(arraycriticos)): # laço de verificação dos riscos 
    if(arraycriticos[i] > maiorrisco):
        maiorrisco = arraycriticos[i]

for i in range(len(temperaturas)): # laço de prints
    print(f"Sala: {i + 1}")
    print(f"Media: {arraymedias[i]}")
    print(f"Criticos: {arraycriticos[i]}")
    print()

print(f"Sala com maior risco: {maiorrisco}")