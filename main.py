import re
def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=8):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            change_number(phone_book,last_name,new_number)
            write_txt('phonebook.txt',phone_book)
        elif choice==4:
            lastname=input('lastname ')
            delete_by_lastname(phone_book,lastname)
            write_txt('phonebook.txt',phone_book)
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        elif choice==7:
            last_name = input('Введите фамилию')
            new_file = input('Введите название нового файла')
            change_file(last_name, new_file, phone_book)
            


        choice=show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер телефона абонента\n"
          "4. Удалить абонента по фамилии\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить нового пользователя\n"
          "7. Перенести пользователя из одного справочника в другой\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
            unnor_string = line.split(',')
            normal_string = list()
            for word in unnor_string:
                new_word = re.sub("[^А-ЯЁа-я0-9]^[ ]","", word).strip()
                normal_string.append(new_word)
            record = dict(zip(fields, normal_string))
            phone_book.append(record)


    return phone_book


global write_txt
def write_txt(filename, phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')

def add_user(phone_book, user_data):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    unnor_string = user_data.split(',')
    normal_string = list()
    for word in unnor_string:
        new_word = re.sub("[^А-ЯЁа-я0-9]^[ ]","", word).strip()
        normal_string.append(new_word)
    record = dict(zip(fields, normal_string))
    phone_book.append(record)
    
def delete_by_lastname(phone_book, last_name):
       for contact in phone_book:
         for key, element in contact.items():
             if element == last_name and key== "Фамилия":
                phone_book.remove(contact) 
                  

def change_file(last_name,new_file, phone_book):
    new_phonebook = list()
    for contact in phone_book:
         for key, element in contact.items():
             if element == last_name  and key== "Фамилия":
                new_phonebook.append(contact)
    write_txt(new_file, new_phonebook)
    
def find_by_number(phone_book, number):
    list_lastname = list()
    for contact in phone_book:
         for key, element in contact.items():
             if element == number and key== "Телефон":
                  list_lastname.append(contact)
    for contact in list_lastname:
        for key, element in contact.items():
            print(f"{key}:{element}", end=".\n ")    
    
def change_number(phone_book,last_name,new_number):
    for contact in phone_book:
         for key, element in contact.items():
             if element == last_name and key == "Фамилия":
                contact["Телефон"] = new_number
                
    
def find_by_lastname(phone_book, last_name):
    list_lastname = list()
    for contact in phone_book:
         for key, element in contact.items():
             if element == last_name and key== "Фамилия":
                  list_lastname.append(contact)
    for contact in list_lastname:
        for key, element in contact.items():
            print(f"{key}:{element}", end=".\n ")
                     

def print_result(phone_book):
    for contact in phone_book:
        for key,element in contact.items():
            if key == "Описание":
                print(f"{key}:{element}", end=".\n ")
                continue
            print(f"{key}:{element}", end=", ")
        
work_with_phonebook()


    
        