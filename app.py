from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, redirect
from routes import pokemons_bp

from flask_cors import CORS


# Configuração do aplicativo
info = Info(title="Api de cards de pokemon", version="1.0.0")
# app = Flask(__name__)
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")


# Registrar o Blueprint
app.register_api(pokemons_bp)


@app.get('/')
def home():
    return redirect('/openapi')


if __name__ == '__main__':
    app.run(debug=True)

