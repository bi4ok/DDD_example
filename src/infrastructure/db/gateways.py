from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from src.application.interfaces.interfaces import UserReader, UserSaver
from src.domain.entities.user_dm import UserDM


class UserGateWay(
    UserReader,
    UserSaver,
):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, uuid: str) -> UserDM | None:
        query = text("SELECT * FROM users WHERE uuid = :uuid")
        result = await self._session.execute(
            statement=query,
            params={"uuid": uuid},
        )
        row = result.fetchone()
        if not row:
            return None
        return UserDM(
            uuid=row.uuid,
            name=row.name,
            email=row.email
        )

    async def add(self, user: UserDM) -> None:
        query = text("INSERT INTO users (uuid, name, email) VALUES (:uuid, :name, :email)")
        await self._session.execute(
            statement=query,
            params={
                "uuid": user.uuid,
                "name": user.name,
                "email": user.email.address,
            },
        )