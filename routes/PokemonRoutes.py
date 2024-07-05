# Autor: Jean Carlos
# Imports
from datetime import datetime

from flask_openapi3 import Tag, APIBlueprint
from pydantic import BaseModel, Field
from sqlalchemy.exc import IntegrityError
from models import Session, Pokemon
from schemas import *

# Constantes tags
pokemon_tag_get = Tag(name="Produto_Get", description="Recupera um pokemon da base")
pokemon_tag_post = Tag(name="Produto_Post", description="Adiciona um pokemon à base")
pokemon_tag_list = Tag(name="Produto_List", description="Recupera todos os pokemons da base")

# Blueprint com a definição do prefixo das rotas
pokemons_bp = APIBlueprint('pokemons', __name__, url_prefix='/api/v1')


class PokemonPath(BaseModel):
    bid: int = Field(..., description='pokemon id', json_schema_extra={"deprecated": False, "example": 10})


@pokemons_bp.get('/pokemon', tags=[pokemon_tag_list],
                 responses={"200": PokemonViewSchema, "404": ErrorSchema})
def get_pokemons():
    session = Session()
    pokemons = session.query(Pokemon).all()

    if not pokemons:
        return {"pokemons": []}, 404
    else:
        return apresenta_pokemons(pokemons), 200


@pokemons_bp.post('/pokemon', tags=[pokemon_tag_post],
                  responses={"201": PokemonViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def add_pokemon(form: PokemonModelo):
    new_pokemon = Pokemon(
        nome=form.nome,
        descricao=form.descricao,
        valor=form.valor,
        tempo=datetime.strptime(form.tempo, '%Y-%m-%d %H:%M:%S'),
        usuario=form.usuario,
        imagem=form.imagem
    )
    try:
        session = Session()
        session.add(new_pokemon)
        session.commit()
        return apresenta_pokemon(new_pokemon), 201
    except IntegrityError as e:
        return {"message": "Pokemon de mesmo nome já salvo na base :/"}, 409
    except Exception as e:
        return {"message": "Não foi possível realizar esta operação :/"}, 400


@pokemons_bp.get('/pokemon/<int:bid>', tags=[pokemon_tag_get],
                 responses={"200": PokemonViewSchema, "404": ErrorSchema})
def get_pokemon(path: PokemonPath):
    session = Session()
    pokemon_persisted = session.query(Pokemon).filter(Pokemon.id == path.bid).first()
    if not pokemon_persisted:
        return {"message": "Pokemon não encontrado :/"}, 404
    else:
        return apresenta_pokemon(pokemon_persisted), 200
