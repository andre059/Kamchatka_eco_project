import requests
from bs4 import BeautifulSoup


def get_page_content(url):
    """Получение HTML-кода страницы"""

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
        return None


def parse_cluster_info(url):
    """Сбор информации из HTML-кода страницы о парке Налычево"""

    description = ''
    content = get_page_content(url)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find('h1').text.strip()

        for span_element in soup.find_all('span')[1:16]:
            if span_element.text not in description:
                description += span_element.text
        description = description.split(". ")
        description1 = ".\n".join(description)

        return {'title': title, 'description': description1}
    else:
        return None


# def parse_cluster_info_1(url):
#     """Сбор информации о маршрутах парка Налычево"""
#
#     content = get_page_content(url)
#     if content:
#         soup = BeautifulSoup(content, 'html.parser')
#         name = soup.find('strong').text.strip()
#
#         for span_element in soup.find_all('span')[1:16]:
#             if span_element.text not in description:
#                 description += span_element.text
#         description = description.split(". ")
#         description1 = ".\n".join(description)
#
#         return {'title': title, 'description': description1}
#     else:
#         return None