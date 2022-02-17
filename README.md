# Videoooogame
Videooogame è un search engine verticale che permette di cercare videogiochi. Si può cercare digitando il titolo, e/o 
una o più parole della descrizione del gioco. È disponibile anche filtrare questi risultati in base allo sviluppatore 
e/o alla piattaforma (console) per la quale è disponibile il gioco. 
##Requisiti
Per lo sviluppo del search engine sono stati utilizzati:  
Python 3.8.10  
Flask 1.1.2  
Whoosh 2.7.4  
##Ricerca e query language
Nell'interfaccia sono presenti tre caselle di testo: la prima permette di cercare termini presenti nel titolo e/o nella
descrizione del gioco. La ricerca predefinita è in OR, ma  è possibile usare anche altri operatori booleani, ad esempio 
AND. È ammessa anche la ricerca per frasi, basta inserire i termini all'interno di doppi apici, ad esempio `"super mario"`.  
La seconda e la terza casella di testo permettono, rispettivamente, la ricerca per sviluppatore e per piattaforma (cioè 
la console sulla quale si può giocare). Essi sono campi progettati per essere filtri della ricerca "principale", cioè del 
titolo/descrizione; ciò vuol dire che se si prova ad effettuare una ricerca inserendo lo sviluppatore e la piattaforma ma 
lasciando vuota la prima casella di testo, la ricerca non restituirà alcun risultato.

##Benchmark
Nel file "Benchmark" sono presenti 10 UIN, espressi quindi 
