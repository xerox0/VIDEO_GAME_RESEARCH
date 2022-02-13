from flask import Flask, render_template, request, redirect

from src import processing_query
from processing_query import
# configurazioni iniziali
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['POST', 'GET'])
def home():  # put application's code here
    # if request.method == 'POST':
    #     task_content = request.form['content']  # è l'attributo name del form
    #     #  qui passo i term inseriti alla funzione di ricerca
    #     return redirect('/results.html')
    # else:
        return render_template('index.html')
# dopo index.html ci va un'eventuale contenuto da passare alla pagina


@app.route('/results.html', methods=['POST', 'GET'])
def risultati():
    query = {'text': request.args.get('generic'), 'developer': request.args.get('developer'),
             'platform': request.args.get('platform')}
    list = process_query
    """processare la query qui. mandarla ai due indici. Pseudocodice:
        x= process_query(query, 'instant_gaming') # ritorna i risultati della query. In process cercherà sia in instant gaming, sia in m
        multiplayer
        y = process_query(query, 'multiplayer')
        risultati = threshold (x,y)
        renderizza risultati a results.html
        """
    # text_stemmed = create_index.preprocessing(query)
    return render_template('results.html', data=list)


if __name__ == '__main__':
    app.run(debug=True)
