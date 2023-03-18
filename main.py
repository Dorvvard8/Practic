from AddressBook import *


# Test
if __name__ == '__main__':
    # Add contact 1
    ab = AddressBook()
    name = Name('Bill')
    phone = Phone()
    phone.value = "+380977777777 +380977771234"
    bday = Birthday()
    bday.value = '23-01-2009'
    record = Record(name, phone, bday)
    ab.add_record(record)

    # Add contact 2
    name = Name('Jack')
    phone = Phone()
    phone.value = "+380977777777"
    bday = Birthday()
    bday.value = '23-01-2009'
    email = Email()
    email.value = 'test@gmail.com'
    record = Record(name, phone, bday, email)
    ab.add_record(record)

    # Pagination
    print(next(ab.iterator(2)))

    # Save contacts to file
    ab.save()

    # Load contacts from file
    ab = ab.load()

    # Find contact by phone
    print(ab.find("777"))

    # Find contact by name
    print(ab.find("Ja"))
