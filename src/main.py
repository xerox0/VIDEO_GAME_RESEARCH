import requests,bs4

url = input('Inserisci l\'URL:')

res = requests.get(url)

try:
    res.raise_for_status()
except Exception as exc:
    print(f'si è verificato questo problema: {exc}')

html_page = bs4.BeautifulSoup(res.text, 'html.parser')
elem_html = '.article__content'

sel_elem = html_page.select(elem_html)

text_elem = sel_elem[0].getText()
with open ('testo.text', 'w') as testo:
    testo.write(text_elem)

print('File aggiornato')