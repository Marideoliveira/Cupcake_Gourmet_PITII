from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("cardapio.html")

@app.route("/pedido", methods=["GET", "POST"])
def pedido():
    if request.method == "POST":
        nome = request.form["nome"]
        cep = request.form["cep"]
        rua = request.form["rua"]
        numero = request.form["numero"]
        complemento = request.form["complemento"]
        bairro = request.form["bairro"]
        cidade = request.form["cidade"]
        estado = request.form["estado"]
        pagamento = request.form["pagamento"]
        sabores = request.form.getlist("sabores")

        return render_template(
            "pagamento.html",
            nome=nome,
            cep=cep,
            rua=rua,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            pagamento=pagamento,
            sabores=sabores
        )

    sabores = request.args.getlist("sabores")
    return render_template("pedido.html", sabores=sabores)

@app.route("/status")
def status():
    return render_template("status.html")

if __name__ == "__main__":
    app.run(debug=True)
