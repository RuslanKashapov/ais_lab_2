from application.config import SessionLocal
from application.services.repository_service import *
import random


""" Данный скрипт заполняет БД тестовыми данными """


CITY = ['UFA', 'MOSCOW', 'SAINT-PETERSBURG', 'NORILSK', 'KHERSON', 'CRIMEA']

TRANS_TYPE = [1, 2, 3, 4, 5, 6]


def populate_city(db: Session) -> None:
    for city_name in CITY:
        add_city(db, city_name)


def populate_weather_type(db: Session) -> None:
    for weather_type_name in TRANS_TYPE:
        add_type(db, weather_type_name)


if __name__ == "__main__":
    with SessionLocal() as session:
        populate_city(session)
        populate_weather_type(session)
        create_transformator(session,
                             hydrogen=1,
                             oxygen=1,
                             nitrogen=1,
                             methane=1,
                             co=1,
                             co_2=1,
                             ethylene=1,
                             ethane=1,
                             acethylene=1,
                             dbds=1,
                             power_factor=1.0,
                             interfacial_v=1,
                             dielectric_rigidity=1,
                             water_content=1,
                             city_id=1,
                             types=1,
                             health_index=1.0
                             )
