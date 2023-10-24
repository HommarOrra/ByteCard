from flask import Flask, redirect, render_template
import use_cases
app = Flask(__name__)
@app.route ('/')
def index():
    return redirect('/cartoes/lista')
@app.route('/cartoes/lista')
def lista_cartoes():
    return render_template('cartao/lista.html', cartoes=use_cases.lista_cartoes())
if __name__ == '__main__':
    app.run(debug=True)
    
    