# hh-hw-2026

## Задание

Доработать класс Switchboard таким образом, чтобы:
1. метод register_call принимал строку с информацией об активном звонке, разбивал её на части и создавал класс ActiveCall, перед этим создав классы LocalUser или ForeignUser для каждого участника звонка
2. метод get_active_calls_count возвращал количество активных звонков
3. метод get_cross_border_calls_count возвращал количетство активных звонков между LocalUser и ForeignUser

### Условия выполнения задания:
1. Нельзя менять названия изначальных классов и методов, но можно создавать свои
2. Все ваши изменения должны быть только в файлах switchboard.py и test_switchboard.py
3. hard deadline - 2 недели от даты лекции, soft deadline - 3 недели. После 3 недель ДЗ не принимается.


## Описание данных

### raw_call

raw_call метода register_call представляет собой строку "caller_id,caller_name,caller_phone,reciever_id,reciever_name,reciever_phone"

* caller_id - id позвонившего пользователя
* caller_name - имя позвонившего пользователя
* caller_phone - номер телефона позвонившего пользователя
* reciever_id - id ответившего пользователя
* reciever_name - имя ответившего пользователя
* reciever_phone - номер телефона ответившего пользователя

### виды юзеров

Выбирайте LocalUser, если номер начинается с +7, ForeignUser для других номеров.
