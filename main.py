import sys
from HTMLParser import HTMLParser
from flask import *
app = Flask(__name__)
jugadores = {
        'b2': [
                    {'nombre': "Ignaciouy", 'posicion': 'jungla', 'server': 'lan'},
                    {'nombre': "Ignaciouy2", 'posicion': 'adc', 'server': 'las'},
                    {'nombre': "Caca", 'posicion': 'jungla', 'server': 'las'},
                    {'nombre': "Caca2", 'posicion': 'jungla', 'server': 'las'},
                    {'nombre': "Ignaciouy2", 'posicion': 'adc', 'server': 'las'},
            ]
}

@app.route('/')
def index():
    return "Jugadores de prueba: Ignaciouy - B2 - Jungla"


@app.route('/busqueda/<servidor>-<division>-<posicion>')
def busqueda(servidor, division, posicion):
    txt = "Jugadores encontrados<br>"
    for jugador in jugadores[division]:
        if jugador['server'] == servidor.lower() and jugador['posicion'] == posicion.lower():
            txt += 'Nick: %s<br>Division: %s<br>Posicion: %s<br><br>' %(jugador['nombre'], division, jugador['posicion'])
    return txt

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(sys.argv[1]))
