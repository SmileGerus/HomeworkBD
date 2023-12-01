import psycopg2


def change_data():
    '''
    Словарь с функциями, который вызывается из основного модуля main
    :return: dict
    '''
    commands = {
        'first_name': change_user_first_name,
        'second_name': change_user_second_name,
        'email': change_user_email,
        'phone_number': change_phones_phone_number
    }
    return commands


def change_user_first_name() -> str:
    """
    Функция вызывается из основного модуля main
    Запрашивает новое имя и id пользователя
    Возвращает новое имя пользователя
    :return:
    """
    new_first_name = input('Введите новое имя: ')
    id_user = int(input('Введите id пользователя: '))
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            UPDATE users
            SET first_name = %s
            WHERE id = %s RETURNING first_name;
            ''', (new_first_name, id_user))
            new_name = cur.fetchone()[0]
        return f'Имя изменено на {new_name}'


def change_user_second_name() -> str:
    """
    Функция вызывается из основного модуля main
    Запрашивает новую фамилию и id пользователя
    Возвращает новую фамилию пользователя
    :return:
    """
    new_second_name = input('Введите новую фамилию: ')
    id_user = int(input('Введите id пользователя: '))
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            UPDATE users
            SET second_name = %s
            WHERE id = %s RETURNING second_name;
            ''', (new_second_name, id_user))
            new_name = cur.fetchone()[0]
        return f'Фамилия изменена на {new_name}'


def change_user_email() -> str:
    """
    Функция вызывается из основного модуля main
    Запрашивает новый email и id пользователя
    Возвращает новый email пользователя
    :return:
    """
    new_email = input('Введите новый email: ')
    id_user = int(input('Введите id пользователя: '))
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            UPDATE users
            SET email = %s
            WHERE id = %s RETURNING email;
            ''', (new_email, id_user))
            new_email = cur.fetchone()[0]
        return f'Email изменён на {new_email}'


def change_phones_phone_number() -> str:
    """
    Функция вызывается из основного модуля main
    Запрашивает новый номер телефона и id пользователя
    Возвращает новый номер пользователя
    :return:
    """
    new_phone_number = input('Введите новый номер телефона: ')
    id_phone = int(input('Введите id телефона: '))
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            UPDATE phones
            SET phone_number = %s
            WHERE id = %s RETURNING phone_number;
            ''', (new_phone_number, id_phone))
            new_number = cur.fetchone()[0]
        return f'Номер телефона изменён на {new_number}'