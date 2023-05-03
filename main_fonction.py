from scrapping_fonction import *

entree=input("Donner le code ISBN")
fiche_amazon=extraction_amazon(entree)
fiche_google=extraction_google(entree)
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
sources={"amazon":fiche_amazon,"google":fiche_google}
fiche_aggrege=aggregation(sources,priorite)
print(fiche_aggrege)