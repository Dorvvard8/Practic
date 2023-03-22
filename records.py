from abc import ABC, abstractmethod
from datetime import date, datetime, timedelta

import re


class Field():
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name

    def __repr__(self):
        return self.value


class Phone(Field):
    def __init__(self, phone=''):
        self.__value = []

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phones):

        if not phones:
            self.__value = []
            return

        try:
            print('phones = ', phones)
            for number in phones.split(' '):
                if re.match('^\\+38\d{10}$', number.strip()):
                    self.__value.append(number)
                else:
                    raise ValueError
        except ValueError:
            print('Incorrect phone number. Please use +380xxxxxxxxx format')


class Birthday(Field):
    def __init__(self, bday=''):
        self.__value = bday

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, bday):

        if not bday:
            self.__value = ''
            return
        bday = bday.replace('/', '.').replace('-', '.')
        try:
            datetime_obj = datetime.strptime(bday, "%d.%m.%Y")
        except ValueError:
            print("Incorrect birthday. Please use dd-mm-yyyy format")
        else:
            self.__value = datetime_obj.date()

        
class Email(Field):
    def __init__(self, email=''):
        self.__value = email

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, email):
        print('emaillll - ', email)
        if not email:
            self.__value = None
            return
        if email == '*':
            self.__value = email
            return
        print('emaillll22222 - ', email)        
        try:
            if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
                print('emaillll22222 - ', email)
                self.__value = email
            else:
                raise ValueError
        except ValueError:
            print('Incorrect email. Please Try again!')


class Address(Field):
    def __init__(self, address=''):
        self.value = address

    def __repr__(self):
        return self.value


class Record():
    def __init__(self, name, phone='', birthday='', address=''):
        self.name = name
        self.phones = phone
        self.birthday = birthday
        self.address = address

    def days_to_birthday(self):
        if self.birthday.value != None:
            today = date.today()
            next_bday = self.birthday.value.replace(year=today.year)

            if next_bday < today:
                next_bday = next_bday.replace(year=today.year + 1)

            days_to_bday = (next_bday - today).days

            return days_to_bday

    def add(record):
        
        return {record.name.value: record}

    def edit(self, parameter, new_value):
        if parameter == "phone":
            self.phones.value = new_value
            print("Phone has been edited")
        elif parameter == "birthday":
            self.bday.value = new_value
            print("Birthday has been edited")
        elif parameter == "email":
            self.email.value = new_value
            print("Email has been edited")
        elif parameter == "address":
            self.address.value = new_value
            print("Address has been edited")
