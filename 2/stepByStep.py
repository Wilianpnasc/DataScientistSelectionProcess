# Importar as bibliotecas necessárias
import requests  # Para fazer requisições HTTP
import zipfile   # Para lidar com arquivos zip
import os        # Para interagir com o sistema de arquivos
import pandas as pd  # Para trabalhar com dataframes de dados
from datetime import datetime  # Para lidar com datas e horas

# Definir a URL base de onde baixaremos os arquivos
url_base = "http://200.152.38.155/CNPJ/"

# Listar nomes dos arquivos que queremos baixar
arquivos = [f"Empresas0{i}.zip" for i in range(10)]

# Baixar um arquivo da internet
def baixar_arquivo(url, destino):
    try:
        # Fazendo a requisição HTTP para o arquivo
        resposta = requests.get(url, stream=True)
        
        # Verificando se a requisição foi bem sucedida (código 200)
        if resposta.status_code == 200:
            # Abrindo o arquivo local para escrita em modo binário ('wb')
            with open(destino, 'wb') as f:
                # Escrevendo os dados recebidos no arquivo local em pedaços de 128 bytes
                for chunk in resposta.iter_content(chunk_size=128):
                    f.write(chunk)
            return True
        else:
            return False
    except Exception as e:
        # Se ocorrer algum erro, imprime uma mensagem de erro
        print(f"Erro ao baixar {url}: {e}")
        return False

# Loop para baixar cada arquivo da lista
for arquivo in arquivos:
    # Montando a URL completa para o arquivo atual
    url = f"{url_base}{arquivo}"
    # Definindo o caminho onde o arquivo será salvo localmente
    destino = f"./downloads/{arquivo}"
    
    # Verificando se o download foi bem sucedido
    if not baixar_arquivo(url, destino):
        print(f"Falha ao baixar {arquivo}")

# Loop para extrair os arquivos zip
for arquivo in arquivos:
    # Definindo o caminho do arquivo zip baixado
    caminho_zip = f"./downloads/{arquivo}"
    
    try:
        # Tentando extrair o conteúdo do arquivo zip
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            # Extraindo todos os arquivos para o diretório './extracted'
            zip_ref.extractall("./extracted")
    except zipfile.BadZipFile:
        # Se o arquivo estiver corrompido, imprime uma mensagem de aviso
        print(f"Arquivo corrompido: {caminho_zip}")

# Listar armazenamento dos dataframes de cada arquivo CSV extraído
dataframes = []

# Loop para carregar e empilhar os arquivos CSV
for arquivo in arquivos:
    # Montando o caminho completo para o arquivo CSV extraído
    caminho_csv = f"./extracted/{arquivo.replace('.zip', '.csv')}"
    
    # Verificando se o arquivo CSV existe no diretório 'extracted'
    if os.path.exists(caminho_csv):
        # Carregando o arquivo CSV para um dataframe do pandas
        df = pd.read_csv(caminho_csv)
        # Adicionando o dataframe à lista de dataframes
        dataframes.append(df)
    else:
        # Se o arquivo não for encontrado, imprime uma mensagem de aviso
        print(f"Arquivo não encontrado: {caminho_csv}")

# Concatenar os dataframes em um único dataframe consolidado
df_consolidado = pd.concat(dataframes, ignore_index=True)

# Obter a data atual no formato 'YYYYMMDD'
data_atualizacao = datetime.now().strftime('%Y%m%d')

# Salvar o dataframe consolidado como um arquivo CSV
df_consolidado.to_csv(f"./consolidated/dataset_{data_atualizacao}.csv", index=False)

# Indicativo término do script 
print("Processamento concluído. Dataset consolidado salvo com sucesso!")
