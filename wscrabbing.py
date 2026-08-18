import bs4
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')

article_block = soup.select_one('div.tm-articles-list')
article_list = article_block.select('article.tm-articles-list__item')

parsed_data = []
for article in article_list:
   div_with_link = article.select_one('h2.tm-title.tm-title_h2')
   link = 'https://habr.com' + div_with_link.select_one('a')['href']
   # print(link)

   response = requests.get(link)
   article_soup = bs4.BeautifulSoup(response.text, features='lxml')
   title = article_soup.select_one('h1').text.strip()
   time = article_soup.select_one('time')['title']

   for word in KEYWORDS:
      if word in article_soup.text:
          print (f'<{time}> – <{title}> – <{link}>')
