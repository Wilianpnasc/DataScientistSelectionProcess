from datetime import datetime

def coletar_dados(pais_origem, pais_destino, ano, tipo):
    if tipo == 'A':
        return f"Dados anuais completos de {pais_origem} para {pais_destino} no ano {ano}"
    else:
        mes_atual = datetime.now().month
        return f"Dados mensais disponíveis até o mês {mes_atual} de {pais_origem} para {pais_destino} no ano {ano}"

def atualizar_dados():
    lista_paises = ['BRA', 'ARG', 'AFG']
    ano_atual = 2024
    for pais_origem in lista_paises:
        for pais_destino in lista_paises:
            if pais_origem != pais_destino:
                res_anual = coletar_dados(pais_origem, pais_destino, ano_atual, 'A')
                save_response(pais_origem, pais_destino, ano_atual, res_anual)
                res_mensal = coletar_dados(pais_origem, pais_destino, ano_atual, 'M')
                save_response(pais_origem, pais_destino, ano_atual, res_mensal)

def save_response(pais_origem, pais_destino, ano, data, tipo=''):
    if tipo == 'A':
        caminho_arquivo = f"{pais_origem}/{pais_destino}_{ano}_anual.txt"
    else:
        caminho_arquivo = f"{pais_origem}/{pais_destino}_{ano}_mensal.txt"
    if not os.path.exists(os.path.dirname(caminho_arquivo)):
        os.makedirs(os.path.dirname(caminho_arquivo))
    with open(caminho_arquivo, 'w') as file:
        file.write(data)

# Chamando a função para atualizar os dados
atualizar_dados()
