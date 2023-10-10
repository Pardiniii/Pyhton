class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas
    
    def __getitem__(self, item):
        return self._programas[item]
    
    