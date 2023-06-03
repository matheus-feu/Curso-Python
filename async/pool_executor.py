"""
A classe ThreadPoolExecutor estende a classe abstrata Executor.

A classe Executor define três métodos usados para controlar nosso pool de threads; eles são: submit() , map() e shutdown().

- submit() : Despacha uma função a ser executada e retorna um objeto futuro.
- map() : aplica uma função a um iterável de elementos.
- shutdown() : Desliga o executor.
"""
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from os.path import basename, join
from urllib.request import urlopen


# baixe um url e retorne os dados brutos, ou Nenhum em caso de erro
def download_url(url):
    try:
        # abrir uma conexão com o servidor
        with urlopen(url, timeout=5) as conn:
            # leia o conteúdo do documento html
            return conn.read(), url
    except Exception as e:
        # url ruim, tempo limite de soquete, http proibido, etc..
        return f'Erro ao ler a URL {url}: {e}', None


# Salvar o arquivo localmente
def save_file(url, data, path):
    # pegar o nome do arquivo da url
    filename = basename(url)
    # construir o caminho completo para o arquivo
    outpath = join(path, filename)
    # salvar o arquivo
    with open(outpath, 'wb') as f:
        f.write(data)
    return outpath


# baixar a lista de URLs para arquivos locais
def download_docs(urls, path):
    # criar um diretório local, se não existir
    os.makedirs(path, exist_ok=True)
    # criar um executor de pool de threads
    n_threads = len(urls)
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        # baixe cada url e salve como um arquivo local
        futures = [executor.submit(download_url, url) for url in urls]
        # aguardar a conclusão de todas as tarefas
        for future in as_completed(futures):
            # obter os dados de url baixados
            data, url = future.result()
            # verificar se o download foi bem sucedido
            if data is None:
                print(f'Erro ao baixar a URL {url}')
                continue
            # salvar o arquivo local
            outpath = save_file(url, data, path)
            # imprimir o caminho do arquivo salvo
            print(f'Salvo a {url} em {outpath}')


# lista de urls para baixar
URLS = ['https://docs.python.org/3/library/concurrency.html',
        'https://docs.python.org/3/library/concurrent.html',
        'https://docs.python.org/3/library/concurrent.futures.html',
        'https://docs.python.org/3/library/threading.html',
        'https://docs.python.org/3/library/multiprocessing.html',
        'https://docs.python.org/3/library/multiprocessing.shared_memory.html',
        'https://docs.python.org/3/library/subprocess.html',
        'https://docs.python.org/3/library/queue.html',
        'https://docs.python.org/3/library/sched.html',
        'https://docs.python.org/3/library/contextvars.html']

# local para salvar os arquivos
PATH = 'docs'

# baixar os documentos
download_docs(URLS, PATH)
