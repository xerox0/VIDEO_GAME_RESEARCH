
#from src import processing_query
#from video_games_research.src.merging_ranking import threshold_edited
from flask import Flask, render_template, request, redirect

# configurazioni iniziali
from video_games_research.src.processing_query import process_query
from video_games_research.src.merging_ranking import  threshold_edited

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
    results_multiplayer = process_query(query, 'multiplayer')
    results_instant_gaming = process_query(query, 'instant_gaming')


    #l1 = loaddata(results_multiplayer)
    #l2 = loaddata(results_instant_gaming)
    merged_results = threshold_edited(results_multiplayer, results_instant_gaming, 5)  # dizionario con risultati

    return render_template('results.html', data=merged_results, query=query)


if __name__ == '__main__':
    app.run(debug=True)
