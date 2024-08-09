# Teste Técnico AAWZ

Este projeto é uma API construída com FastAPI para gerenciar usuários. A seguir estão as instruções para rodar o projeto e interagir com os endpoints disponíveis.

## Requisitos

Antes de começar, certifique-se de ter o `poetry` e o `sqlite` instalados em seu sistema.

## Passos para rodar o projeto

1. **Clonar o repositório**

   Clone o repositório para o seu ambiente local:
    git clone https://github.com/toledodouglas/-technical_test_project

    cd -technical_test_project


2. **Instalar o Poetry**

Caso ainda não tenha o Poetry instalado, siga as instruções na [documentação oficial do Poetry](https://python-poetry.org/docs/#installation) para instalar.

3. **Instalar o SQLite**

O SQLite deve estar instalado em seu sistema. Você pode instalar o SQLite a partir do [site oficial](https://www.sqlite.org/download.html) ou usar um gerenciador de pacotes.

4. **Atualizar o banco de dados**

Execute o comando para atualizar o banco de dados com o Alembic:
    alembic upgrade head


5. **Instalar as dependências**

Instale as dependências do projeto usando o Poetry:
    poetry install


6. **Iniciar o ambiente virtual**

Inicie o ambiente virtual criado pelo Poetry:
    poetry shell


7. **Executar o projeto**

Com o ambiente virtual ativado, execute o projeto:
    task run


8. **Validar o endpoint `/users`**

Teste os seguintes endpoints disponíveis na API:

- **GET /users**: Obtém a lista de todos os usuários.
- **GET /users/{cpf}/**: Obtém um usuário específico pelo CPF.
- **POST /users**: Cria um novo usuário. Exemplo de payload:
  ```
  {
    "username": "string",
    "cpf": "00000000000",
    "email": "user@example.com",
    "uf": "string",
    "dataNasc": "string"
  }
  ```
- **PUT /users/{cpf}/**: Atualiza um usuário existente pelo CPF. Exemplo de payload:
  ```
  {
    "username": "string",
    "cpf": "00000000000",
    "email": "user@example.com",
    "uf": "string",
    "dataNasc": "string"
  }
  ```
- **DELETE /users/{cpf}/**: Deleta um usuário específico pelo CPF.

## Exemplos de uso

- **Criar um novo usuário**

```
curl -X POST "http://localhost:8000/users" -H "Content-Type: application/json" -d '{"username": "john_doe", "cpf": "12345678900", "email": "john@example.com", "uf": "SP", "dataNasc": "1990-01-01"}'
```

- **Atualizar um usuário**
```
curl -X PUT "http://localhost:8000/users/12345678900/" -H "Content-Type: application/json" -d '{"username": "john_doe_updated", "cpf": "12345678900", "email": "john_updated@example.com", "uf": "SP", "dataNasc": "1990-01-01"}'
```

- **Deletar um usuário**

```
curl -X DELETE "http://localhost:8000/users/12345678900/"
```


- **Obter todos os usuários**
```
curl -X GET "http://localhost:8000/users"
```


- **Obter um usuário específico**
```
curl -X GET "http://localhost:8000/users/12345678900/"
```




