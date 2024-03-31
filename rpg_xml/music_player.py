import subprocess


class MusicPlayer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.process = None

    def play(self):
        if not self.process:
            self.process = subprocess.Popen(
                ["mpv", "--loop=inf", self.file_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        else:
            print("A música já está sendo reproduzida.")

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None
        else:
            print("Não há música em reprodução para parar.")

    def pause(self):
        if self.process:
            self.process.send_signal(subprocess.signal.SIGSTOP)
        else:
            print("Não há música em reprodução para pausar.")

    def resume(self):
        if self.process:
            self.process.send_signal(subprocess.signal.SIGCONT)
        else:
            print("Não há música em reprodução para retomar.")


# Exemplo de uso
player = MusicPlayer("caminho/do/arquivo/musica.mp3")
player.play()  # A música será reproduzida infinitamente
