import pytest

from app.switchboard import Switchboard
from app.users import ForeignUser, LocalUser


def test_register_call_creates_local_and_foreign_users() -> None:
    switchboard = Switchboard()

    active_call = switchboard.register_call(
        "1,Ivan Ivanov,+79990000000,2,John Smith,+15551234567"
    )

    assert isinstance(active_call.caller, LocalUser)
    assert isinstance(active_call.receiver, ForeignUser)
    assert active_call.caller.id == 1
    assert active_call.receiver.id == 2


def test_register_call_counts_active_calls() -> None:
    switchboard = Switchboard()

    switchboard.register_call(
        "1,Ivan Ivanov,+79990000000,2,Petr Petrov,+78880000000"
    )
    switchboard.register_call(
        "3,John Smith,+15551234567,4,Jane Doe,+33123456789"
    )

    assert switchboard.get_active_calls_count() == 2


def test_register_call_counts_calls_between_local_and_foreign_users() -> None:
    switchboard = Switchboard()

    switchboard.register_call(
        "1,Ivan Ivanov,+79990000000,2,John Smith,+15551234567"
    )
    switchboard.register_call(
        "3,Petr Petrov,+78880000000,4,Maria Petrova,+79991112233"
    )
    switchboard.register_call(
        "5,Jane Doe,+33123456789,6,Alex Doe,+442012345678"
    )

    assert switchboard.get_active_calls_count() == 3
    assert switchboard.get_cross_border_calls_count() == 1


def test_multiple_calls_mixed_types() -> None:
    switchboard = Switchboard()
    switchboard.register_call("1, Иван Иванов, +79990000000, 2, Петр Петров, +78880000000")
    switchboard.register_call("3, John Smith, +15551234567, 4, Jane Doe, +33123456789")
    switchboard.register_call("5, Иван Иванов, +79990000000, 6, John Smith, +15551234567")
    switchboard.register_call("7, John Smith, +15551234567, 8, Иван Иванов, +79990000000")
    
    assert switchboard.get_active_calls_count() == 4
    assert switchboard.get_cross_border_calls_count() == 2


def test_register_call_returns_active_call() -> None:
    switchboard = Switchboard()
    
    active_call = switchboard.register_call("1, Иван Иванов, +79990000000, 2, John Smith, +15551234567")
    
    assert isinstance(active_call, ActiveCall)
    assert active_call.caller.phone == "+79990000000"
    assert active_call.receiver.phone == "+15551234567"


def test_cross_border_property() -> None:
    from app.users.local_user import LocalUser
    from app.users.foreign_user import ForeignUser

    call1 = ActiveCall(LocalUser("1", "Иван", "+79001234567"),LocalUser("2", "Петр", "+79111234567"))
    assert call1.is_cross_border is False

    call2 = ActiveCall(LocalUser("1", "Иван", "+79001234567"),ForeignUser("2", "John", "447911123456"))
    assert call2.is_cross_border is True


def test_ids_as_strings() -> None:
    switchboard = Switchboard()
    active_call = switchboard.register_call("1001, Иван Иванов, +79990000000, 2002, John Smith, +15551234567")
    
    assert isinstance(active_call.caller.id, str)
    assert active_call.caller.id == "1001"
    assert isinstance(active_call.receiver.id, str)
    assert active_call.receiver.id == "2002"
