# %% [markdown]
# Récupération d'une page HTML grâce au code ISBN:

# %% [markdown]
# Importation des librairies nécessaires:

# %%
import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request
import os
import time
import json

# %% [markdown]
# Format de l'URL à rentrer:
# Séparation des cas où l'ISBN est à 10 ou 13 caractères:
# Récupération du lien pour accéder à la page Amazon du produit:

# %%

entree = str(input("Donner le code ISBN  "))
ISBN = ""
entree=entree.replace(" ","").replace("-","")
ISBN=entree

#for char in entree:
#      if char.isdigit():
#      ISBN += char
if len(ISBN)==10:
    url = "https://www.amazon.fr/dp/"+ISBN
elif len(ISBN)==13:
    url1="https://www.amazon.fr/s?k="+ISBN
    try:
        recherche=urllib.request.urlopen(url1,timeout=100)
        soup1=bs(recherche)
        link =str(soup1.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href'])
        indice = link.find("/dp/")
        url="https://www.amazon.fr"+link[indice:]
    except:
        raise FileNotFoundError("Une erreur s'est produite veuillez vérifier votre connexion Internet et rééssayer")
        

else:
    raise SyntaxError("Erreur dans le format du code ISBN")

# %% [markdown]
# Récupérer la page html de la page du produit amazon:

# %%
try:
    page=urllib.request.urlopen(url,timeout=100)
    soup2=bs(page,features="html.parser")
except:
    raise FileNotFoundError("Une erreur s'est produite veuillez vérifier votre connexion Internet et rééssayer")
# %% [markdown]
# Création du dictionnaire pour les attributs du livre:

# %%
fiche={"isbn10":"","isbn13":"","titre":"","sousTitre":"","editeur":"","auteurs":"","fonctions":"","date":"","genre":"","nbPages":"","poids":0.0,"prix":0.0,"image":"","format":"","collection":"","numeroCollection":0,"serie":"","numeroSerie":0,"reliure":"","consultation":"","creation":""}
if len(ISBN)==13:
    fiche["isbn13"]=ISBN
elif len(ISBN)==10:
    fiche["isbn10"]=ISBN
# %% [markdown]
# Récupération du titre:

# %%
try:
    titre = soup2.find('span', {'id': 'productTitle'}).text
    fiche["titre"]=titre.strip()
except:
    pass
# %% [markdown]
# Récupération des auteurs ainsi que fonctions:

# %%
try:
    auteurs=soup2.find_all('span', {'class': 'author notFaded'})
    a=[]
    f=[]
    for auteur in auteurs:
        auteur=auteur.text.replace("\n","").replace(",","")
        a.append(auteur[:auteur.find(" (")])
        f.append(auteur[auteur.find("(")+1:auteur.find(")")])
    fiche["auteurs"]=a
    fiche["fonctions"]=f
except:
    pass


# %% [markdown]
# Récupération du genre: A priori non précisé sur amazon donc non récupérable

# %% [markdown]
# Récupération des attributs suivants: Editeur, Date Parution, Relié/Broché, Nombre de pages, Poids, Dimensions

# %%
try:   
    poids=soup2.find('ul',{'class': 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list'})
    for attribut in poids:
        attribut=attribut.text.replace("  ","").replace("\n","")
        if attribut[:8]==" Éditeur":
            fiche["editeur"]=attribut[attribut.find(":")+1:attribut.find("(")]
            fiche["editeur"]=fiche["editeur"].replace("\u200e","").strip()
            fiche["date"]=attribut[attribut.find("(")+1:attribut.find(")")].strip()
        elif attribut[:6]==" Poche":
            fiche["reliure"]="Broché"
            fiche["nbPages"]=attribut[attribut.find(":")+1:attribut.find("pages")]
            fiche["nbPages"]=int(fiche["nbPages"].replace("\u200e",""))
        elif attribut[:7]==" Broché":
            fiche["reliure"]="Broché"
            fiche["nbPages"]=attribut[attribut.find(":")+1:attribut.find("pages")]
            fiche["nbPages"]=int(fiche["nbPages"].replace("\u200e",""))
        elif attribut[:6]==" Relié":
            fiche["reliure"]=" Relié"
            fiche["nbPages"]=attribut[attribut.find(":")+1:attribut.find("pages")]
            fiche["nbPages"]=int(fiche["nbPages"].replace("\u200e",""))

        elif attribut[:19]==" Poids de l'article":
            if attribut[-3:]==" g ":
                fiche["poids"]=attribut[attribut.find(":")+1:attribut.find("g")]
                fiche["poids"]=float(fiche["poids"].replace("\u200e",""))
            elif attribut[-3:]=="kg ":
                fiche["poids"]=attribut[attribut.find(":")+1:attribut.find("kg")]
                fiche["poids"]=float(fiche["poids"].replace("\u200e",""))*1000

        elif attribut[:11]==" Dimensions":
            fiche["format"]=attribut[attribut.find(":")+1:attribut.find("cm")+2]
            fiche["format"]=(fiche["format"].replace("\u200e","").strip())
except:
    pass
        

# %% [markdown]
# Récupération du prix:


# %%
try:
    prix=soup2.find('span', {'class': 'a-offscreen'})
    fiche["prix"]=prix.text[:-1].replace(",",".").strip()
    fiche["prix"]=float(fiche["prix"].replace("\xa0",""))
except:
    pass
# %% [markdown]
# Récupération de la série et du numéro de série (s'il existe):

# %%
try:
    serie=soup2.find('div', {'id': 'rpi-attribute-book_details-series'}) 
    serie=serie.text
    if serie[:7]=="  Fait ":
        serie_nom=serie[serie.find("    ")+5:]
        fiche["serie"]=serie_nom.strip()
    elif serie[:7]=="  Livre":
        numero=serie[serie.find("Livre")+5:serie.find("sur")]
        serie_nom=serie[serie.find("    ")+5:]
        fiche["numeroSerie"]=int(numero)
        fiche["serie"]=serie_nom.strip()
except:
    pass

# %% [markdown]
# 

# %% [markdown]
# Récupération du lien de l'image:


# %%
try:
    lien=soup2.find('div', {'id': 'booksImageBlock_feature_div'})
    lien=lien.find('img',{'class': 'a-dynamic-image image-stretch-vertical frontImage'})["data-a-dynamic-image"]
    lien=lien[lien.find('"')+1:lien.find('":')]
except:
    pass

# %% [markdown]
# Téléchargement de la couverture et sauvegarde sur le pc avec comme nom de fichier isbn:

# %%
try:
    urllib.request.urlretrieve(lien, "C:/Users/tommy/Documents/Travail/Codev/couverture/"+ISBN+".jpg")
except:
    print("Problème de récupération de l'image")
# %% [markdown]
# Mettre le lien local de l'image sur la fiche:

# %%
fiche["image"]="C:/Users/tommy/Documents/Travail/Codev/couverture/"+ISBN+".jpg"

# %% [markdown]
# Mettre l'horodatage de la consultation du site:

# %%
path = fiche["image"]
ti_m = os.path.getmtime(path)
m_ti = time.ctime(ti_m)
t_obj = time.strptime(m_ti)
T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
fiche["consultation"]=T_stamp

# %% [markdown]
# Transformer l'élément fiche de type dictionnaire en fichier JSON:

# %%
jsonString = json.dumps(fiche)
jsonFile = open("C:/Users/tommy/Documents/Travail/Codev/json_amazon/"+ISBN+".json", "w")
jsonFile.write(jsonString)
jsonFile.close()
path = "C:/Users/tommy/Documents/Travail/Codev/json_amazon/"+ISBN+".json"
ti_m = os.path.getmtime(path)
m_ti = time.ctime(ti_m)
t_obj = time.strptime(m_ti)
T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
fiche["creation"]=T_stamp
print(fiche)
