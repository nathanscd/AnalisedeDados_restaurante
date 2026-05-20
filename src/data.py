import pandas as pd
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent

ARQUIVO = BASE / "dados_restaurante.csv"

PASTA = BASE / "output"

PASTA.mkdir(exist_ok=True)


def arrumar_data(x):

    x = str(x)

    try:

        partes = x.split('/')

        n = int(partes[0])

        if n > 12:

            return pd.to_datetime(
                x,
                format='%d/%m/%Y',
                errors='coerce'
            )

        return pd.to_datetime(
            x,
            format='%m/%d/%Y',
            errors='coerce'
        )

    except:

        return pd.NaT


def pegar_dados():

    tabela = pd.read_csv(ARQUIVO)

    tabela.columns = [
        'data',
        'filial',
        'produto',
        'qtd',
        'preco',
        'pagamento',
        'funcionario',
        'total'
    ]

    tabela['data'] = tabela['data'].apply(
        arrumar_data
    )

    tabela = tabela.dropna(
        subset=['data']
    )

    tabela = tabela[
        tabela['data'].dt.year > 2000
    ]

    nomes = {
        'COCA LATA': 'Coca-Cola 350ml',
        'Refri Cola': 'Coca-Cola 350ml'
    }

    tabela['produto'] = tabela[
        'produto'
    ].replace(nomes)

    nums = [
        'qtd',
        'preco',
        'total',
        'funcionario'
    ]

    for x in nums:

        tabela[x] = pd.to_numeric(
            tabela[x],
            errors='coerce'
        )

    tabela['funcionario'] = (
        tabela['funcionario']
        .fillna(999)
        .astype(int)
    )

    tabela['pagamento'] = (
        tabela['pagamento']
        .fillna('Não informado')
    )

    m1 = (
        tabela['qtd'].isna()
        &
        tabela['total'].notna()
    )

    tabela.loc[m1, 'qtd'] = (
        tabela['total']
        /
        tabela['preco']
    )

    m2 = tabela['total'].isna()

    tabela.loc[m2, 'total'] = (
        tabela['qtd']
        *
        tabela['preco']
    )

    tabela = tabela.drop_duplicates()

    tabela.to_csv(
        PASTA / "dados_limpos.csv",
        index=False
    )

    return tabela