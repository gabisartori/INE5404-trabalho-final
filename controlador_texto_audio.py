from gtts import gTTS

class ControladorTextoAudio:
    def __init__(self, idioma) -> None:
        self.idioma = idioma

    def setIdioma(self, idioma):
        self.idioma = idioma

    def texto_para_audio(self, texto):
        tts = gTTS(texto, lang=self.idioma)
        return tts