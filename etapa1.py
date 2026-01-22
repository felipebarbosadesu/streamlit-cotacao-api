import requests

# 1. Lista global para armazenar as consultas
historico = []

def registrar_historico(moeda_b, moeda_d, valor):
    """
    Adiciona as informações da conversão à lista 'historico'.
    """
    registro = {
        "origem": moeda_b,
        "destino": moeda_d,
        "cotacao": valor
    }
    historico.append(registro)

def buscar_cotacao(moeda_base, moeda_destino):
    """
    Acessa a AwesomeAPI, busca o valor e salva no histórico.
    """
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_base}-{moeda_destino}"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        
        # A chave no JSON da API é a junção das moedas (ex: USDBRL)
        chave = f"{moeda_base}{moeda_destino}"
        
        if chave in dados:
            valor_atual = dados[chave]['bid']
            
            # Exibe no terminal conforme solicitado
            print(f"Cotação Atual ({moeda_base}/{moeda_destino}): {valor_atual}")
            
            # Chama a função de registro
            registrar_historico(moeda_base, moeda_destino, valor_atual)
            
            return valor_atual
        else:
            print(f"⚠️ Par de moedas {moeda_base}-{moeda_destino} não encontrado.")
            return None
            
    except Exception as e:
        print(f"❌ Erro ao conectar com a API: {e}")
        return None

# --- EXECUÇÃO DO PROJETO ---

if __name__ == "__main__":
    print("--- 🚀 INICIANDO CONSULTAS ---")
    
    # Fazendo algumas consultas de teste
    buscar_cotacao("USD", "BRL")  # Dólar para Real
    buscar_cotacao("EUR", "BRL")  # Euro para Real
    buscar_cotacao("BTC", "BRL")  # Bitcoin para Real

    # Mostrando o histórico final
    print("\n--- 📜 HISTÓRICO DE CONVERSÕES ---")
    for item in historico:
        print(f"Moeda: {item['origem']} | Destino: {item['destino']} | Valor: {item['cotacao']}")
    print("-" * 34)

def rota_converter(valor, moeda_origem, moeda_destino):
    taxa_cambio = float(buscar_cotacao(moeda_origem, moeda_destino))
    if taxa_cambio > 0: 
        valor_convertido = valor * taxa_cambio
        return valor_convertido
    else:
        return valor