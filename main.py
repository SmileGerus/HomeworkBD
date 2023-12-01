from create_table import create_tables
from insert_data import users_insert, phones_insert
from update_data import change_data
from delete_data import delete_phone_number, delete_user
from select_data import select_data


# Справка для пользователей
def prog_help() -> str:
    return '''
    Создать таблицы users и phones - /create_table
    Добавить в таблицу данные - /insert
    Изменить данные в таблице - /change
    Удалить данные в таблице - /delete
    Найти клиента по параметру - /find_user
    Закрыть программу - /exit
    '''


def main():
    '''
    Это ядро программы. Здесь реализован интерфейс взаимодействия с пользователем.
    request принимает команды от пользователей и в зависимости от ответа перенаправляет в разные модули.
    '''
    print('Добро пожаловать! Для получения справки введите команду: /help')
    while True:
        request = input('Введите команду: ')
        if request == '/help':
            print(prog_help())
        elif request == '/create_db':
            print(create_tables())
        elif request == '/insert':
            table = input('Введите название таблицы (users или phones): ')
            if table == 'users':
                first_name = input('Введите имя: ')
                second_name = input('Введите фамилию: ')
                email = input('Введите email: ')
                print(users_insert(first_name, second_name, email))
            elif table == 'phones':
                phone_number = input('Введите номер телефона: ')
                user_email = input('Введите email пользователя: ')
                print(phones_insert(phone_number=phone_number, email=user_email))
            else:
                print('Неправильное название таблицы!')
        elif request == '/change':
            what_change = input('''
                    Выберете параметр для изменения:

                    Имя - first_name
                    Фамилия - second_name
                    Email - email
                    Номер телефона - phone_number
                    ''')
            ch_data = change_data()
            try:
                ch_data.get(what_change)()
            except KeyError:
                print('Неправильная команда!')
        elif request == '/delete':
            what_delete = input('''
            Введите данные, которые хотите удалить:
            Номер телефона - phone_number
            Клиента - user
            ''')
            if what_delete == 'phone_number':
                delete_number = input('Введите номер телефона, который хотите удалить: ')
                print(delete_phone_number(delete_number))
            elif what_delete == 'user':
                delete_email = input('Введите email клиента, которого хотите удалить: ')
                print(delete_user(delete_email))
        elif request == '/find_user':
            what_find = input('''
                Введите параметр поиска:
                
                Имя - first_name
                Фамилия - second_name
                Email - email
                Номер телефона - phone_number
            ''')
            try:
                find = select_data()
                print(find.get(what_find)())
            except KeyError:
                print('Неправильная команда!')
        elif request == '/exit':
            break
        else:
            print('Неправильная команда!')


if __name__ == '__main__':
    main()
