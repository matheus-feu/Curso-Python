# Exemplo de execução de uma função em separadas threads
from threading import Thread
from time import sleep


# Função que será executada em uma thread
def task():
    sleep(3)
    print('Executando uma task em uma thread')


# Criando uma thread e configurando para executar a função task
thread = Thread(target=task)

# Iniciando a thread
thread.start()

# Imprimindo uma mensagem enquanto a thread é executada
print('Executando o programa enquanto a thread é executada...')

# Aguardando a thread terminar
thread.join()
