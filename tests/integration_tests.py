import pytest
from app import app as flask_app
from models import Base, engine, Session

from models import Session, Pokemon
from models import Pokemon
from datetime import datetime


@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    with flask_app.app_context():
        Base.metadata.create_all(engine)
        yield flask_app
        Session.close_all()
        Base.metadata.drop_all(engine)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_add_pokemon(client):
    response = client.post('/api/v1/pokemon', json={
        "nome": "Charmander",
        "descricao": "Lagarto de fogo",
        "valor": 300.0,
        "tempo": "2024-07-03 12:00:00",
        "usuario": "Ash Ketchum"
    })
    assert response.status_code == 201
    assert response.json['nome'] == "Charmander"
    assert response.json['descricao'] == "Lagarto de fogo"


def test_get_pokemons(client):
    client.post('/api/v1/pokemon', json={
        "nome": "Charmander",
        "descricao": "Lagarto de fogo",
        "valor": 300.0,
        "tempo": "2024-07-03 12:00:00",
        "usuario": "Ash Ketchum"
    })
    response = client.get('/api/v1/pokemon?page=1&per_page=5')
    assert response.status_code == 200
    assert len(response.json['pokemons']) == 1
    assert response.json['pokemons'][0]['nome'] == "Charmander"


def test_get_pokemon(client):
    client.post('/api/v1/pokemon', json={
        "nome": "Charmander",
        "descricao": "Lagarto de fogo",
        "valor": 300.0,
        "tempo": "2024-07-03 12:00:00",
        "usuario": "Ash Ketchum"
    })
    response = client.get('/api/v1/pokemon/1')
    assert response.status_code == 200
    assert response.json['nome'] == "Charmander"
    assert response.json['descricao'] == "Lagarto de fogo"


def test_get_pokemon_not_found(client):
    response = client.get('/api/v1/pokemon/999')
    assert response.status_code == 404
