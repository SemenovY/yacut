"""Абстрагируем хранение и взаимодействие с данными от бизнес логики."""
import abc
from typing import List

from models import User


class AbstractRepository(abc.ABC):
    """Базовый репозиторий, от которого наследуются все другие репозитории."""

    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> User:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add(self, user: User):
        self.session.add(user)

    def get(self, id: str) -> User:
        return self.session.query(User).get(id)

    def list(self) -> List[User]:
        return self.session.query(User).all()
