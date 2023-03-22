from collections import UserDict
from records import *
import os
import pickle
import pathlib


class AddressBook(UserDict):
    def __init__(self):
        self.data = []
        self.backup_file = 'helperbob.bin'

    def show_all(self):
        result = []
        if len(self.data) > 0:
            print('self.data - ', self.data)
            for account in self.data:
                if account['birthday']:
                    birth = account['birthday'].value.strftime("%d.%m.%Y")
                else:
                    birth = ''
                print('phones - ', account['phones'].value)
                if account['phones']:
                    new_value = []
                    for phone in account['phones'].value:
                        if phone:
                            new_value.append(phone)
                    phone = ', '.join(new_value)
                else:
                    phone = ''
                
                result.append(
                    f"Name: {account['name']} \nPhones: {phone} \nBirthday: {birth} \nAddress: {account['address']}\n" + "_" * 50 + '\n')
            return '\n'.join(result)
        else:
            return f"Address book is empty.\n"

    def add_record(self, record):
        account = {'name': record.name,
                   'phones': record.phones,
                   'birthday': record.birthday,
                   'address': record.address
        }
        
        self.data.append(account)
        self.save()
        print("Contact has been added")

    def iterator(self, n):
        result_list = list(self.data.items())
        contacts_count = len(self.data)
        while True:
            if n <= contacts_count:
                yield result_list[:n]
            else:
                yield result_list[:contacts_count]

    def search(self, pattern, category):
        result = []

        #category_new = category.strip().lower().replace(' ', '')
        pattern_new = pattern.strip().lower().replace(' ', '')
        print(f'pattern_new - {pattern_new}, category - {category}')
        for account in self.data:
            flag = False
            birth = account['birthday'].value.strftime("%d.%m.%Y")
            if category == 'phones':
                for phone in account['phones'].value:
                    print(phone)
                    if phone.find(pattern_new) != -1:
                        flag = True
            elif  category == 'name':
                #print(f'pattern_new - {pattern_new}, category - {category}')
                if account[category].value.lower().replace(' ', '').find(pattern_new) != -1:
                    flag = True
            elif category == 'birthday':
                if birth.lower().replace(' ', '').find(pattern_new) != -1:
                    flag = True
            else:
                if account[category].lower().replace(' ', '').find(pattern_new) != -1:
                    flag = True
            if flag:
                result.append(
                    f"Name: {account['name']} \nPhones: {account['phones'].value} \nBirthday: {birth} \nAddress: {account['address']}\n" + "_" * 50 + '\n')
        if not result:
            return 'There is no such contact in address book!'
        return '\n'.join(result)

    def save(self):
        list_save = []
        for account in self.data:
            if account['birthday']:
                birth = account['birthday'].value.strftime("%d.%m.%Y")
            else:
                birth = ''
            if account['phones']:
                new_value = []
                for phone in account['phones'].value:
                    if phone:
                        new_value.append(phone)
                phone = ', '.join(new_value)
            else:
                phone = ''
            list_save.append({'name': str(account['name']), 'phone': phone, 'birth': birth, 
                     'address': account['address']})
        print(list_save)
        with open(self.backup_file, "wb") as fh:
            pickle.dump(list_save, fh)

    def search_with_name(self, find_name):
        result = []
        for account in self.data:
            if account['name'].value == find_name:
                if account['birthday']:
                    birth = account['birthday'].value.strftime("%d.%m.%Y")
                else:
                    birth = ''
                if account['phones']:
                    new_value = []
                    for phone in account['phones'].value:
                        if phone:
                            new_value.append(phone)
                    phone = ', '.join(new_value)
                else:
                    phone = ''
                result0 = "_" * 50 + "\n" + \
                    f"Name: {account['name']} \nPhones: {phone} \nBirthday: {birth} \nAddress: {account['address']}\n" + "_" * 50 + '\n'
                result = [result0, account['name'].value, phone, birth, account['address']]
                break
        else:
            return 'Not found!\n'      
        return result        
                
                
        # for key, value in self.data.items():
        #     if category == 'birthday':
        #         if value.birthday.value.find(shab) != -1:
        #             result.append(
        #                 f'name: {key} phone: {value.phones[0].value} birthday: {value.birthday.value}')
        #     elif category == 'name':
        #         if str(key).find(shab) != -1:
        #             result.append(
        #                 f'name: {key} phone: {value.phones[0].value} birthday: {value.birthday.value}')
        #     elif category == 'name':
        #         if value.phones[0].value.find(shab) != -1:
        #             result.append(
        #                 f'name: {key} phone: {value.phones[0].value} birthday: {value.birthday.value}')
        #     else:
        #         result.append('Not find!')
        return result


    def load(self):

        # path = pathlib.Path(self.backup_file)
        # if path.exists():
        #     with open(self.backup_file, "rb") as fh:
                
        #         k = fh.read()
        #         print('k = ', k)
        #         if k:
        #             list_load = pickle.load(fh)
        file_name = 'helperbob.bin'
        path = pathlib.Path('helperbob.bin')
        if path.exists():
            with open(file_name, "r") as fh:
                read_string = fh.read()
            
            if read_string:
                with open(file_name, "rb") as fh:
                    unpacked = pickle.load(fh)    
                    print('________________________________________________')
                    print(unpacked)
                    print('________________________________________________')                
                    for account in unpacked:
                
                        name = Name(account['name'])

                        phone = Phone()
                        phone.value = account['phone']

                        bday = Birthday()
                        print('|' + account['birth'] + '|')
                        bday.value = str(account['birth']).strip()
                        record = Record(name, phone, bday)
                        account = {'name': record.name,
                                    'phones': record.phones,
                                    'birthday': record.birthday,
                                    'address': record.address
                        }

                        self.data.append(account)

    def delete(self, name):
        # try:
        #     del self.data[name]
        # except NameError:
        #     print("Contact not found")
        # else:
        k = -1
        for account in self.data:
            k += 1     
            if account['name'].value == name:
               break 
        self.data.pop(k)   
        self.save()
        print(f"Contact '{name}' has been deleted")
        print(self.data)

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

    