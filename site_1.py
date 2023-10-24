from bs4 import BeautifulSoup
import requests

# Определите URL-адрес страницы
url = 'https://www.nemera.com'

# Отправьте запрос к указанному URL и получите содержимое страницы
response = requests.get(url)
content = response.content

# Создайте объект BeautifulSoup для анализа содержимого страницы
soup = BeautifulSoup(content, 'html.parser')

# Найдите все ссылки на CSS файлы
css_links = soup.find_all('link', rel='stylesheet')

# Запросите содержимое каждого CSS файла
for css_link in css_links:
    css_url = css_link.get('href')
    if css_url.startswith('http'):  # Обработка абсолютных URL
        css_response = requests.get(css_url)
    else:  # Обработка относительных URL
        css_response = requests.get(url + css_url)

    css_content = css_response.content

    # Действия с содержимым CSS файла
    # Например, можно сохранить его в файл или выполнить другую обработку
    # В данном примере просто выводим содержимое CSS файла
    print(css_content)
