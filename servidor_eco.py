import socket
import threading

HOST, PORT = "127.0.0.1", 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))
s.listen()

print(f"[servidor] ouvindo em {HOST}:{PORT}", flush=True)


def atender_cliente(conexao, endereco):
    """Atende um cliente individualmente."""
    print(f"[servidor] cliente conectado: {endereco}", flush=True)

    while True:
        dado = conexao.recv(1024)

        if not dado:
            # Cliente fechou a conexão
            break

        print(
            f"[servidor] recebi de {endereco}: {dado.decode()}",
            flush=True
        )

        # ECO: devolve a mesma mensagem
        conexao.sendall(dado)

    conexao.close()
    print(f"[servidor] cliente desconectado: {endereco}", flush=True)


while True:
    # Fica aguardando novos clientes
    conexao, endereco = s.accept()

    # Cria uma thread para atender esse cliente
    thread = threading.Thread(
        target=atender_cliente,
        args=(conexao, endereco)
    )

    thread.start()
