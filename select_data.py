import psycopg2


def select_data() -> dict:
    """
    Словарь с функциями, который вызывается из основного модуля main
    :return:
    """
    commands = {
        'first_name': select_user_by_first_name,
        'second_name': select_user_by_second_name,
        'email': select_user_by_email,
        'phone_number': select_user_by_phone_number
    }
    return commands


def select_user_by_first_name() -> str:
    """
    Вызывается из основного модуля main
    запрашивает имя, возвращает данные клиентов с введенным именем
    :return:
    """
    name = input('Введите имя: ')
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            SELECT second_name, email, id FROM users
            WHERE first_name = %s;
            ''', (name,))
            result = 'Вот список клиентов с таким именем:\n'
            for data in cur.fetchall():
                second_name, email, user_id = data
                result += f'Имя - {name}, Фамилия - {second_name}, Email - {email}, Id - {user_id}\n'
            return result


def select_user_by_second_name() -> str:
    """
    Вызывается из основного модуля main
    запрашивает фамилию, возвращает данные клиентов с введенной фамилией
    :return:
    """
    second_name = input('Введите фамилию: ')
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            SELECT first_name, email, id FROM users
            WHERE second_name = %s;
            ''', (second_name,))
            result = 'Вот список клиентов с такой фамилией:\n'
            for data in cur.fetchall():
                first_name, email, user_id = data
                result += f'Имя - {first_name}, Фамилия - {second_name}, Email - {email}, Id - {user_id}\n'
            return result


def select_user_by_email() -> str:
    """
    Вызывается из основного модуля main
    запрашивает email, возвращает данные клиента с введенной почтой
    :return:
    """
    email = input('Введите email: ')
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            SELECT first_name, second_name, id FROM users
            WHERE email = %s;
            ''', (email,))
            first_name, second_name, user_id = cur.fetchall()[0]
            return f'Имя - {first_name}, Фамилия - {second_name}, Email - {email}, Id - {user_id}\n'


def select_user_by_phone_number() -> str:
    """
    Вызывается из основного модуля main
    запрашивает номер телефона, возвращает данные клиента с введенным номером
    :return:
    """
    phone_number = input('Введите номер телефона: ')
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            SELECT first_name, second_name, email, u.id FROM users u 
            JOIN phones p ON u.id = p.user_id 
            WHERE p.phone_number = %s;
            ''', (phone_number,))
            first_name, second_name, email, user_id = cur.fetchall()[0]
            return f'Имя - {first_name}, Фамилия - {second_name}, Email - {email}, Id - {user_id}\n'


