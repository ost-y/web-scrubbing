import bs4
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'развития']

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')

article_block = soup.select_one('div.tm-articles-list')
article_list = article_block.select('article.tm-articles-list__item')

for article in article_list:

    title = article.select_one('h2.tm-title.tm-title_h2').text.strip()
    div_with_link = article.select_one('h2.tm-title.tm-title_h2')
    link = 'https://habr.com' + div_with_link.select_one('a')['href']
    time = article.select_one('time')['title']
    text = article.select_one('div.article-formatted-body.article-formatted-body_version-2')
    for word in KEYWORDS:
        if word in title or text:
            print({f'<{time}> – <{title}> – <{link}>'})




