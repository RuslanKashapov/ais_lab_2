from sqlalchemy import Column, ForeignKey, Boolean, Integer, Numeric, String, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime


#Объявление декларативного (описательного) метода представления БД
Base = declarative_base()


class Transformator(Base):
    """ Таблица с наименованиями населённых пунктов """
    __tablename__ = "transformator"

    id = Column(Integer, primary_key=True)
    hydrogen = Column('hydrogen', Integer, nullable=False)
    oxygen = Column('oxygen', Integer, nullable=False)
    nitrogen = Column('nitrogen', Integer, nullable=False)
    methane = Column('methane', Integer, nullable=False)
    co = Column('co', Integer, nullable=False)
    co_2 = Column('co2', Integer, nullable=False)
    ethylene = Column('ethylene', Integer, nullable=False)
    ethane = Column('ethane', Integer, nullable=False)
    acethylene = Column('acethylene', Integer, nullable=False)
    dbds = Column('dbds', Integer, nullable=False)
    power_factor = Column('power_factor', Float, nullable=False)
    interfacial_v = Column('interfacial_v', Integer, nullable=False)
    dielectric_rigidity = Column('dielectric_rigidity', Integer, nullable=False)
    water_content = Column('water_content', Integer, nullable=False)
    health_index = Column('health_index', Float)

    city = Column(Integer, ForeignKey('city.id'), nullable=False)
    city_name = relationship('City')

    types = Column(Integer, ForeignKey('types.id'), nullable=False)
    transformator_type = relationship('Types')

    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    @hybrid_property
    def _health_index(self):
        """ Декоратор @hybrid_property позволяет добавить какую-нибудь бизнес-логику или проверку
            при установке данному полю какого-либо значения. Подробнее см.:
            https://docs.sqlalchemy.org/en/14/orm/extensions/hybrid.html#sqlalchemy.ext.hybrid.hybrid_property """
        return self.health_index

    @_health_index.setter
    def _health_index(self):
        """ При установке значения полю temperature_c будет автоматически рассчитано значение temperature_f """
        self.health_index = 100.0

    def update_health_index(self):
        pass

    def __repr__(self):
        """ Переопределяем строковое представление объекта (см. python magic methods)"""
        return f'{self.__dict__}'



class City(Base):
    """ Таблица с наименованиями населённых пунктов """
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        """ Переопределяем строковое представление объекта (см. python magic methods)"""
        return f'{self.__dict__}'


class Types(Base):
    """ Таблица с наименованиями населённых пунктов """
    __tablename__ = "types"

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False, unique=True)

    def __repr__(self):
        """ Переопределяем строковое представление объекта (см. python magic methods)"""
        return f'{self.__dict__}'






