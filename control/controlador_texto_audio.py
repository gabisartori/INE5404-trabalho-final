from io import BytesIO
from gtts import gTTS
from pygame import mixer


class ControladorTextoAudio:
    def __init__(self) -> None:
        self.__idioma = "pt-BR"

    def set_idioma(self, idioma: str) -> None:
        self.__idioma = idioma

    def get_idioma(self) -> str:
        return self.__idioma

    def ler_texto(self, texto: str) -> None:
        """Toca o áudio do texto"""
        if isinstance(texto, list):
            texto = ' '.join(texto)
        
        myobj = gTTS(texto, lang=self.__idioma)
        mp3_p = BytesIO()
        myobj.write_to_fp(mp3_p)
        mixer.init()
        mp3_p.seek(0)
        mixer.music.load(mp3_p, 'mp3')
        mixer.music.play()

    @staticmethod
    def parar_leitura() -> None:
        mixer.music.stop()
