import sys, time, os, tty, termios


def ler_tecla():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        tecla = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return tecla


def limpar_terminal():
    # Comando para Windows
    if os.name == "nt":
        _ = os.system("cls")
    # Comando para MacOS e Linux(here, os.name is 'posix')
    else:
        _ = os.system("clear")


# Modifique a função para incluir o atraso antes de falar e a opção de quebrar a linha
def narrar_historia(mensagem, tom="normal", atraso_antes=0, quebrar_linha=True):
    # Define o atraso entre cada caractere com base no tom
    atrasos_tom = {
        "normal": 0.05,
        "excitado": 0.02,
        "sussurro": 0.1,
        "lento": 0.1,
        "rapido": 0.01,
    }

    # Obtém o atraso para o tom especificado, padrão para normal se não encontrado
    atraso = atrasos_tom.get(tom, atrasos_tom["normal"])

    # Espera o delay especificado antes de começar a falar
    time.sleep(atraso_antes / 1000)

    # Imprime a mensagem letra por letra com o atraso especificado
    for char in mensagem:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)

    # Quebra a linha se a opção estiver ativada
    if quebrar_linha:
        print()
