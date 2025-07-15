from typing import AsyncIterable
from uuid import uuid4

from dishka import Provider, Scope, provide, AnyOf, from_context
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.infrastructure.db.database import new_session_maker
from src.config import Config
from src.infrastructure.db.gateways import UserGateWay
from src.application.interfaces.interfaces import UserReader, UserSaver, DBSession, UUIDGenerator
from src.application.interactors.user import GetUserInteractor, CreateUserInteractor


class AppProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_uuid_generator(self) -> UUIDGenerator:
        return uuid4

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Config) -> async_sessionmaker[AsyncSession]:
        return new_session_maker(config.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, session_maker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AnyOf[
        AsyncSession,
        DBSession,
    ]]:
        async with session_maker() as session:
            yield session

    user_gateway = provide(
        UserGateWay,
        scope=Scope.REQUEST,
        provides=AnyOf[UserReader, UserSaver]
    )

    get_user_interactor = provide(GetUserInteractor, scope=Scope.REQUEST)
    create_new_user_interactor = provide(CreateUserInteractor, scope=Scope.REQUEST)
