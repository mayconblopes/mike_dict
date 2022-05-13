import bs4
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'index.html')


def search(request):
    word = request.GET['word'].lower()
    res = requests.get('https://www.dicio.com.br/pesquisa.php?q=' + word)

    if res and word:
        soup = BeautifulSoup(res.text, 'lxml')
        scraping = soup.find_all('p', {'itemprop': 'description'})
        print(scraping)
        scraping_text = scraping[0].get_text('@@', strip=True)
        print(scraping_text)
        scraping_text = scraping_text.split('@@')

    else:
        word = f'A palavra {word} não foi encontrada'
        scraping_text = ''

    return render(request, 'search.html', {
        'word': word,
        'scraping_text': scraping_text,
    })
