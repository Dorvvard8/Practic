from abc import ABC, abstractmethod
from datetime import date, datetime

import re


class Field(ABC):

    @abstractmethod
    def __getitem__(self):
        pass


class Name(Field):
    def __init__(self, name):
        self.value = name

    def __getitem__(self):
        return f"{self.value}"


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
        while True:
            try:
                for number in phones.split(' '):
                    if re.match('^\\+38\d{10}$', number.strip()):
                        self.__value.append(number)
                    else:
                        raise ValueError
            except ValueError:
                print(
                    'Incorrect phone number format - +380xxxxxxxxx. Try again!')
            else:
                break

    def __getitem__(self):
        return f"{self.value}"


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
            print("Incorrect birthday format. Please use dd-mm-yyyy format)")
        else:
            self.__value = datetime_obj.date()

    def __getitem__(self):
        return f"{self.value}"


class Record():
    def __init__(self, name: Name, phone: Phone = None, bday: Birthday = None):
        self.name = name
        self.phones = phone
        # if phone.value:
        #     self.phones.append(phone)
        self.bday = bday

    def days_to_birthday(self):
        if self.bday.value != None:
            today = date.today()
            next_bday = self.bday.value.replace(year=today.year)
            if next_bday < today:
                next_bday = next_bday.replace(year=today.year + 1)

            days_to_bday = (next_bday - today).days
            return f"{days_to_bday} days to birthday"

    def add(record):
        return {record.name.value: record}

    def delete(self):
        del self.phones

    def edit(self, phone):
        self.phones[0].value = phone
