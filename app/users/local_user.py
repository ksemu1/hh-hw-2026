from dataclasses import dataclass

from app.users.user import User


@dataclass(slots=True)
class LocalUser(User):
    @classmethod
    def user_type(cls) -> str:
        return "local"
