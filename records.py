from abc import ABC, abstractmethod
from datetime import date, datetime

import re


class Field():
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name

    def __repr__(self):
        return self.value


class Phone(Field):
    def __init__(self, phone=None):
        self.__value = []

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phones):
        if not phones:
            return
        try:
            for number in phones.split(' '):
                if re.match('^\\+38\d{10}$', number.strip()):
                    self.__value.append(number)
                else:
                    raise ValueError
        except ValueError:
            print('Incorrect phone number. Please use +380xxxxxxxxx format')


class Birthday(Field):
    def __init__(self, bday=None):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, bday):
        try:
            datetime_obj = datetime.strptime(bday, "%d-%m-%Y")
        except ValueError:
            print("Incorrect birthday. Please use dd-mm-yyyy format")
        else:
            self.__value = datetime_obj.date()


class Email(Field):
    def __init__(self, email=None):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, email):
        if not email:
            return
        try:
            if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
                self.__value = email
            else:
                raise ValueError
        except ValueError as error:
            return error
            # print('Incorrect email! Please Try again!')


class Address(Field):
    def __init__(self, address=None):
        self.value = address

    def __repr__(self):
        return self.value


class Record():
    def __init__(self, name: Name, phone: Phone = None, bday: Birthday = None, email: Email = None, address: Address = None):
        self.name = name
        self.phones = phone
        self.bday = bday
        self.email = email
        self.address = address

    def days_to_birthday(self):
        if self.bday.value != None:
            today = date.today()
            next_bday = self.bday.value.replace(year=today.year)

            if next_bday < today:
                next_bday = next_bday.replace(year=today.year + 1)

            days_to_bday = (next_bday - today).days

            return days_to_bday

    def add(record):
        return {record.name.value: record}

    def delete(self):
        del self.phones

    def edit(self, phone):
        self.phones[0].value = phone
