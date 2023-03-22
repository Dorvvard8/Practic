import pickle
import sys

import os
import datetime
from datetime import date
from datetime import timedelta
from AddressBook import *
from collections import UserDict

from pathlib import Path
from Note_book import *

os.system('cls||clear')


class MyException(Exception):
    def __init__(self, error):
        self.output = {'error1': 'Invalid input! Try again!',
                       'phone_error': 'Must be entered in the format: phone[space]username',
                       'phone_error1': 'The name is NOT already in the database',
                       'phone_error2': 'Incorrect number phone!',
                       'birthday_error': '--Birthday is empty!',
                       'date_error': 'Incorrect date birthday!',
                       'add_error1': 'The name is already in the database',
                       'add_error2': 'The phone is already in the database',
                       'change_error1': 'The name is NOT already in the database',
                       'hello': '--How can I help you?',
                       'show_error1': '--The base is empty!',
                       'close': '--Good bye!'
                       }
        print(self.output[error])
        if error == 'close':
            sys.exit()


class Parser():
    def __init__(self):
        self.contact = AddressBook()
        self.contact.load()

        self.base = {}
        self.OPERATIONS = {
            'good bye': self.good_bye,
            'exit': self.good_bye,
            'close': self.good_bye,
            'hello': self.hello,
            'show all': self.show_all,
            'phone ': self.get_number,
            'add ': self.add,
            'change ': self.change,
            'iterator': self.iterator,
            'save': self.save,
            'search': self.search
        }

    def inputString(self, input_string):
        try:
            # self.contact = contact
            self.input_string = input_string.lower().strip()
            for i in self.OPERATIONS.keys():
                if i + self.input_string[len(i):] == self.input_string:
                    my_return = self.get_handler(i)(input_string)
                    break
            else:
                raise MyException('error1')
        except MyException:
            pass

    def save(self, input_string):
        if input_string == 'save':
            return self.contact.save()
        else:
            raise MyException('error1')

    def search(self, input_string):
        if input_string == 'search':

            print("Enter categorie: \n\nName \nPhones \nBirthday")
            category = input('Enter category: ')
            category = category.lower().strip()
            shab = input('Enter text: ')
            shab = shab.lower().strip()
            result = self.contact.search(shab, category)
            for cont in result:
                print(cont)
        else:
            raise MyException('error1')

    def search_with_name(self, name):
        print(name)
        result = self.contact.search_with_name(name)
        return result

    def search(self, pattern, category):
        result = self.contact.search(pattern, category)
        return result
    
    def delete(self, name):
        self.contact.delete(name)

    def iterator(self, input_string):
        if input_string == 'iterator':
            return self.contact.iterator()
        else:
            raise MyException('error1')

    def good_bye(self, input_string):
        if input_string in ['close', 'exit', 'good bye']:
            raise MyException('close')
        else:
            raise MyException('error1')

    def hello(self, input_string):
        if input_string == 'hello':
            raise MyException('hello')
        else:
            raise MyException('error1')

    def show_all(self, input_string):
        # print('self.data - ', self.contact.data)
        if input_string == 'show all':
           # print('self.data - ', self.contact.data)
            return self.contact.show_all()
            # return self.contact.show_all()
        else:
            raise MyException('error1')

    def show_all2(self):
        return self.contact.show_all2()

    def get_number(self, input_string):
        if input_string[0:6] != 'phone ':
            raise MyException('error1')
        else:
            return self.contact.get_number()
# add Dima +380678888888 23-03-1976
# add Vasya +380637777777 01-01-2000
# add Klava +380503333333

    def add(self, input_string):
        print("def add")
        self.answer = input_string.split()
        # self.answer = input_string.lower().strip()

        name = Name(self.answer[1])

        phone = Phone()
        phone.value = self.answer[2]

        bday = Birthday()
        bday.value = self.answer[3]
        
        address = Address()
        address.value = self.answer[4]
              
        record = Record(name, phone, bday, address)
        return self.contact.add_record(record)

    def change(self, input_string):
        list_add = input_string.split()
        if input_string[0:7] != 'change ' or len(list_add) != 3:
            raise MyException('error1')
        if list_add[1] not in base:
            raise MyException('change_error1')
        elif list_add[2] in base.values():
            raise MyException('add_error1')
        return self.contact.change()

    def get_handler(self, operator):
        return self.OPERATIONS[operator]

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
    def input_error(func):
        # Декоратор помилок
        pass
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except KeyError:
                return "This record not exist. Try again."
            except ValueError:
                return "This record is not correct. Try again."
            except IndexError:
                return "Wrong command."
            except Exception:
                return "Error. Try again."

        return wrapper


    @input_error      # створення нової нотатки
    def new_note(self, text):
        note_ = RecordNote(text)
        result = notebook.add_new_note(note_)
        #notebook.save_to_file()
      
        return result


    @input_error    # редагування нотатки
    def edit_note(self, value):
        id_, text = value.split(" ", 1)
        notebook.to_edit_text(id_, text)
        notebook.save_to_file()
        return f"Note with id: {id_} - changed."


    @input_error     # додавання теги
    def tags(self, value):
        id_, *tags_ = value.split()
        notebook.to_add_tags(id_, list(tags_))
        notebook.save_to_file()
        return f"Tag for note with id: {id_} - added."


    @input_error   # подивитись всі нотатки
    def show_notes(self, value):
        return notebook.show_all_notes()


    @input_error   # відалення нотатки
    def delete_notes(self, id_):
        notebook.to_remove_note(id_)
        notebook.save_to_file()
        return f'Note with id: {id_} - deleted.'


    @input_error   # пошук нотатки за словом
    def search_notes(self, text_to_search):
        return notebook.search_note(text_to_search)


    @input_error   # пошук нотатки за тегом
    def search_tags(self, tag_to_search):
        return notebook.search_tag(tag_to_search)


    COMMANDS = {
        "add note": new_note,
        "change note": edit_note,
        "add tag": tags,
        "show notes": show_notes,
        "remove note": delete_notes,
        "search note": search_notes,
        "search tag": search_tags,
    }
