from fastapi import APIRouter, HTTPException, status, Request, Response
from starlette.responses import RedirectResponse
from application.models.dto import *
from application.services.trans_service import TransformatorService
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


"""

    Данный модуль отвечает за маршрутизацию доступных API URI (endpoints) сервера

"""


router = APIRouter( tags=['Transformator Forecast API'])       # подключаем данный роутер к корневому адресу /api
service = TransformatorService()              # подключаем слой с дополнительной бизнес-логикой


class Data(BaseModel):
    id: int
    hydrogen: int

@router.get('/')
async def root():
    """ Переадресация на страницу Swagger """
    return RedirectResponse(url='/docs', status_code=307)


@router.get('/transforecast/{city_name}', response_model=List[TransformatorDTO])
async def get_all_transforecast_by_city_name(city_name: str):
    """ Получение всех записей о погоде в населённом пункте """
    return service.get_all_transformator_in_city(city_name)


@router.get('/transforecast/{city_id}', response_model=TransformatorDTO)
async def get_transforecast_by_city_id(city_id: int):
    """ Получение записи о погоде в населенном пункте по идентификатору населенного пункта (необходим параметр ?city_id=) """
    response = service.get_transformator_in_city(city_id)
    if response is None:
        return Response(status_code=204)
    return response


@router.post('/transforecast', status_code=201)
async def post_transforecast(trans: TransformatorDTO):
    """ Добавить новую запись о погоде """
    if service.add_trans_info(trans):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new Transformator data",
        )


@router.put('/transforecast', status_code=202)
async def put_transforecast(input_data: Data):
    trans = TransformatorDTO
    trans.id = input_data.id
    trans.hydrogen = input_data.hydrogen
    """ Обновить гидроген """
    if service.update_trans_info(trans):
        print(trans.id, trans.hydrogen)
        return Response(status_code=202)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't update Transformator data",
        )



@router.delete('/transforecast/{id}', status_code=200)
async def del_transforecast(id: int):
    """ Удаление всех записей о погоде в населённом пункте """
    if service.delete_trans_by_id(id):
        return Response(status_code=200)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't delete Transformator data",
        )


@router.post('/city', status_code=201)
async def create_city(city: CityDTO) -> Response:
    """ Добавить новый населённый пункт """
    if service.add_city(city):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new City data",
        )
