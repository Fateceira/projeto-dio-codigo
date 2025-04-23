nome = input()
level = int(input())
if level >= 40:
    print (f"Parabéns, valente {nome}! Sua coragem e habilidade são notáveis!")
elif 30 <= level < 40:
    print (f"Quase lá, {nome}! Continue treinando!")
else:
    print (f"Ainda é cedo, jovem {nome}. Treine mais!")