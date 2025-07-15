from src.domain.value_objects.email import Email
from src.application.interfaces.interfaces import DBSession, UserSaver, UserReader, UUIDGenerator
from src.domain.entities.user_dm import UserDM
from src.application.dtos.user_dto import CreateUserDTO


class GetUserInteractor:
    def __init__(
            self,
            user_gateway: UserReader,
    ) -> None:
        self._user_gateway = user_gateway

    async def __call__(self, uuid: str) -> UserDM | None:
        return await self._user_gateway.get(uuid)


class CreateUserInteractor:
    def __init__(
            self,
            db_session: DBSession,
            user_gateway: UserSaver,
            uuid_generator: UUIDGenerator,
    ) -> None:
        self._db_session = db_session
        self._user_gateway = user_gateway
        self._uuid_generator = uuid_generator

    async def __call__(self, dto: CreateUserDTO) -> str:
        uuid = str(self._uuid_generator())
        email = Email(str(dto.email))
        book = UserDM(
            uuid=uuid,
            name=dto.name,
            email=email
        )

        await self._user_gateway.add(book)
        await self._db_session.commit()
        return uuid
