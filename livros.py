from pymongo import MongoClient
db = MongoClient("mongodb://localhost:27017/") #cria a variavel db para associar ao banco de dados

biblioteca = db["biblioteca"] #conecta a variavel biblioteca com a variavel db 

if "livros" not in biblioteca.list_collection_names(): #verifica se já existe a coleção
    biblioteca.create_collection("livros") #se não existir, cria a coleção "livros"

if "usuarios" not in biblioteca.list_collection_names():
    biblioteca.create_collection("usuarios") #se não existir, cria a coleção "usuarios"

    
