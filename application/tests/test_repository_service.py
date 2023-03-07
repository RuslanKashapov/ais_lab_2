import unittest
import random as rnd
from application.config import SessionLocal
from application.services.repository_service import *


"""
   Данный модуль реализует "тестовые случаи/ситуации" для модуля repository_service.
   Для создания "тестового случая" необходимо создать отдельный класс, который наследует 
   базовый класс TestCase. Класс TestCase предоставляется встроенным 
   в Python модулем для тестирования - unittest.
   
   Более детально см.: https://pythonworld.ru/moduli/modul-unittest.html
"""


CITY = []

TYPE = []


class TestWeatherRepositoryService(unittest.TestCase):
    """ Все тестовые методы в классе TestCase (по соглашению)
        должны начинаться с префикса test_* """

    def setUp(self):
        """ Наследуемый метод setUp определяет инструкции,
            которые должны быть выполнены ПЕРЕД тестированием """
        self.session = SessionLocal()       # создаем сессию подключения к БД
        try:
            for city_name in CITY:
                add_city(self.session, city_name)
            for type_name in TYPE:
                add_type(self.session, type_name)
        except:
            print('Test data already created')

    def test_create_weather(self):
        """ Тест функции создания записи Weather """
        result = create_transformator(self.session,
                                      number=rnd.randint(1, 1000),
                                      hydrogen=rnd.randint(1, 100),
                                      oxygen=rnd.randint(1, 100),
                                      nitrogen=rnd.randint(1, 100),
                                      methane=rnd.randint(1, 100),
                                      co=rnd.randint(1, 100),
                                      co_2=rnd.randint(1, 100),
                                      ethylene=rnd.randint(1, 100),
                                      ethane=rnd.randint(1, 100),
                                      acethylene=rnd.randint(1, 100),
                                      dbds=rnd.randint(1, 100),
                                      power_factor=1.0,
                                      interfacial_v=rnd.randint(1, 100),
                                      dielectric_rigidity=rnd.randint(1, 100),
                                      water_content=rnd.randint(1, 100),
                                      city_id=rnd.randint(1, 6),
                                      types=rnd.randint(1, 6),
                                      health_index=1.0)
        self.assertTrue(result)     # валидируем результат (result == True)

    def test_get_transformator(self):
        """ Тест функции поиска записи Weather по наименованию населённого пункта """
        trans_in_ufa_rows = get_trans_by_city_name(self.session, city_name='UFA')
        for row in trans_in_ufa_rows:
            self.assertIsNotNone(row)           # запись должна существовать
            self.assertTrue(row.city == 1)   # идентификатор city_id == 1 (т.е. город UFA в таблице city)
            self.assertTrue(row.city_name.name == 'UFA')  # проверка связи (relation) по FK

    '''def test_delete_weather(self):
        """ Тест функции удаления записи Weather по наименованию населённого пункта """
        delete_transformator_by_id(self.session, transformator_id=2)
        result = get_transformator_by_id(self.session, transformator_id=2)        # ищем запись по идентификатору города UFA
        self.assertIsNone(result)       # запись не должна существовать
    '''

    # ахах
    def test_update_hydrogen_by_transformator_id(self):
        update_hydrogen_by_transformator_number(self.session, transformator_number=2, hydrogen=2)
        self.assertTrue(get_transformator_by_number(self.session, 2).hydrogen == 2)

    def tearDown(self):
        """ Наследуемый метод tearDown определяет инструкции,
            которые должны быть выполнены ПОСЛЕ тестирования """
        self.session.close()        # закрываем соединение с БД


if __name__ == '__main__':
    unittest.main()
