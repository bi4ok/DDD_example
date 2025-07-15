from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, HTTPException, Path
from http import HTTPStatus
from src.api.schemas.schemas import UserSchema
from src.application.interactors.user import CreateUserInteractor, GetUserInteractor
from src.application.dtos.user_dto import CreateUserDTO
from typing import Annotated
from uuid import UUID

router = APIRouter(route_class=DishkaRoute)


@router.post("/", status_code=201)
async def create_user(
        data: UserSchema,
        interactor: FromDishka[CreateUserInteractor]
):
    dto = CreateUserDTO(
        name=data.name,
        email=data.email
    )
    user_id = await interactor(dto)
    return {"id": user_id}


@router.get("/{user_id}", status_code=201)
async def get_user(
        user_id: Annotated[UUID, Path(description="User ID", title="User ID")],
        interactor: FromDishka[GetUserInteractor]
):
    user_dm = await interactor(uuid=str(user_id))
    if not user_dm:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return UserSchema(
        name=user_dm.name,
        email=user_dm.email
    )
