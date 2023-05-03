#exemples
from fiche_test import google,amazon
from fuzzywuzzy import fuzz
import copy

sources={'amazon':amazon,'google':google}

def sont_equivalents(attribut:list):
    new_attribut=copy.deepcopy(attribut)
    for i in range(len(attribut)):
        for j in range(len(attribut)):
            if i<j:
                if est_equivalent(attribut[i],attribut[j]):
                    if type(attribut[i])==str:
                        if len(attribut[i])<=len(attribut[j]):
                            try:
                                new_attribut.remove(attribut[i])
                            except:
                                pass
                        else:
                            try:
                                new_attribut.remove(attribut[j])
                            except:
                                pass
                    else:
                        try:
                            new_attribut.remove(attribut[j])
                        except:
                            pass
    return new_attribut


def est_equivalent(attribut1,attribut2):
    if type(attribut1)==str:
        if fuzz.partial_ratio(attribut1,attribut2)>85:
            return True
    else:
        return attribut1==attribut2

def aggreg(sources:dict):
    
    final = {"isbn10"           :"",
             "isbn13"           :"",
             "titre"            :"",
             "sousTitre"        :"",
             "editeur"          :"",
             "auteurs"          :"",
             "fonctions"        :"",
             "date"             :"",
             "genre"            :"",
             "nbPages"          :"",
             "poids"            :0.0,
             "prix"             :0.0,
             "image"            :"",
             "format"           :"",
             "collection"       :"",
             "numeroCollection" :0,
             "serie"            :"",
             "numeroSerie"      :0,
             "reliure"          :"",
             "consultation"     :"",
             "creation"         :""
             }
    
    for source in sources:
        for key in sources[source].keys():
            if final[key]=="" or final[key]==0 :
                final[key]=sources[source][key]
            elif final[key] != sources[source][key]:
                choices = [final[key],sources[source][key]]
                print("Collision pour l'entrée " + key)
                print("Choix 1 : ", sources[source][key])
                print("Choix 2 : ",final[key])
                choice = -1
                while choice <0 or choice > 1 :
                    choice = int(input("Tapez 1 ou 2 :")) - 1
                    if choice <0 or choice >1:
                        print("Valeur incorrecte")
                final[key]=choices[choice]
    return final

priorite = {"isbn10"            :"",
            "isbn13"            :"",
            "titre"             :"",
            "sousTitre"         :"",
            "editeur"           :"",
            "auteurs"           :"",
            "fonctions"         :"",
            "date"              :"",
            "genre"             :"",
            "nbPages"           :"",
            "poids"             :"",
            "prix"              :"",
            "image"             :"",
            "format"            :"",
            "collection"        :"",
            "numeroCollection"  :"",
            "serie"             :"",
            "numeroSerie"       :"",
            "reliure"           :"",
            "consultation"      :"",
            "creation"          :""
            }
#  il faut que les sources soient rempli avec tous les clés mêmes vides pour que cela fonctionne
def aggreg_2(sources:dict,priorite:dict):
    final = {"isbn10":"","isbn13":"","titre":"","sousTitre":"","editeur":"","auteurs":"","fonctions":"","date":"","genre":"","nbPages":"","poids":0.0,"prix":0.0,"image":"","format":"","collection":"","numeroCollection":0,"serie":"","numeroSerie":0,"reliure":"","consultation":"","creation":""}
    for key in final:
        # Si on décide qu'une source a des priorités sur d'autres et que de plus elle soit rempli
        if priorite[key]!="" and (sources[priorite[key]][key]!="" or sources[priorite[key]][key]!=0):
            final[key]=sources[priorite[key]][key]
        else:
            attribut = []
            for source in sources:
                if sources[source][key]!= "" and sources[source][key]!=0 and  sources[source][key]!= None:
                    attribut.append(sources[source][key])
            if len(attribut)==1:
                final[key]=attribut[0]
            elif len(attribut)>1:
                attribut=sont_equivalents(attribut)
                if len(attribut)==1:
                    final[key]=attribut[0]
                else:
                    print("Collision pour l'entrée " + key)
                    for i in range(len(attribut)):
                        print("Choix",i,":",attribut[i])
                    choice = -1
                    while (not (choice in list(range(len(attribut))))):
                        choice = int(input("Donner le numéro voulu "))
                        if (not (choice in list(range(len(attribut))))):
                            print("Valeur incorrecte")
                    final[key]=attribut[choice]

    return final
    
print(aggreg_2(sources,priorite))