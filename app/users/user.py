from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(slots=True)
class User(ABC):
    id: int
    fullname: str
    phone: str

    def __post_init__(self) -> None:
        if not isinstance(self.id, int):
            raise TypeError("User id must be int")
        if not isinstance(self.fullname, str):
            raise TypeError("User fullname must be str")
        if not self.fullname.strip():
            raise ValueError("User fullname cannot be empty")
        if not isinstance(self.phone, str):
            raise TypeError("User phone must be str")
        if not self.phone.strip():
            raise ValueError("User phone cannot be empty")

    @classmethod
    @abstractmethod
    def user_type(cls) -> str:
        """Return the user type."""
