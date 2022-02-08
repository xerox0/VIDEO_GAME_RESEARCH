from flask import Flask, render_template, request, redirect

# configurazioni iniziali
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        task_content = request.form['content']  # è l'attributo name del form
        #  qui passo i term inseriti alla funzione di ricerca
        return redirect('/results.html')
    else:
        return render_template('index.html')
# dopo index.html ci va un'eventuale contenuto da passare alla pagina


@app.route('/results.html', methods=['POST', 'GET'])
def risultati():
    pass


if __name__ == '__main__':
    app.run(debug=True)
