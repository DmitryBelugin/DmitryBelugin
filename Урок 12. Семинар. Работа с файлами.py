import os

def save_to_file(directory):
    with open('phonebook.txt', 'w') as f:
        for key, value in directory.items():
            f.write(f'{key}: {value}\n')

def load_from_file():
    if os.path.exists('phonebook.txt'):
        with open('phonebook.txt', 'r') as f:
            lines = f.readlines()
        directory = {}
        for line in lines:
            key, value = line.strip().split(': ')
            directory[key] = value
        return directory
    else:
        return {}

def search_in_directory(directory, search):
    for key, value in directory.items():
        if search.lower() in key.lower() or search in value:
            print(f'{key}: {value}')

def phonebook():
    directory = load_from_file()
    while True:
        print("\n1. Показать все контакты\n2. Добавить контакт\n3. Поиск\n4. Изменить контакт\n5. Удалить контакт\n6. Сохранить и выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            for key, value in directory.items():
                print(f'{key}: {value}')
        elif choice == '2':
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона: ")
            directory[name] = phone
        elif choice == '3':
            search = input("Введите имя контакта или номер телефона для поиска: ")
            search_in_directory(directory, search)
        elif choice == '4':
            name = input("Введите имя контакта, который вы хотите изменить: ")
            if name in directory:
                phone = input("Введите новый номер телефона: ")
                directory[name] = phone
            else:
                print("Контакт не найден.")
        elif choice == '5':
            name = input("Введите имя контакта, который вы хотите удалить: ")
            if name in directory:
                del directory[name]
            else:
                print("Контакт не найден.")
        elif choice == '6':
            save_to_file(directory)
            break

phonebook()