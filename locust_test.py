import json
import time
import random
import json
from locust import HttpUser, task, tag, between


# Статичные данные для тестирования
CITY_NAMES = ['ufa', 'moscow', 'saint-petersburg', 'paris']


class RESTServerUser(HttpUser):
    """ Класс, эмулирующий пользователя / клиента сервера """
    wait_time = between(1.0, 5.0)       # время ожидания пользователя перед выполнением новой task

    # Адрес, к которому клиенты (предположительно) обращаются в первую очередь (это может быть индексная страница, страница авторизации и т.п.)
    def on_start(self):
        self.client.get("/docs")    # базовый класс HttpUser имеет встроенный HTTP-клиент для выполнения запросов (self.client)

    @tag("get_all_task")
    @task(3)
    def get_all_task(self):
        """ Тест GET-запроса (получение записей о трансформаторах в определенном городе) """
        city_id = random.randint(0, 3)      # генерируем случайный id в диапазоне [0, 3]
        city_name = CITY_NAMES[city_id]     # получаем случайное значение населенного пункта из списка CITY_NAMES
        with self.client.get(f'/transformator/{city_name}',
                             catch_response=True,
                             name='/transformator/{city_name}') as response:
            # Если получаем код HTTP-код 200, то оцениваем запрос как "успешный"
            if response.status_code == 200:
                response.success()
            # Иначе обозначаем как "отказ"
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("get_one_task")
    @task(10)
    def get_one_task(self):
        """ Тест GET-запроса (получение одной записи) """
        trans_number = 22
        with self.client.get(f'/transformator?trans_number={trans_number}',
                             catch_response=True,
                             name='/transformator?trans_number={trans_number}>') as response:
            # Если получаем код HTTP-код 200 или 204, то оцениваем запрос как "успешный"
            if response.status_code == 200 or response.status_code == 204:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("post_task")
    @task(1)
    def post_task(self):
        """ Тест POST-запроса (создание записи о трансформаторе) """
        # Генерируем случайные данные в опредленном диапазоне
        test_data = {
                     'number': random.randint(1, 1000),
                     'hydrogen': random.randint(1, 100),
                     'oxygen': random.randint(1, 100),
                     'nitrogen': random.randint(1, 100),
                     'methane': random.randint(1, 100),
                     'co': random.randint(1, 100),
                     'co_2': random.randint(1, 100),
                     'ethylene': random.randint(1, 100),
                     'ethane': random.randint(1, 100),
                     'acethylene': random.randint(1, 100),
                     'dbds': random.randint(1, 100),
                     'power_factor': random.uniform(1.0, 100.0),
                     'interfacial_v': random.randint(1, 100),
                     'dielectric_rigidity': random.randint(1, 100),
                     'water_content': random.randint(1, 100),
                     'city_id': random.randint(1, 6),
                     'types': random.randint(1, 6),
                     'health_index': random.uniform(1.0, 100.0)
                     }
        post_data = json.dumps(test_data)       # сериализуем тестовые данные в json-строку
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/api/weatherforecast
        with self.client.post('/transformator',
                              catch_response=True,
                              name='/transformator', data=post_data,
                              headers={'content-type': 'application/json'}) as response:
            # проверяем, корректность возвращаемого HTTP-кода
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    # ахах
    @tag("put_task")
    @task(3)
    def put_task(self):
        """ Тест PUT-запроса (обновление записи о погоде) """
        test_data = {'number': 1, 'hydrogen': random.randint(1, 100)}
        put_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/weatherforecast/{city_name}
        with self.client.put('/transformator',
                             catch_response=True,
                             name='/transformator',
                             data=put_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 202:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

