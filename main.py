import json  # read and write .json files
import os    # create file paths that work on Windows
import unicodedata

#function from library
def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = texto_normalizado.encode('ascii', 'ignore').decode('utf-8')
    return texto_sem_acentos

CAMINHO_ARQUIVO = os.path.join("data", "livros.json")


#MAIN FUNCTIONS
# register data
def salvar_dados(dados):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# read .json and list the saved books
def carregar_dados():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return {"livros": []}
    
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return {"livros": []}


#SECONDARY FUNCTIONS
def cadastrar_livro():
    titulo = input("Qual o nome do livro? ")
    autor = input(f"Qual o autor do livro ({titulo})? ")
    ano = input(f"Qual o ano de publicação do livro ({titulo})? ")
    editora = input(f"Qual a editora do livro ({titulo})? ")

    dados = carregar_dados()

    novo_id = len(dados["livros"])+ 1

    novo_livro = {
            "id": novo_id,
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "editora": editora
        }

    dados["livros"].append(novo_livro)

    salvar_dados(dados)

    print(f"\n Livro '{titulo}' cadastrado com sucesso :) ")

def listar_livros():
    dados = carregar_dados()
    livros = dados["livros"]

    if not livros:
        print("\nNenhum livro cadastrado ainda.")
        return

    print("\n Lista de livros:")
    print("-" * 40)
    for livro in livros:
        for chave, valor in livro.items():
            print(f"{chave.capitalize()}: {valor}")
        print("-" * 40)

def buscar_livro():
    dados = carregar_dados()
    livros = dados["livros"]
    buscado = input("Qual nome do livro você quer buscar? ")

    for livro in livros :
        if remover_acentos(livro["titulo"]).lower() == buscado.lower():
            print("\n==> Livro encontrado \n")
            for chave,valor in livro.items():
                print(f"{chave.capitalize()} : {valor}")
            return
        
    print("\n:( Livro não encontrado")

    

def atualizar_livro():
    dados = carregar_dados()
    livros = dados["livros"]

    mudanca = input("Qual nome do livro deseja atualizar dados?")
    for livro in livros:
        if remover_acentos(livro["titulo"]).lower() == mudanca.lower():
            tipo = input("Qual dos parametros deseja mudar (titulo / autor/ ano / editora) ? ")
            if tipo in ["titulo", "autor", "ano", "editora"]:
                novo_valor = input(f"Digite o novo valor para {tipo}: ")
                livro[tipo] = novo_valor
                salvar_dados(dados)
                print("Valores atualizados com sucesso!")
                for chave,valor in livro.items():
                    print(f"{chave.capitalize()} : {valor}")
                return
            print(":( Parametro inválido")
            return
    print(":( Livro não encontrado")

            

def remover_livro():
    dados = carregar_dados()
    livros = dados["livros"]

    titulo = input("Digite o título do livro que deseja remover: ").strip()

    for livro in livros:
        if remover_acentos(livro["titulo"]).lower() == titulo.lower():
            livros.remove(livro)
            encontrado = True
            print(f"\nLivro '{titulo}' removido com sucesso.")
            salvar_dados(dados)
            return
        
    print(":( Livro não encontrado)")

    

def sair():
    print("\nSalvando dados....")
    print("Saindo....")



#MAIN BLOCK
dados = carregar_dados()

opcoes = {
    "1": cadastrar_livro,
    "2": listar_livros,
    "3": buscar_livro,
    "4": atualizar_livro,
    "5": remover_livro,
    "6": sair
}

while True:
    print("\n=== MENU ===")
    print("1. Cadastrar novo livro")
    print("2. Listar todos os livros")
    print("3. Buscar livro por título")
    print("4. Atualizar livro")
    print("5. Remover livro")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao in opcoes:
        opcoes[opcao]()
        if opcao == "6":
            break
    else:
        print("Opção inválida.")
