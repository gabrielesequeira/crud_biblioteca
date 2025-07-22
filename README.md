# Library CRUD

Project for the course **CTC4002 - Modeling and Programming**
Built with **Python** using **JSON** files for data persistence.

## Objective

Create a simple **book registration system** (CRUD: Create, Read, Update, Delete), executed via terminal.
The project simulates a library system, allowing users to register books with title, author, and year of publication.

## Features

* [x] Register new books
* [x] List all books
* [x] Search for a book by title
* [x] Update book information
* [x] Remove a book from the system
* [x] Data persistence with JSON

## Backend Data Logic

The system uses two main functions to manage book data:

`load_data()`
Checks if the JSON file with the books exists, reads and converts its contents into a Python dictionary with the list of books. If the file doesn't exist or is empty, it returns an empty list to avoid errors.

`save_data(data)`
Receives the updated book data as `data` and writes it to the JSON file, ensuring all changes are persisted. This keeps the system synchronized and the information always up to date between executions.

These functions ensure that the program can read, modify, and save data safely and efficiently, forming the foundation for the CRUD operations.

## Data Structure

Each book will be saved in the file `data/livros.json` in the following format:

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
```
## Topics Learned and Practiced

During the development of this project, the following topics covered in class were reinforced:

- **JSON File Handling**
  - Reading and writing data using the `json` library
  - Structuring data in a hierarchical format

- **Structured Programming with Functions**
  - Modularizing the code using reusable functions
  - Separating responsibilities (reading, writing, processing)

- **CRUD Operations**
  - Creating, listing, updating, and deleting records
  - Implementing conditional logic for flow control

- **Input and Output via Terminal**
  - Interacting with the user using `input()` and `print()`

- **Python Data Structures**
  - Using lists and dictionaries to represent collections and objects

- **File and Exception Handling**
  - Checking file existence and content
  - Preventing failures during read/write operations

