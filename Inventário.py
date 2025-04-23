Itemdoheroi = str(input("Qual o nome do item que deseja verificar?"))
Quantidadedoitem = int(input("Quanto desse item vc precisa?"))
Inventário = {'espada': 1, 'escudo': 1, 'poção de cura': 6, 'poção de mana': 4, 'pergaminho': 3}
if Itemdoheroi in Inventário:
    if Inventário[Itemdoheroi] >= Quantidadedoitem:
        print("Disponível")
    else:
        print("Indisponível")
