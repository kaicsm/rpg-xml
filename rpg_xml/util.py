import time
import sys
import os


class TerminalUI:
    COLORS = {
        "default": "\033[0m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }

    def __init__(self):
        self.running = True

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def type_message(
        self, message, type_vel=30, delay_before=0, color="default", wrap_line=True
    ):
        if delay_before > 0:
            time.sleep(delay_before / 1000)

        # Escreve a mensagem caractere por caractere com um atraso
        for char in message:
            color_code = self.COLORS.get(color.lower(), self.COLORS["default"])
            print(f"{color_code}{char}", end="", flush=True)
            time.sleep(type_vel / 1000)

        if wrap_line:
            print(f"{self.COLORS['default']}")  # Retorna ao estilo de texto padrão

    def render_menu(self, menu_items):
        while True:
            for i, item in enumerate(menu_items):
                self.type_message(f"{i+1}. ", color="green", wrap_line=False)
                self.type_message(f"{item}")

            self.type_message("Escolha um número: ", color="cyan", wrap_line=False)

            try:
                user_choice = int(input())
                if 1 <= user_choice <= len(menu_items):
                    return menu_items[user_choice - 1]
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

    def run_forever(self):
        while self.running:
            try:
                # Atualização contínua da tela
                time.sleep(1)
            except KeyboardInterrupt:
                self.close()

    def close(self):
        self.running = False
        sys.exit()  # Sai do programa


# Exemplo de uso
if __name__ == "__main__":
    ui = TerminalUI()
    ui.type_message("Hello world!", color="green")
    lost = ["Kaic", "Salomao"]
    selected = ui.render_menu(lost)
    ui.type_message(selected, color="blue")
    ui.run_forever()
