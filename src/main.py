from data import pegar_dados
from charts import criar_graficos


df = pegar_dados()

criar_graficos(df)

print()

print("feito")
print("dados_limpos.csv")
print("filiais.html")
print("dias.html")
print("produtos.html")
print("pagamentos.html")