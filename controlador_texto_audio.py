from io import BytesIO
from gtts import gTTS
from pygame import mixer
from time import sleep

class ControladorTextoAudio:
    def __init__(self) -> None:
        self.idioma = "pt-BR"

    def setIdioma(self, idioma):
        self.idioma = idioma

    def ler_texto(self, texto):
        if isinstance(texto, list):
            texto = ' '.join(texto)
        
        myobj = gTTS(texto, lang=self.idioma)
        mp3_p = BytesIO()
        myobj.write_to_fp(mp3_p)
        mixer.init()
        mp3_p.seek(0)
        mixer.music.load(mp3_p, 'mp3')
        mixer.music.play()

    def parar_leitura(self):
        mixer.music.stop()