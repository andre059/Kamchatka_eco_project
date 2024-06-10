import requests
from bs4 import BeautifulSoup


def parse_trails():
    url = 'https://www.vulcanikamchatki.ru/'  # Замените  на  URL  сайта
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #  Найдите  элементы  HTML,  которые  содержат  данные  о  маршрутах.
    #  Например,  используйте  soup.find_all('div', class_='trail-item')
    #  или  soup.select('div.trail-item')

    trails = []

    for trail_item in soup.find_all('div', class_='block-route'):
        title = trail_item.find('block-route__title').text.strip()
        description = trail_item.find('block-route__text').text.strip()
        #  Найдите  другие  данные:  загруженность,  фото,  координаты,  etc.
        #  Например,  используйте  trail_item.find_all('img')  для  фото,
        #  trail_item.select('span.block-route__descr')  для  описания

        print(f'Название: {title}')
        print(f'Описание: {description}')

        trails.append({
            'title': title,
            'description': description,
            #  Добавьте  другие  данные
        })


# if __name__ == '__main__':
#     parse_trails()
