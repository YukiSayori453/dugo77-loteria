from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sorte777'  # necessário para armazenar os números selecionados

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamento', methods=['POST'])
def pagamento():
    selecionados = request.form.getlist('numeros')
    if len(selecionados) != 15:
        return "Você precisa escolher exatamente 15 números.", 400
    session['numeros'] = selecionados
    return render_template('pagamento.html')

@app.route('/sucesso')
def sucesso():
    numeros = session.get('numeros', [])
    return render_template('sucesso.html', numeros=numeros)

if __name__ == '__main__':
    app.run(debug=True)