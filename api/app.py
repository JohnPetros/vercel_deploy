from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


"""
1 2

"""


@app.route("/personalizada")
def home_perso():
    usu = "PASTEL DE COXINHA"
    # Para ler dados do BD ou csv (usar pandas)
    # criar a variável com os dados da lista
    # enviar para a aplicação de modo similar.
    user = {
        "name": "João Pedro",
        "course": "Desenvolvimento de Sistemas",
    }

    rows = 2
    columns = 2
    start = 1

    count = start - 1

    table = [[None for _ in range(columns)] for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            count += 1
            table[row][column] = count

    return render_template(
        "home_personalizada.html",
        usuario=usu,
        user=user,
        table=table,
    )


if __name__ == "__main__":
    app.run(debug=True)
