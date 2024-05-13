import requests
from bs4 import BeautifulSoup
import json

def get_author_details(author_url):
    response = requests.get(author_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    fullname = soup.find('h3', class_='author-title').text.strip()
    born_date = soup.find('span', class_='author-born-date').text.strip()
    born_location = soup.find('span', class_='author-born-location').text.strip()
    description = soup.find('div', class_='author-description').text.strip()
    return {
        'fullname': fullname,
        'born_date': born_date,
        'born_location': born_location,
        'description': description
    }


quotes_data = []
authors_data = []
authors_set = set()


url = "http://quotes.toscrape.com/page/{}/"
page = 1

while True:
    response = requests.get(url.format(page))
    if "No quotes found!" in response.text:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text.strip()
        author = quote.find('small', class_='author').text.strip()
        tags = [tag.text.strip() for tag in quote.find_all('a', class_='tag')]
        quote_data = {
            'quote': text,
            'author': author,
            'tags': tags
        }
        quotes_data.append(quote_data)

        if author not in authors_set:
            author_url = "http://quotes.toscrape.com" + quote.find('a')['href']
            author_details = get_author_details(author_url)
            authors_data.append(author_details)
            authors_set.add(author)

    page += 1


with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(quotes_data, f, ensure_ascii=False, indent=4)

with open('authors.json', 'w', encoding='utf-8') as f:
    json.dump(authors_data, f, ensure_ascii=False, indent=4)

print("Дані успішно зібрано та збережено у файли quotes.json та authors.json")


#Команди для імпорту
#mongoimport --uri "mongodb+srv://bond1qdev:54Md4qkso7tCCiF@goitlearn.rkpgekc.mongodb.net/hw_2" --collection authors --file authors.json --jsonArray
#mongoimport --uri "mongodb+srv://bond1qdev:54Md4qkso7tCCiF@goitlearn.rkpgekc.mongodb.net/hw_2" --collection quotes --file quotes.json --jsonArray