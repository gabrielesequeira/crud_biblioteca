import json  # read and write .json files
import os    # create file paths that work on Windows

CAMINHO_ARQUIVO = os.path.join("data", "livros.json")

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

# Funções das opções (você ainda vai implementar essas)
def cadastrar_livro():
    pass

def listar_livros():
    pass

def buscar_livro():
    pass

def atualizar_livro():
    pass

def remover_livro():
    pass

# Função específica para encerrar o programa
def sair():
    salvar_dados(dados)
    print("Saindo...")

# carregar os dados no início
dados = carregar_dados()

# dicionário de opções
opcoes = {
    "1": cadastrar_livro,
    "2": listar_livros,
    "3": buscar_livro,
    "4": atualizar_livro,
    "5": remover_livro,
    "6": sair  # agora aponta para uma função nomeada
}

# loop principal do menu
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
