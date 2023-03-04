from typing import Optional, List
from application.config import SessionLocal
from application.models.dao import Transformator
from application.models.dto import TransformatorDTO, CityDTO
import application.services.repository_service as repository_service


"""
"""


class TransformatorService:

    def get_transformator_in_city(self, city_id: int) -> Optional[TransformatorDTO]:
        result = None
        with SessionLocal() as session:     # конструкция with позволяет автоматически завершить сессию после выхода из блока
            result = repository_service.get_transformator_by_city_id(session, city_id)
        if result is not None:
            return self.map_trans_data_to_dto(result)
        return result

    def get_all_transformator_in_city(self, city_name: str) -> List[TransformatorDTO]:
        trans_data: List[TransformatorDTO] = []
        with SessionLocal() as session:
            result = repository_service.get_trans_by_city_name(session, city_name.upper())
            for w in result:
                trans_data.append(self.map_trans_data_to_dto(w))
        return trans_data

    def add_trans_info(self, transformator: TransformatorDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.create_transformator(session,
                                                   hydrogen=transformator.hydrogen,
                                                   oxygen=transformator.oxygen,
                                                   nitrogen=transformator.nitrogen,
                                                   methane=transformator.methane,
                                                   co=transformator.co,
                                                   co_2=transformator.co_2,
                                                   ethylene=transformator.ethylene,
                                                   ethane=transformator.ethane,
                                                   acethylene=transformator.acethylene,
                                                   dbds=transformator.dbds,
                                                   power_factor=transformator.power_factor,
                                                   interfacial_v=transformator.interfacial_v,
                                                   dielectric_rigidity=transformator.dielectric_rigidity,
                                                   water_content=transformator.water_content,
                                                   city_id=transformator.city_id,
                                                   types=transformator.types,
                                                   health_index=transformator.health_index)

    def update_trans_info(self, transformator: TransformatorDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.update_hydrogen_by_transformator_id(session,  transformator_id=transformator.id,
                                                                          hydrogen=transformator.hydrogen)

    def delete_trans_by_id(self, id: int) -> bool:
        with SessionLocal() as session:
            return repository_service.delete_transformator_by_id(session, id)

    def add_city(self, city: CityDTO) -> bool:
        if city.name != "":
            with SessionLocal() as session:
                return repository_service.add_city(session, city_name=city.name.upper())
        return False

    def map_trans_data_to_dto(self, trans_dao: Transformator):
        """ Метод для конвертирования (маппинга) Weather DAO в WeatherDTO """
        return TransformatorDTO(
                                id=trans_dao.id,
                                hydrogen = trans_dao.hydrogen,
                                oxygen = trans_dao.oxygen,
                                nitrogen = trans_dao.nitrogen,
                                methane = trans_dao.methane,
                                co = trans_dao.co,
                                co_2 = trans_dao.co_2,
                                ethylene = trans_dao.ethylene,
                                ethane =  trans_dao.ethane,
                                acethylene =  trans_dao.acethylene,
                                dbds =  trans_dao.dbds,
                                power_factor = trans_dao.power_factor,
                                interfacial_v =  trans_dao.interfacial_v,
                                dielectric_rigidity =  trans_dao.dielectric_rigidity,
                                water_content =  trans_dao.water_content,
                                city_id =  trans_dao.city,
                                types = trans_dao.types,
                                health_index = trans_dao.health_index,
                                updated_on=trans_dao.updated_on)
