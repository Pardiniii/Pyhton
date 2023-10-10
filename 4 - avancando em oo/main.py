from filme import Filme
from serie import Serie
from titulo import Titulo
from playlist import Playlist

tmep = Filme('Todo mundo em panico', 1999, 110)
vingadores = Filme("vingadores - Guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()


you = Serie('You', 2018, 4)
flash = Serie('The flash', 2017, 6)
flash.dar_like()
flash.dar_like()
flash.dar_like()
flash.dar_like()
you.dar_like()
you.dar_like()
you.dar_like()
you.dar_like()
you.dar_like()
you.dar_like()
you.dar_like()

filmes_e_series = [vingadores, you, tmep, flash]

playlist_fim_de_semana = Playlist("Meu fim de semana", filmes_e_series)
print(f"Tamanho da playslist {len(playlist_fim_de_semana)}")
print(f"vingadores esta na playlist para o fds?{vingadores in playlist_fim_de_semana}")
print(len(playlist_fim_de_semana))
for programa in playlist_fim_de_semana:
    print(programa)

print(vingadores)
