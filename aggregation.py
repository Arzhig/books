def aggreg(sources:dict):
    final = {}
    for source in sources:
        for key in source.getkeys():
            if type(final[key]) == None :
                final[key]=source[key]
            elif final[key] != source[key]:
                choices = [final[key],source[key]]
                print("Collision pour l'entrée " + key)
                print("Choix 1 : ", source[key])
                print("Choix 2 : " final[key])
                choice = 0
                while choice != 0 or choice != 1 :
                    choice = int(input("Tapez 1 ou 2 :")) - 1
                    if choice !=0 or choice !=1:
                        print("Caleur incorrecte")
                final[key]=choices[choice]
