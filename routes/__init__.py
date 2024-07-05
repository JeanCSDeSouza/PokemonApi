from flask_openapi3 import APIBlueprint

pokemons_bp = APIBlueprint('pokemons', __name__)

from .PokemonRoutes import *
