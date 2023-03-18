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
    email = Email()
    email.value = 'bill@gmail.com'
    address = Address('1st Street')
    record = Record(name, phone, bday, email, address)
    ab.add_record(record)

    # Add contact 2
    name = Name('Jack')
    phone = Phone()
    phone.value = "+38097777777"
    bday = Birthday()
    bday.value = '23-01-2009'
    email = Email()
    email.value = 'test@gmail.com'
    address = Address('2nd Street')
    record = Record(name, phone, bday, email, address)
    ab.add_record(record)

    # Pagination
    print(next(ab.iterator(2)))

    # Save contacts to file
    ab.save()

    # Load contacts from file
    ab = ab.load()

    # Find contact by email
    print(ab.find("777", "phone"))

    # Find contact by email
    print(ab.find("test", "email"))

    # Find contact by name
    print(ab.find("Ja"), "name")
