# Classe que implementa a tabela Pokemon
from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime

from models.base import Base


class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column("pk_pokemon", Integer, primary_key=True)
    nome = Column("unq_nome_pokemon", String(80), nullable=False, unique=True)
    descricao = Column(String(200), nullable=False)
    valor = Column(Float, nullable=False)
    tempo = Column(DateTime, default=datetime.now())
    usuario = Column(String(80), nullable=False)
    imagem = Column(String(100), nullable=True)

    def __init__(self, nome, descricao, valor, tempo, usuario, imagem):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.usuario = usuario
        self.imagem = imagem
        # se não for informada, será o data exata da inserção no banco
        if tempo:
            self.tempo = tempo

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'valor': self.valor,
            'tempo': self.tempo.strftime('%Y-%m-%d %H:%M:%S'),
            'usuario': self.usuario,
            'imagem': self.imagem
        }
