from src import processing_query
from src.merging_ranking import threshold_edited, loaddata
from flask import Flask, render_template, request, redirect

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

    # processo la query in entrambi gli indici
    results_multiplayer = processing_query.process_query(query, 'multiplayer')
    results_instant_gaming = processing_query.process_query(query, 'instant_gaming')

    # fusione dei risultati
    l1 = loaddata(results_multiplayer)
    l2 = loaddata(results_instant_gaming)
    merged_results = threshold_edited(l1, l2, 5) #dizionario con titoli e score, ora devo

    # text_stemmed = create_index.preprocessing(query)
    return render_template('results.html', data=merged_results, query=query)


if __name__ == '__main__':
    app.run(debug=True)
