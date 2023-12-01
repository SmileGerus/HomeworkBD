import psycopg2


def create_tables():
    """
    Функция вызывается из основного модуля main
    Создает в бд две таблицы: клиенты и телефоны
    Возвращает уведомление о успешном создании таблиц
    :return:
    """
    with psycopg2.connect(database='homework', user='postgres',
                          password='159159-Smile') as conn:
        with conn.cursor() as cur:
            cur.execute('''
            CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(40) NOT NULL,
            second_name VARCHAR(40) NOT NULL,
            email VARCHAR(80) UNIQUE NOT NULL
            );
            ''')

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Phones (
                id SERIAL PRIMARY KEY,
                phone_number VARCHAR(80) UNIQUE NOT NULL,
                user_id INTEGER NOT NULL REFERENCES Users(id)
                );
                ''')
            conn.commit()
    conn.close()
    return 'Таблицы успешно созданы!'

