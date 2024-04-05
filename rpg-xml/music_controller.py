import threading
from .music_player import MusicPlayer


class MusicController:
    def __init__(self):
        self.music_player = None
        self.music_playing = False
        self.music_stop_flag = threading.Event()

    def play_music(self, music_url):
        if self.music_player and self.music_playing:
            self.stop_music()  # Parar música atual se estiver tocando
        self.music_stop_flag.clear()  # Limpar a flag de parada
        self.music_player = threading.Thread(
            target=self._play_music_thread, args=(music_url,)
        )
        self.music_player.start()
        self.music_playing = True

    def stop_music(self):
        if self.music_playing:
            self.music_stop_flag.set()  # Sinalizar para parar a música
            self.music_player.join()  # Aguardar música atual terminar
            self.music_playing = False

    def _play_music_thread(self, music_url):
        music_player = MusicPlayer(music_url)
        music_player.play()
        while not self.music_stop_flag.is_set():
            self.music_stop_flag.wait(0.1)
        music_player.stop()
