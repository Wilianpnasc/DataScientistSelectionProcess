# Requests para todos os países, parceiros e anos

# Lista completa de países
lista_paises = ['BRA', 'ARG', 'AFG']

# Função simulada para obter os dados de comércio
def get(pais_origem, pais_destino, ano):
    return f"Dados de {pais_origem} para {pais_destino} no ano {ano}"

# Iterar sobre países de origem, destino e anos
for pais_origem in lista_paises:
    for pais_destino in lista_paises:
        if pais_origem != pais_destino:  # Evitar auto-referência
            for ano in ['2019', '2020', '2021']:
                res = get(pais_origem, pais_destino, ano)
                # Salvar os dados (ver Etapa 2)
                with open(f"{pais_origem}/{pais_destino}_{ano}.txt", 'w') as file:
                    file.write(res)


# Salvar arquivo
import os

# Função para salvar os dados
def save_response(pais_origem, pais_destino, ano, data):
    diretorio = f"{pais_origem}"
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    caminho_arquivo = f"{diretorio}/{pais_destino}_{ano}.txt"
    with open(caminho_arquivo, 'w') as file:
        file.write(data)

