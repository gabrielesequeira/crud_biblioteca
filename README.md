# CRUD de Biblioteca

Projeto da disciplina **CTC4002 - Modelagem e Programação**  
Feito com **Python** utilizando arquivos **JSON** para persistência de dados.

---

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
