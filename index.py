heroi = input("Qual o nome do seu heroi?")
XP_do_heroi = int(input("Quanto de xp seu heróis já coletou nessa temporada?"))
XPTabela = ['Ferro', 0, 1000],['Bronze', 1001, 2000], ['Prata', 2001, 5000],['Ouro', 5001, 7000],['Platina', 7001, 8000],['Ascendente', 8001, 9000],['Imortal', 9001, 10000],['Radiante', 10001, float('inf')]

for i in range(len(XPTabela)):
    if XPTabela[i][1] <= XP_do_heroi <= XPTabela[i][2]:
        XP_do_heroi = XPTabela[i][0]
        break

print (f"O herói do nome de {heroi} Está no nível {XP_do_heroi}")