# README — Servidor Eco TCP com Múltiplos Clientes

Este projeto demonstra uma comunicação **cliente-servidor utilizando sockets TCP em Python**.

O servidor funciona como um **servidor de eco (Echo Server)**: ele recebe uma mensagem enviada por um cliente e devolve exatamente a mesma mensagem para ele.

Nesta versão o servidor consegue atender **vários clientes ao mesmo tempo** utilizando `threading`.

## 📂 Arquivos

```text
.
├── servidor_eco.py
└── cliente_eco.py
```

### `servidor_eco.py`

É responsável por:

* Criar o socket TCP.
* Reservar a porta `5000`.
* Aguardar conexões.
* Aceitar vários clientes.
* Criar uma thread para cada cliente.
* Receber mensagens.
* Devolver as mensagens para o cliente que as enviou.

### `cliente_eco.py`

É responsável por:

* Criar uma conexão TCP.
* Conectar-se ao servidor através de `127.0.0.1:5000`.
* Enviar mensagens.
* Receber o eco do servidor.
* Encerrar a conexão quando o usuário digitar `sair`.

## 🧵 Múltiplos clientes

O servidor utiliza `threading` para atender vários clientes simultaneamente.

Quando um cliente se conecta, o servidor cria uma nova thread:

```python
thread = threading.Thread(
    target=atender_cliente,
    args=(conexao, endereco)
)

thread.start()
```

Dessa forma, enquanto uma thread está atendendo o Cliente 1, outra pode atender o Cliente 2.

```text
                  SERVIDOR
                     │
          ┌──────────┴──────────┐
          │                     │
      Thread 1              Thread 2
          │                     │
      Cliente 1              Cliente 2
```

## ▶️ Como executar

Primeiro, execute o servidor:

```bash
python servidor_eco.py
```

Será exibido algo parecido com:

```text
[servidor] ouvindo em 127.0.0.1:5000
```

Depois, abra **dois terminais diferentes** e execute o cliente em cada um:

```bash
python cliente_eco.py
```

Você terá dois clientes conectados ao mesmo servidor.

No servidor será possível observar as duas conexões:

```text
[servidor] cliente conectado: ('127.0.0.1', 54321)
[servidor] cliente conectado: ('127.0.0.1', 54322)

[servidor] recebi de ('127.0.0.1', 54321): Olá!
[servidor] recebi de ('127.0.0.1', 54322): Oi servidor!
```

## 🧪 Objetivo

O projeto tem como objetivo demonstrar conceitos básicos de:

* Comunicação em rede.
* Protocolo **TCP**.
* Sockets em Python.
* Arquitetura cliente-servidor.
* Comunicação entre múltiplos clientes.
* Uso de `threading`.
* Envio e recebimento de dados através de sockets.
