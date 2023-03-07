from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime
#ахах

class TransformatorDTO(BaseModel):
    """ DTO для добавления, обновления и получения информации о погоде.
        Если данные, передаваемые клиенту сильно отличаются от данных,
        которые принимает REST API сервера, необходимо разделять DTO
        для запросов и ответов, например, WeatherRequestDTO, WeatherResponseDTO """
    # id: int
    number: int
    hydrogen: int
    oxygen: int
    nitrogen: int
    methane: int
    co: int
    co_2: int
    ethylene: int
    ethane: int
    acethylene: int
    dbds: int
    power_factor: float
    interfacial_v: int
    dielectric_rigidity: int
    water_content: int
    city_id: Optional[int]
    types: int
    health_index:  Optional[float]
    # updated_on: Optional[datetime]


class TransformatorUpdateInfo(BaseModel):
    number: int
    hydrogen: int