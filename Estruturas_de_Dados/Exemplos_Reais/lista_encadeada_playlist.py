class Media:
    
    def __init__(self, nome = "Sem Título", tamanho = 0, tempo = 0, autor = "Sem Autor", playlists_presentes:list = [], thumb = None):
        
        self.nome = nome
        self.tempo = tempo
        self.thumb = thumb
        self.proximo = None

class Musica(Media):

    def __init__(self, nome = "Sem Título", tamanho = 0, tempo = 0, autor = "Sem Autor", playlists_presentes:list = [], thumb = None):
        super().__init__(nome, tamanho, tempo, autor, playlists_presentes, thumb)
    
class Podcast(Media):
    def __init__(self, nome = "Sem Título", tamanho = 0, tempo = 0, autor = "Sem Autor", playlists_presentes:list = [], thumb = None):
        super().__init__(nome, tamanho, tempo, autor, playlists_presentes, thumb)

class Music_Player:
    def __init__(self, currenyly_playing:Media):
        
        self.play_media(currenyly_playing)

    def play_media(self, media:Media):

        while media.proximo:
            print(f"Atualmente tocando: {media.nome}")

            for count in range(media.tempo):
                if count %20 == 0:
                    print(f"Tempo atual: {count}")
                if 0 != count and count %80 == 0:
                    print(f"Tempo atual: {media.tempo} Tocando: {media.nome}")
            print(f"Próximo: {media.proximo.nome}", end="\n\n")
            media = media.proximo 

pneu_queimado = Musica("pneu queimado", tempo = 145)
tropa_de_elite = Musica("tropa de elite", tempo = 207)
ate_quando = Musica("Até Quando?", tempo = 263, autor="Gabriel Pensador")
qual_e = Musica("Qual é?", tempo = 405, autor= "Marcelo D2")
rap_do_silva = Musica("Rap do Silva", tempo = 325, autor="Mc Bob Rum")
in_the_end = Musica("In The End", tempo = 125, autor="Linkin Park")

pneu_queimado.proximo = tropa_de_elite
tropa_de_elite.proximo = rap_do_silva
rap_do_silva.proximo = qual_e
qual_e.proximo = in_the_end
in_the_end.proximo = ate_quando

abc = Music_Player(pneu_queimado)