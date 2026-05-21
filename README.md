# 🍽️ SeuAlberto

Sistema de limpeza, normalização e análise de dados para uma rede de restaurantes com geração automática de dashboards e relatórios.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-black)
![Plotly](https://img.shields.io/badge/Plotly-Dashboard-purple)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

</p>

---

## 📖 Sobre o projeto

Este projeto foi desenvolvido simulando um problema real:

Uma rede com múltiplas unidades possuía dados inconsistentes e desorganizados, dificultando a geração de análises e indicadores confiáveis.

O objetivo foi construir uma solução de dados responsável por:

- Limpeza automática
- Normalização
- Tratamento de inconsistências
- Geração de métricas
- Dashboard interativo
- Exportação dos dados tratados

---

## ⚡ Problemas encontrados nos dados

Os dados originais apresentavam diversas inconsistências:

✅ Datas em formatos diferentes

```csv
15/05/2026
05/16/2026
```

✅ Produtos duplicados

```csv
COCA LATA
Refri Cola
Coca-Cola 350ml
```

✅ Valores ausentes

```csv
ID funcionário vazio
Forma de pagamento vazia
Quantidade vazia
Total vazio
```

✅ Dados inválidos

```csv
01/01/1900
```

✅ Registros duplicados

---

## 🧠 Solução implementada

O pipeline executa automaticamente:

### Tratamento de datas

Converte:

```text
DD/MM/YYYY
MM/DD/YYYY
```

para:

```text
YYYY-MM-DD
```

---

### Normalização de produtos

Transforma:

| Valor original | Resultado |
|---|---:|
| COCA LATA | Coca-Cola 350ml |
| Refri Cola | Coca-Cola 350ml |

---

### Tratamento de valores nulos

Campos ausentes recebem tratamento automático:

| Campo | Tratamento |
|---|---:|
| Funcionário | 999 |
| Pagamento | Não informado |
| Quantidade | Calculada |
| Total | Calculado |

---

### Remoção de inconsistências

- Remoção de datas inválidas
- Remoção de duplicidades
- Conversão automática de tipos

---

## 📂 Estrutura do projeto

```bash
SeuAlberto/

├── dados_restaurante.csv
│
├── src/
│   ├── main.py
│   ├── data.py
│   └── charts.py
│
├── output/
│   ├── dados_limpos.csv
│   ├── filiais.html
│   ├── dias.html
│   ├── produtos.html
│   └── pagamentos.html
│
├── gerar_pdf.py
│
└── README.md
```

---

## 🚀 Instalação

Clone o projeto:

```bash
git clone https://github.com/seu-usuario/SeuAlberto.git
```

Entre na pasta:

```bash
cd SeuAlberto
```

Crie ambiente virtual:

Windows:

```bash
python -m venv .venv
```

Linux/Mac:

```bash
python3 -m venv .venv
```

Ative:

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

Instale dependências:

```bash
pip install pandas plotly reportlab
```

---

## ▶️ Executando

Rodar processamento + dashboard:

```bash
python src/main.py
```

Gerar relatório:

```bash
python gerar_pdf.py
```

---

## 📊 Saída gerada

Após execução:

```bash
output/

dados_limpos.csv

filiais.html
dias.html
produtos.html
pagamentos.html

relatorio_final_restaurantes.pdf
```

---

## 📈 Dashboards disponíveis

### Receita por filial

Mostra desempenho das unidades.

---

### Receita diária

Permite visualizar tendência temporal.

---

### Produtos mais vendidos

Ranking por quantidade.

---

### Formas de pagamento

Distribuição dos métodos de pagamento utilizados.

---

## 💻 Tecnologias utilizadas

- Python
- Pandas
- Plotly
- ReportLab

---

## 🔍 Exemplo de resultado

Dataset original:

```csv
15/05/2026,Aldeota,COCA LATA
16/05/2026,Maraponga,Refri Cola
```

Dataset tratado:

```csv
2026-05-15,Aldeota,Coca-Cola 350ml
2026-05-16,Maraponga,Coca-Cola 350ml
```

---

## 📌 Possíveis melhorias futuras

- API REST
- Banco PostgreSQL
- Power BI
- Pipeline ETL
- Docker
- Machine Learning para previsão de demanda
- Sistema de autenticação
- Dashboard web em tempo real

---

## 🤝 Contribuição

Contribuições são bem-vindas.

```bash
fork → branch → commit → pull request
```

---

## 📄 Licença

Distribuído sob licença MIT.

---

<p align="center">

Desenvolvido por Nathanael 🚀

</p>
