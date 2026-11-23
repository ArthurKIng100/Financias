# Controle de Finanças Pessoais

Fiz esse projeto para praticar **Python**, **Flask** e **Programação Orientada a Objetos** na prática, juntando lógica de back-end com uma interface web simples em **HTML** e **CSS**.

A ideia aqui foi não jogar tudo dentro de um arquivo só e separar bem o papel de cada parte do sistema:

- **`lancamento.py`**: representa cada gasto registrado (valor, categoria e data).
- **`carteira.py`**: guarda os lançamentos, controla o saldo inicial e calcula quanto ainda sobra.
- **`grafico.py`**: faz a conta das porcentagens por categoria para alimentar as barras na tela.
- **`app.py`**: recebe os dados dos formulários e manda tudo organizado para o template.
- **`templates/tela.html` e `static/style.css`**: montam a tela, o histórico e as barras de progresso por categoria.

## O que dá para fazer nele
- Definir um saldo inicial e acompanhar o saldo atual conforme os gastos entram.
- Cadastrar gastos escolhendo categoria e data.
- Ver na hora quanto cada categoria representa no total através das barras coloridas.
- Consultar o histórico de lançamentos e limpar tudo quando quiser começar do zero.

## Como rodar na sua máquina

Você precisa ter o Python instalado. No terminal, dentro da pasta do projeto:

```bash
pip install flask
python app.py
