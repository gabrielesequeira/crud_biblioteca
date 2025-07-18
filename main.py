import json  # read and write .json files
import os    # create file paths that work on Windows

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
    pass

def atualizar_livro():
    pass

def remover_livro():
    dados = carregar_dados()
    livros = dados["livros"]

    titulo = input("Digite o título do livro que deseja remover: ").strip()

    encontrado = False
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            livros.remove(livro)
            encontrado = True
            print(f"\nLivro '{titulo}' removido com sucesso.")
            break

    if not encontrado:
        print(f"\nO Livro '{titulo}' não foi encontrado.")

    salvar_dados(dados)

def sair():
    salvar_dados(dados)
    print("Saindo...")




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
