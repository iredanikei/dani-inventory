from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


def obtener_objetos():

    excel = pd.read_excel("inventario.xlsx")

    objetos = excel.to_dict(orient="records")

    return objetos
@app.route("/")
def inicio():

    objetos = obtener_objetos()

    return render_template(
        "index.html",
        objetos=objetos
    )
@app.route("/objeto/<int:id>")
def detalle_objeto(id):

    objetos = obtener_objetos()

    objeto_encontrado = None

    for objeto in objetos:

        if objeto["id"] == id:

            objeto_encontrado = objeto

    return render_template(
        "detalle.html",
        objeto=objeto_encontrado
    )
app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
)