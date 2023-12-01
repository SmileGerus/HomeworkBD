import psycopg2


def users_insert(first_name='', second_name='', email='') -> str:
    """
    Функция вызывается из основного модуля main
    Принимает имя, фамилию, почту, возвращает присвоенное клиенту id
    :param first_name: string
    :param second_name: string
    :param email: string
    :return: string
    """
    try:
        with psycopg2.connect(database='homework', user='postgres',
                            password='159159-Smile') as conn:
            with conn.cursor() as cur:
                cur.execute('''
                INSERT INTO users(first_name, second_name, email) 
                VALUES(%s, %s, %s) RETURNING id;
                ''', (first_name, second_name, email))
                return f'Клиенту {first_name} {second_name} присвоено id - {cur.fetchone()[0]}'
    except psycopg2.errors.UniqueViolation:
        return "Такой email уже есть!"


def phones_insert(email, phone_number='') -> str:
    """
    Функция вызывается из основного модуля main
    Принимает почту пользователя, находит его id
    По id добавляет в бд и возвращает имя клиента, которому присвоен номер
    :param email: string
    :param phone_number: string
    :return: string
    """
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
                SELECT id, first_name, second_name FROM users
                WHERE email = %s;
            ''', (email,))

            user_id, first_name, second_name = cur.fetchall()[0]
            user_name = f'{first_name} {second_name}'
            cur.execute('''
               INSERT INTO phones(phone_number, user_id) 
               VALUES(%s, %s) RETURNING phone_number;
            ''', (phone_number, user_id))
            return f'К клиенту - {user_name}, добавлен номер {cur.fetchone()[0]}'

