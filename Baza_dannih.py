
import csv
def read_csv(filename):
    contacts = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            Surname, Name, Phone_number, Description = row
            contacts[Surname] = {
                'name': Name,
                'phone_number': Phone_number,
                'description': Description
            }
    return contacts

def show_menu():
    print("\n Выберите необходимое действие \n"
          "1. Отоброзить весь справочник\n"
          "2. Найти обонента по Фамилии\n"
          "3. Найти обонента по номеру телефона\n"
          "4. Добавить обонента в справочник\n"
          "5. Сохронить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def work_with_phonebook():

    phone_book = read_csv('contacts1.csv')
    choice = show_menu()    

    while (choice!=6):

        if choice==1:
            print_phonebook(phone_book)
        elif choice==2:
            last_name=input('Введите фамилию: ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('Введите номер телефона: ')
            new_number=input('Новый номер телефона: ')
            print(find_by_phone_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('Введите данные нового обонента: ')
            print(add_contact(phone_book,lastname))
        elif choice == 5:
            save_phonebook(phone_book, 'phonebook.txt')

        choice=show_menu()

def print_phonebook(phone_book):
    print("Справочник:")
    for surname, contact in phone_book.items():
        print(f"{surname}: {contact['name']}, {contact['phone_number']}, {contact['description']}")

def find_by_last_name(phone_book, last_name):
    if last_name in phone_book:
        contact = phone_book[last_name]
        return f"{contact['name']}, {contact['phone_number']},{contact['description']}"
    else:
        return "Контакт не найден"

def find_by_phone_number(phone_book, phone_number):
    for contact in phone_book.values():
        if contact['phone_number'] == phone_number:
            return f"{contact['name']}, {contact['phone_number']},{contact['description']}"
        else:
            return "Контакт не найден"


def add_contact(phone_book):
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone_number = input('Введите номер телефона: ')
    description = input('Введите описание: ')
    new_contact = {
        'name' : name,
        'phone_number' : phone_number,
        'description' : description
    }
    phone_book[last_name] = new_contact
    print("Контакт добавлен")



def save_phonebook(phone_book, filename):
    with open(filename,'w', encoding='utf-8') as file:
        writer = txt.writer(file)
        for last.name, contact in phone_book.items():
            name = contact['name']
            phone_number = contact['phone_number']
            description = contact['description']
            writer,writerow(last_name,name,phone_book,description)
        print("Справочник сохронен в файле", filename)

work_with_phonebook()