from titulo import Titulo

class Serie(Titulo):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - {self.temporadas} temporadas - Likes: {self._likes}"

