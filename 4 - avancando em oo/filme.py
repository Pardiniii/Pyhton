from titulo import Titulo


class Filme(Titulo):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duracao: {self.duracao} min - Likes: {self._likes}"
