from pymongo import MongoClient
db = MongoClient("mongodb://localhost:27017/") #cria a variavel db para associar ao banco de dados

biblioteca = db["biblioteca"] #conecta a variavel biblioteca com a variavel db 

if "livros" not in biblioteca.list_collection_names(): #verifica se já existe a coleção
    biblioteca.create_collection("livros") #se não existir, cria a coleção "livros"

if "usuarios" not in biblioteca.list_collection_names():
    biblioteca.create_collection("usuarios") #se não existir, cria a coleção "usuarios"

if "livros" not in biblioteca.list_collection_names():
    biblioteca.create_collection("livros")

colecao_usuarios = biblioteca["usuarios"]
colecao_livros = biblioteca["livros"]

print("\n========== Bem vindo(a) a sua biblioteca ==========\n")
escolha = input("1-login\n2-cadastro\nEscolha:")

if escolha == "1":
    def login():
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        resultado = colecao_usuarios.find_one({
            "$and": [
                {"usuario": usuario},
                {"senha": senha},
            ]
        })
        if resultado:
            print("Usuario encontrado")
            return resultado
        else:
             print("Usuario e/ou senha inválidos")
             return None
    usuario_logado = login()

else:
    def cadastro():
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")
            
        usuarios = {
            "usuario": usuario,
            "senha": senha
        }
        resultado = colecao_usuarios.find_one({
                    "usuario": usuario
                })
        if resultado:
            print("Usuario ja cadastrado, realize login")
        else:
            colecao_usuarios.insert_one(usuarios)
            print("Cadastro realizado com sucesso")
        print("Livro cadastrado com sucesso!")
    cadastro()


def cadastro_livros():
    print("\n========== Cadastre seu livro ==========\n")
    nomelivro = input("Nome: ")
    autor = input("Autor: ")
    genero = input("Genero: ")
    cat = input("Categoria (lido, lendo ou desejo): ")


    livros = {
        "nomelivro": nomelivro,
        "autor": autor,
        "genero": genero,
        "cat": cat,
        "usuario_id": usuario_logado["_id"]
    }
    colecao_livros.insert_one(livros)


    

