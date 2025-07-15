from abc import abstractmethod
from typing import Optional, Protocol
from uuid import UUID
from src.domain.entities.user_dm import UserDM


class UserReader(Protocol):
    @abstractmethod
    async def get(self, user_id: str) -> Optional[UserDM]: ...


class UserSaver(Protocol):
    @abstractmethod
    async def add(self, user: UserDM) -> None: ...


class UUIDGenerator(Protocol):
    def __call__(self) -> UUID:
        ...


class DBSession(Protocol):
    @abstractmethod
    async def commit(self) -> None:
        ...

    @abstractmethod
    async def flush(self) -> None:
        ...
