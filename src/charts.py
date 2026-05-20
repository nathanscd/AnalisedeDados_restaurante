from pathlib import Path
import plotly.express as px

BASE = Path(__file__).resolve().parent.parent
PASTA = BASE / "output"


def criar_graficos(df):

    x1 = (
        df.groupby('filial')['total']
        .sum()
        .reset_index()
    )

    g1 = px.bar(
        x1,
        x='filial',
        y='total'
    )

    x2 = (
        df.groupby('data')['total']
        .sum()
        .reset_index()
    )

    g2 = px.line(
        x2,
        x='data',
        y='total'
    )

    x3 = (
        df.groupby('produto')['qtd']
        .sum()
        .reset_index()
    )

    g3 = px.bar(
        x3,
        x='produto',
        y='qtd'
    )

    x4 = (
        df.groupby('pagamento')
        .size()
        .reset_index(name='qtd')
    )

    g4 = px.pie(
        x4,
        names='pagamento',
        values='qtd'
    )

    g1.write_html(PASTA / "filiais.html")
    g2.write_html(PASTA / "dias.html")
    g3.write_html(PASTA / "produtos.html")
    g4.write_html(PASTA / "pagamentos.html")