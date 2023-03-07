from fastapi import APIRouter, HTTPException, status, Request, Response
from starlette.responses import RedirectResponse
from application.models.dto import *
from application.services.trans_service import TransformatorService

"""

    Данный модуль отвечает за маршрутизацию доступных API URI (endpoints) сервера

"""


router = APIRouter( tags=['Transformator Forecast API'])       # подключаем данный роутер к корневому адресу /api
service = TransformatorService()              # подключаем слой с дополнительной бизнес-логикой

@router.get('/')
async def root():
    """ Переадресация на страницу Swagger """
    return RedirectResponse(url='/docs', status_code=307)


@router.get('/transformator/{city_name}', response_model=List[TransformatorDTO])
async def get_all_transforecast_by_city_name(city_name: str):
    """ Получение всех записей о трансформаторах в определенном городе """
    return service.get_all_transformator_in_city(city_name)


@router.get('/transformator', response_model=TransformatorDTO)
async def get_transformator_by_number(trans_number: int):
    """ Получение записи о трансформаторе по номеру """
    response = service.get_transformator_by_number(trans_number)
    if response is None:
        return Response(status_code=204)
    return response


@router.post('/transformator', status_code=201)
async def post_transformator(trans: TransformatorDTO):
    """ Добавить новую запись о трансформаторе """
    if service.add_trans_info(trans):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new Transformator data",
        )
#ахах

@router.put('/transformator', status_code=202)
async def put_transformator_by_hydrogen(input: TransformatorUpdateInfo):
    """ Обновить гидроген """
    trans = TransformatorDTO
    trans.number = input.number
    trans.hydrogen = input.hydrogen
    if service.update_trans_hydrogen(trans):
        return Response(status_code=202)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't update Transformator data",
        )


@router.delete('/transformator/<int:number>}', status_code=200)
async def del_transformator(number: int):
    """ Удаление всех записей о трансформаторе в населённом пункте """
    if service.delete_trans_by_number(number):
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
