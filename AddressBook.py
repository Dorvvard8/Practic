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

    def iterator(self, n):
        result_list = list(self.data.items())
        contacts_count = len(self.data)
        while True:
            if n <= contacts_count:
                yield result_list[:n]
            else:
                yield result_list[:contacts_count]

    def find(self, search_word):

        for k, v in self.data.items():

            if search_word.isnumeric():

                for phone in v.phones.value:  # Search by value (phone)
                    if phone.rfind(search_word) >= 0:
                        return f'Search by "{search_word}": {v.name}, {v.phones}, {v.bday}'

            else:

                if k.rfind(search_word) >= 0:  # Search by key (name)
                    return f'Search by "{search_word}": {v.name.value}, {v.phones.value}, {v.bday.value}'

    def save(self):
        with open(self.backup_file, "wb") as file:
            pickle.dump(self, file)

    def load(self):
        with open(self.backup_file, "rb") as file:
            backup = pickle.load(file)

        return backup
