import psycopg2


def delete_phone_number(phone_number: str) -> str:
    """
    Функция вызывается из основного модуля main
    Принимает номер телефона, ищет по номеру id
    Удаляет по id и возвращает id
    :param phone_number: string
    :return: string
    """
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
                SELECT id FROM phones
                WHERE phone_number = %s;
            ''', (phone_number,))
            phone_id = cur.fetchone()[0]
            cur.execute('''
                DELETE FROM phones
                WHERE id = %s;
            ''', (phone_id,))
            return f'Номер с id {phone_id} удален'


def delete_user(email: str) -> str:
    '''
    Функция вызывается из основного модуля main
    Принимает почту, ищет id пользователя
    Удаляет пользователя по id и возвращает id
    :param email: string
    :return: string
    '''
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
                SELECT id FROM users
                WHERE email = %s;
            ''', (email,))
            user_id = cur.fetchone()[0]
            cur.execute('''
                DELETE FROM users
                WHERE id = %s;
            ''', (user_id,))
            return f'Номер с id {user_id} удален'