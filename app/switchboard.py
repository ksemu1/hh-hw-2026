from __future__ import annotations
from dataclasses import dataclass
from app.users import User
from app.users.local_user import LocalUser
from app.users.foreign_user import ForeignUser

LOCAL_PHONE_PREFIX = "+7"


@dataclass(slots=True)
class ActiveCall:
    caller: User
    receiver: User

    @property
    def is_cross_border(self) -> bool:
        return type(self.caller) is not type(self.receiver)


class Switchboard:
    def __init__(self) -> None:
        self._active_calls: list[ActiveCall] = []
        self._cross_border_count: int = 0

    def register_call(self, raw_call: str) -> ActiveCall:
        parts = [part.strip() for part in raw_call.split(',')]
        (caller_id, caller_name, caller_phone, receiver_id, receiver_name, receiver_phone) = parts
       
        caller = self._create_user(caller_id, caller_name, caller_phone)
        receiver = self._create_user(receiver_id, receiver_name, receiver_phone)
       
        active_call = ActiveCall(caller, receiver)
        self._active_calls.append(active_call)

        if active_call.is_cross_border:
            self._cross_border_count += 1
        
        return active_call

    def _create_user(self, user_id: str, name: str, phone: str) -> User:
        if phone.startswith(LOCAL_PHONE_PREFIX):
            return LocalUser(user_id, name, phone)
        return ForeignUser(user_id, name, phone)

    def get_active_calls_count(self) -> int:
        return len(self._active_calls)

    def get_cross_border_calls_count(self) -> int:
        return self._cross_border_count
