Nível = input("Qual o nível do seu herói?")
Vitorias = int(input("Quantas vitórias vc teve?"))
Derrotas = int(input("Quantas derrotas tivestes?"))

Ranques = ['Ferro', float('-inf'), 10],['Bronze', 11, 20], ['Prata', 21, 50],['Ouro', 51, 80],['Diamante', 81, 90],['Lendário', 91, 100],['Imortal', 101, float('inf')]

def retornar_saldo(Vitorias, Derrotas):
    return Vitorias - Derrotas

Saldo = retornar_saldo(Vitorias, Derrotas)

for i in range(len(Ranques)):
    if Ranques[i][1] <= Saldo <= Ranques[i][2]:
        Saldo = Ranques[i][0]
        break

print(f"O Herói tem de saldo de {Saldo} está no nível de {Nível}")