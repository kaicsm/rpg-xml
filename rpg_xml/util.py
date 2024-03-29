import sys, time, os, tty, termios


def read_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key


def clear_terminal():
    # Windows
    if os.name == "nt":
        _ = os.system("cls")
    # MacOS e Linux
    else:
        _ = os.system("clear")


def type_message(msg, type_vel=50, delay_before=0, wrap_line=True):
    # Espera o delay especificado antes de começar
    time.sleep(from_milis(delay_before))

    # Imprime a mensagem letra por letra com o atraso especificado
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(from_milis(type_vel))

    # Quebra a linha se a opção estiver ativada
    if wrap_line:
        print()


def from_milis(value):
    return value / 1000
