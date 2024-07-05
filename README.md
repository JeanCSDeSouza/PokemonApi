# Pokemon API
PokemonAPI desenvolvida com Python Flask, SQLAlchemy e SQLite.

## Requisitos
- Flask
- Flask-Cors
- flask-openapi3
- Flask-SQLAlchemy
- Flask-Migrate
- flask-serialize
- nose2
- pydantic
- SQLAlchemy
- SQLAlchemy-Utils
- typing_extensions
- pytest
- pytest-flask

## Quick Start
1. Clonar o repositório
    ```bash
    git clone a definir
    cd PokemonAPI
    ```

2. Inicializar e ativar o ambiente virtual (opcional):
    ```bash
   python -m pip install --user virtualenv 
   virtualenv env
   source env/bin/activate
    ```

3. Instalar as dependências do projeto
    ```bash
    pip3 install -r requirements.txt
    ```
4. Rodar os testes da aplicação
    ```bash
      nose2
    ```
5. Rodar o servidor de desenvolvimento
    ```bash
    flask run --host 0.0.0.0 --port 5000 --reload
    ```

6. Veja a api em: http://localhost:5000

# Realizar operações CRUD com a API

## Endpoints da API

#### Adicionar Pokémon
- URL: /api/v1/pokemon
  - Método: POST

  - Descrição: Adiciona um novo Pokémon.

  - Exemplo de Request:
  ```Bash
   curl -X POST -H "Content-Type: application/json" -d '{
  "nome": "Pikachu",
  "descricao": "Um Pokémon do tipo elétrico",
  "valor": 300.0,
  "tempo": "2024-07-03 12:00:00",
  "usuario": "Ash Ketchum"
   }' http://127.0.0.1:5000/api/v1/pokemon
  ```
    - Exemplo de Response:
    ```json
    {
        "id": 1,
        "nome": "Pikachu",
        "descricao": "Um Pokémon do tipo elétrico",
        "valor": 300.0,
        "tempo": "2024-07-03 12:00:00",
        "usuario": "Ash Ketchum"
    }
    ```
#### Listar Pokémons
- URL: /api/v1/pokemon
  - Método: GET

  - Descrição: Lista todos os Pokémons cadastrados.

  - Exemplo de Request:
  ```Bash
  curl -X GET "http://127.0.0.1:5000/api/v1/pokemon?page=1&per_page=5"
    ```
   - Exemplo de Response:      
   ```json
        {
            "items": [
                {
                    "id": 1,
                    "nome": "Pikachu",
                    "descricao": "Um Pokémon do tipo elétrico",
                    "valor": 300.0,
                    "tempo": "2024-07-03 12:00:00",
                    "usuario": "Ash Ketchum"
                }
            ]
        }
   ```
#### Buscar Pokémon por id
  - URL: /api/v1/pokemon/<id>
    - Método: GET

    - Descrição: Busca um Pokémon pelo seu id.

    - Exemplo de Request:
    ```Bash
      curl -X GET http://127.0.0.1:5000/api/v1/pokemon/1
      ```
- Exemplo de Response:
   ```json
        {
            "id": 1,
            "nome": "Pikachu",
            "descricao": "Um Pokémon do tipo elétrico",
            "valor": 300.0,
            "tempo": "2024-07-03 12:00:00",
            "usuario": "Ash Ketchum"
        }
   ```   



