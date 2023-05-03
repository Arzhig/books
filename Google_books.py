#lib pour traiter les json
import json
#lib pour ouvrir et lire les url
from urllib.request import urlopen
from datetime import datetime

test_isbn_hp = '9780747573609'
test_isbn_python = '1593276036'
def get_book_raw(code):
    #variables de départ : url "vide" et isbn
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    isbn = code.strip()

    #récupérer la réponse serveur http liée à l'isbn demandé
    reponse = urlopen(api + isbn)
    #extraire les données du json de la reponse, et les charger dans un dictionnaire python
    book_data = json.load(reponse)
    infos=book_data['items'][0]['volumeInfo']
    return(infos)

raw = get_book_raw('2253941700')
#print(raw)
def extract(raw):
    data = {"isbn10"           :"",
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
             "creation"         :""}
    data['isbn10'] = raw.get('industryIdentifiers')[0]['identifier']
    data['isbn13'] = raw.get('industryIdentifiers')[1]['identifier']
    data['titre'] = raw.get('title')
    data['sousTitre'] = raw.get('subtitle')
    data['auteurs'] = raw.get('authors')
    data['editeur'] = raw.get('publisher')
    data['date'] = raw.get('publishedDate')
    data['nbPages'] = int(raw.get('pageCount'))
    data['genre'] = raw.get('categories')
    data['consultation'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

print(extract(raw))