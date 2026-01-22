# 💱 Monitor de Cotações de Moedas

Aplicação em Python que permite consultar **cotações de moedas em tempo real** e realizar **conversões de valores**, utilizando uma interface web simples e interativa construída com **Streamlit**.

Os dados de câmbio são obtidos diretamente da **AwesomeAPI**, garantindo informações atualizadas.

---

## Funcionalidades

- Consulta de cotação atual entre pares de moedas
- Conversão de valores com base na cotação atual
- Registro do histórico de consultas
- Integração com API externa (AwesomeAPI)
- Interface gráfica interativa via Streamlit

---

## 🪙 Moedas Disponíveis

- USD (Dólar Americano)
- EUR (Euro)
- BRL (Real Brasileiro)
- BTC (Bitcoin)
- JPY (Iene Japonês)
- GBP (Libra Esterlina)
- AUD (Dólar Australiano)
- CAD (Dólar Canadense)
- CHF (Franco Suíço)
- CNY (Yuan Chinês)

---

## Tecnologias Utilizadas

- **Python 3**
- **Streamlit**
- **Requests**
- **AwesomeAPI (Economia)**

---

## 📂 Estrutura do Projeto

```

📁 projeto/
├── main.py          # Regras de negócio, integração com API e histórico
├── etapa1.py        # Funções de cotação e conversão
├── app.py           # Interface Streamlit
└── README.md

````

---

## Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/felipebarbosadesu/streamlit-cotacao-api
cd seu-repositorio
````

### 2️⃣ Crie um ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install streamlit requests
```

### 4️⃣ Execute a aplicação

```bash
streamlit run app.py
```

---

## 🔌 API Utilizada

* **AwesomeAPI - Economia**
* Endpoint:

```
https://economia.awesomeapi.com.br/json/last/{MOEDA_ORIGEM}-{MOEDA_DESTINO}
```

Exemplo:

```
USD-BRL
```

---

## 📈 Possíveis Melhorias Futuras

* Persistência do histórico em banco de dados
* Gráficos de variação cambial
* Testes automatizados
* Tratamento avançado de erros da API
* Deploy em cloud (Streamlit Cloud ou Heroku)

---

## 👨‍💻 Autor Felipe Barbosa

Projeto desenvolvido para fins de estudo e prática em:

* Consumo de APIs
* Organização de código Python
* Interfaces simples com Streamlit

```

---
