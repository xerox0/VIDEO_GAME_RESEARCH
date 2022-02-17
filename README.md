# Videoooogame
Videooogame è un search engine verticale che permette di cercare videogiochi. Si può cercare digitando il titolo, e/o 
una o più parole della descrizione del gioco. È disponibile anche filtrare questi risultati in base allo sviluppatore 
e/o alla piattaforma (console) per la quale è disponibile il gioco.
 I dati sono stati scaricati da due siti Web:  
```https://multiplayer.it```  
```https://www.instant-gaming.com/it```  
  
## Requisiti
Per lo sviluppo del search engine sono stati utilizzati:  
Python 3.8.10  
Flask 1.1.2  
Whoosh 2.7.4  
Beautifulsoup4 4.8.2

## Come usare il search engine  
Per avviare l'applicazione, andare nella directory video_games_research/UI e digitare  ```
flask run```.  
Nel codice sono già presenti i file con i dati dei videogiochi, scaricati dai rispettivi siti Web. Sono stati scaricati
dati di oltre 2000 videogiochi. Se si vuole rieseguire lo scraping,e di conseguenza ricostruire gli indici,
 basta eseguire dalla directory ```src```  i
comandi:  
```python3 scraping_instant_gaming.py```  
```python3 scraping_multiplayer.py```  
```python3 create_index.py```


## Ricerca e query language  
Nell'interfaccia sono presenti tre caselle di testo: la prima permette di cercare termini presenti nel titolo e/o nella
descrizione del gioco. La ricerca predefinita è in OR, ma  è possibile usare anche altri operatori booleani, ad esempio 
AND. È ammessa anche la ricerca per frasi, basta inserire i termini all'interno di doppi apici, ad esempio `"super mario"` .  
La seconda e la terza casella di testo permettono, rispettivamente, la ricerca per sviluppatore e per piattaforma (cioè 
la console sulla quale si può giocare). Essi sono campi progettati per essere filtri della ricerca "principale", cioè del 
titolo/descrizione; ciò vuol dire che se si prova ad effettuare una ricerca inserendo lo sviluppatore e la piattaforma ma 
lasciando vuota la prima casella di testo, la ricerca non restituirà alcun risultato.

## Benchmark  
Nel file "Benchmark" sono presenti 10 query, espresse prima in linguaggio naturale e poi in linguaggio di interrogazione.  
La nostra interfaccia prevede tre caselle di testo , di cui due di filtro ```filtro_platform``` e ```filtro_developer```.  
Nelle query dove vogliamo usare questi filtri, abbiamo specificato in quale casella va digitato il testo.
