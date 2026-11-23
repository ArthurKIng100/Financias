from flask import Flask, render_template, request
from carteira import Carteira
from grafico import Grafico
from lancamento import Lancamento

app = Flask(__name__)
carteira = Carteira()
grafico = Grafico(carteira)

CATEGORIAS = [
    ("comida", "Comida"),
    ("transporte", "Transporte"),
    ("lazer", "Lazer"),
    ("fixos", "Fixos"),
]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "definir_saldo":
            saldo_disponivel = request.form.get("saldo_disponivel")
            if saldo_disponivel is not None and saldo_disponivel != "":
                carteira.definir_saldo_inicial(saldo_disponivel)

        elif acao == "adicionar_gasto":
            valor = request.form.get("valor")
            categoria = request.form.get("categoria")
            data = request.form.get("data")
            if valor and categoria and data:
                lancamento = Lancamento(
                    valor=valor,
                    categoria=categoria,
                    data=data,
                    tipo="saida",
                )
                carteira.adicionar(lancamento)

        elif acao == "limpar":
            carteira.limpar()

    total = carteira.total_geral()
    slugs = [slug for slug, _ in CATEGORIAS]
    percentuais = grafico.percentuais_por_categoria(slugs)

    itens_resumo = []
    for slug, nome in CATEGORIAS:
        itens_resumo.append({
            "slug": slug,
            "nome": nome,
            "valor": carteira.total_por_categoria(slug),
            "percentual": percentuais.get(slug, 0.0),
        })

    return render_template(
        "tela.html",
        saldo_inicial=carteira.saldo_inicial(),
        saldo_atual=carteira.saldo_atual(),
        total=total,
        itens_resumo=itens_resumo,
        lancamentos=carteira.lancamentos(),
    )


if __name__ == "__main__":
    app.run(debug=True)