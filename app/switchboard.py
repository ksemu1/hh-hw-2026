from __future__ import annotations

from dataclasses import dataclass

from app.users import User


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

    def register_call(self, raw_call: str) -> ActiveCall:
        '''
        Метод должен принимать только 1 строку и возвращать класс ActiveCall.
        На входе строка должна быть вида "caller_id,caller_name,caller_phone,reciever_id,reciever_name,reciever_phone"

        Например: "1001,Иван Петров,+71234567890,1085,Адам Яковлев,+71255556666"
        '''

    def get_active_calls_count(self) -> int:
        '''
        Задание: ответ должен быть за константное время - О(1)
        '''

    def get_cross_border_calls_count(self) -> int:
        '''
        *** Задание: ответ должен быть за константное время - О(1)
        '''
