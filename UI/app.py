import sys
sys.path.append("..")
from flask import Flask, render_template, request
from src import processing_query

# configurazioni iniziali
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results.html', methods=['GET', 'POST'])
def risultati():
    query = {'text': request.args.get('generic'), 'developer': request.args.get('developer'),
             'platform': request.args.get('platform')}
    print(query)
    results_list = processing_query.process_query(query, 'multiplayer')
    """processare la query qui. mandarla ai due indici. Pseudocodice:
        x= process_query(query, 'instant_gaming') # ritorna i risultati della query. In process cercherà sia in instant gaming, sia in m
        multiplayer
        y = process_query(query, 'multiplayer')
        risultati = threshold (x,y)
        renderizza risultati a results.html
        """
    print(results_list)
    # text_stemmed = create_index.preprocessing(query)
    return render_template('results.html', data=results_list, query=query)


if __name__ == '__main__':
    app.run(debug=True)
