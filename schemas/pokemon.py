from pydantic import BaseModel
from typing import Optional, List
from models.Pokemon import Pokemon


class PokemonModelo(BaseModel):
    """ Representa um pokemon a ser inserido.
    """
    nome: str = "Charmander"
    descricao: str = "Lagarto de fogo"
    valor: float = 12.50
    tempo: str = "2024-07-03 22:20:32"
    usuario: str = "Ash Ketchum"
    imagem: Optional[str] = "https://img.pokemondb.net/artwork/large/charmander.jpg"


class ListagemPokemonSchema(BaseModel):
    """ Representa o retorno de uma listagem de pokemons.
    """
    pokemons: List[PokemonModelo]


def apresenta_pokemons(pokemons: List[Pokemon]):
    """ Retorna uma representação do pokemon seguindo o schema definido em
        PokemonViewSchema.
    """
    result = []
    for pokemon in pokemons:
        result.append({
            "nome": pokemon.nome,
            "descricao": pokemon.descricao,
            "valor": pokemon.valor,
            "tempo": pokemon.tempo.strftime("%Y-%m-%d %H:%M:%S"),
            "usuario": pokemon.usuario,
            "imagem": pokemon.imagem
        })

    return {"pokemons": result}


class PokemonViewSchema(BaseModel):
    """ Define como um pokemon será retornado.
    """
    nome: str = "Charmander"
    descricao: str = "Lagarto de fogo"
    valor: float = 12.50
    tempo: str = "31/07/2024 10:00"
    usuario: str = "Ash Ketchum"
    imagem: Optional[str] = "https://img.pokemondb.net/artwork/large/charmander.jpg"


def apresenta_pokemon(pokemon: Pokemon):
    """ Retorna uma representação do pokemon seguindo o schema definido em
        pokemonViewSchema.
    """
    return {
        "nome": pokemon.nome,
        "descricao": pokemon.descricao,
        "valor": pokemon.valor,
        "tempo": pokemon.tempo.strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": pokemon.usuario,
        "imagem": pokemon.imagem
    }
