from collections import UserDict
from records import *
import os
import pickle


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        self.backup_file = 'backup.bin'

    def add_record(self, record):
        self.data.update(Record.add(record))
        print("Contact has been added")

    def iterator(self, n):
        result_list = list(self.data.items())
        contacts_count = len(self.data)
        while True:
            if n <= contacts_count:
                yield result_list[:n]
            else:
                yield result_list[:contacts_count]

    def find(self, search_word, category) -> dict:
        result = {}

        for k, v in self.data.items():

            if category == 'phone':

                for i in v.phones.value:  # Search by value - phone
                    if i.rfind(search_word) >= 0:
                        result[k] = v

            elif category == 'name':

                if k.rfind(search_word) >= 0:  # Search by key - name
                    result[k] = v

            elif category == 'email':

                if v.email.value.rfind(search_word) >= 0:  # Search by value - email
                    result[k] = v

        if result:
            return result

        print("Contact not found")

    def save(self):
        with open(self.backup_file, "wb") as file:
            pickle.dump(self, file)

    def load(self):
        with open(self.backup_file, "rb") as file:
            backup = pickle.load(file)

        return backup

    def delete(self, name):
        try:
            del self.data[name]
        except NameError:
            print("Contact not found")
        else:
            print(f"Cantact '{name}' has been deleted")

    def congratulate(self, days):
        now = date.today()
        result = {}

        for k in self.data:
            days_to_birthday = self.data[k].days_to_birthday()

            if days_to_birthday <= days:

                bday_planned = now + \
                    timedelta(days_to_birthday)
                result[k] = bday_planned.strftime("%d-%m-%Y")

        if result:

            return result

        print("No birthdays sheduled")
