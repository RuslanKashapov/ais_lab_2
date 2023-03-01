from typing import Optional, Iterable
from sqlalchemy.orm import Session
from application.models.dao import *
import functools
import traceback


def dbexception(db_func):
    @functools.wraps(db_func)
    def decorated_func(db: Session, *args, **kwargs) -> bool:
        try:
            db_func(db, *args, **kwargs)    # вызов основной ("оборачиваемой") функции
            db.commit()     # подтверждение изменений в БД
            return True
        except Exception as ex:
            # выводим исключение и "откатываем" изменения
            print(f'Exception in {db_func.__name__}: {traceback.format_exc()}')
            db.rollback()
            return False
    return decorated_func


def get_transformator_by_id(db: Session, transformator_id: int) -> Optional[Transformator]:
    result = db.query(Transformator).filter(Transformator.id == transformator_id).first()
    return result





def get_trans_by_city_name(db: Session, city_name: str) -> Iterable[Transformator]:
    result = db.query(Transformator).join(City).filter(City.name == city_name).all()
    return result


def create_transformator(db: Session, hydrogen: int, oxygen: int, nitrogen: int, methane: int, co: int, co_2: int,
                         ethylene: int, ethane: int, acethylene: int, dbds: int, power_factor: float, interfacial_v: int,
                         dielectric_rigidity: int, water_content: int, city_id: int, types: int,
                         health_index: float) -> bool:
    transformator = Transformator(
        hydrogen=hydrogen,
        oxygen=oxygen,
        nitrogen=nitrogen,
        methane=methane,
        co=co,
        co_2=co_2,
        ethylene=ethylene,
        ethane=ethane,
        acethylene=acethylene,
        dbds=dbds,
        power_factor=power_factor,
        interfacial_v=interfacial_v,
        dielectric_rigidity=dielectric_rigidity,
        water_content=water_content,
        city=city_id,
        types=types,
        health_index=health_index
        )
    return add_transformator(db, transformator)





def add_transformator(db: Session, transformator: Transformator) -> bool:
    try:
        db.add(transformator)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


def update_hydrogen_by_transformator_id(db: Session, transformator_id: int, hydrogen: int) -> bool:
    transformator = get_transformator_by_id(db, transformator_id)
    transformator.hydrogen = hydrogen
    return add_transformator(db, transformator)



def get_transformator_by_city_id(db: Session, city_id: int) -> Optional[Transformator]:
    result = db.query(Transformator).filter(Transformator.city == city_id).order_by(Transformator.updated_on.asc()).first()
    return result




@dbexception
def delete_transformator_by_id(db: Session, transformator_id: int) -> bool:
    trans = get_transformator_by_id(db, transformator_id)
    db.delete(trans)





@dbexception
def add_city(db: Session, city_name: str) -> bool:
    city = City(name=city_name)
    db.add(city)
    return True



@dbexception
def add_type(db: Session, transformator_type: int) -> None:
    trans_type = Types(name=transformator_type)
    db.add(trans_type)
