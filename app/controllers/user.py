from app.models import User
from app.repositories import TaskRepository, UserRepository
from core.controller import BaseController


class UserController(BaseController[User]):
    def __init__(
        self, user_repository: UserRepository, task_repository: TaskRepository
    ):
        super().__init__(model=User, repository=user_repository)
        self.user_repository = user_repository
        self.task_repository = task_repository

    async def get_by_username(self, username: str) -> User:
        return await self.user_repository.get_by_username(username)

    async def get_by_email(self, email: str) -> User:
        return await self.user_repository.get_by_email(email)
