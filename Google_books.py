#lib pour traiter les json
import json
#lib pour ouvrir et lire les url
from urllib.request import urlopen

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

raw = get_book_raw(test_isbn_hp)
print(raw)
def extract(raw):
    data = {}
    data['isbn_10'] = raw.get('industryIdentifiers')[0]['identifier']
    data['isbn_13'] = raw.get('industryIdentifiers')[1]['identifier']
    data['titre'] = raw.get('title')
    data['sous-titre'] = raw.get('subtitle')
    data['auteur(s)'] = raw.get('authors')
    data['éditeur'] = raw.get('publisher')
    data['publication'] = raw.get('publishedDate')
    data['Nombre de pages'] = raw.get('pageCount')
    data['Genre'] = raw.get('categories')
    return data

extract(raw)