# Обзор сторонних библиотек Python


import matplotlib.pyplot as plt

# Пример данных
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Построение графика
plt.plot(x, y, marker='o')
plt.title('Quadratic Function')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid()
plt.show()


# Возможности
# Создание статических, анимационных и интерактивных графиков.
# Поддержка множества различных типов графиков (линейные, столбчатые, круговые и др.).
# Настройка отображения графиков: цвета, метки, заголовки и др.



import requests

# 1. Отправка GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(f'Status Code: {response.status_code}')
print(f'Response JSON: {response.json()}')

# 2. Отправка POST-запроса
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
post_response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(f'Post Response: {post_response.json()}')

# 3. Обработка ошибок
try:
    bad_response = requests.get('https://jsonplaceholder.typicode.com/badendpoint')
    bad_response.raise_for_status()  # Выдаст ошибку для статусов 4xx/5xx
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")  # Выводим ошибку
    

# Возможности
# Легкое отправление HTTP-запросов.
# Поддержка различных HTTP-методов (GET, POST и др.).
# Работа с параметрами запроса и обработка ответов.
# Поддержка работы с аутентификацией и сессиями