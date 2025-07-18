# CRUD de Biblioteca

Projeto da disciplina **CTC4002 - Modelagem e Programação**  
Feito com **Python** utilizando arquivos **JSON** para persistência de dados.


## Objetivo

Criar um sistema simples de **cadastro de livros** (CRUD: Create, Read, Update, Delete), executado via terminal.  
O projeto simula um sistema de biblioteca, permitindo registrar livros com título, autor e ano de publicação.

## Funcionalidades

- [x] Cadastrar novos livros
- [x] Listar todos os livros
- [x] Buscar livro por título
- [x] Atualizar informações de um livro
- [x] Remover um livro do sistema
- [x] Persistência de dados com JSON

## Lógica de dados do Backend
O sistema utiliza duas funções principais para gerenciar os dados dos livros:

`carregar_dados()`
Verifica se o arquivo JSON com os livros existe, lê e converte o conteúdo para um dicionário Python com a lista de livros. Se o arquivo não existir ou estiver vazio, retorna uma lista vazia para evitar erros.

`salvar_dados(dados)`
Recebe os dados atualizados dos livros como `dados` e grava no arquivo JSON, garantindo que todas as alterações sejam persistidas. Isso mantém o sistema sincronizado e com as informações sempre atualizadas entre as execuções.

Essas funções garantem que o programa possa ler, modificar e salvar os dados de forma segura e eficiente, formando a base para as operações de cadastro, consulta, atualização e remoção (CRUD).


## Estrutura de dados

Cada livro será salvo no arquivo `data/livros.json` com o seguinte formato:

```json
{
  "livros": [
    {
      "id": 1,
      "titulo": "Dom Casmurro",
      "autor": "Machado de Assis",
      "ano": 1899
    }
  ]
}
