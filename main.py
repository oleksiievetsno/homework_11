from collections import UserDict
from typing import Optional, List


def input_error(func):
    def wrapper(*args, **kwars):
        try:
            func(*args, **kwars)
        except KeyError:
            print("Please enter correct username and phone")
        except ValueError:
            print("Please enter a valid phone number")
        except IndexError:
            print("Please enter a username and maybe a phone number ")
    return wrapper


class Field:
    """Fields of records in contact book : name , phone/phones , etc."""

    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    """Phone of the contact"""

    def __eq__(self, other: object) -> bool:
        return self.value == other.value

    def __str__(self):
        return f"Phone:{self.value}"


class Record:
    """Records(contacts) in users contact book.
    Only one name , but it can be more than one phone"""

    def __init__(self, name: str, phone: List[str] = None) -> None:
        if phone is None:
            self.phone = []
        else:
            self.phone = [Phone(p) for p in phone]
        self.name = Name(name)

    def add_phone(self, phone_number: str) -> None:
        phone = Phone(phone_number)
        if phone not in self.phone:
            self.phone.append(phone)

    def find_phone(self, phone: str) -> Optional[Phone]:
        for p in self.phone:
            if p.value == phone:
                return p

    def delete_phone(self, phone: str) -> None:
        phone_to_delete = self.find_phone(phone)
        self.phone.remove(phone_to_delete) if phone_to_delete else None

    def edit_phone(self, old_phone, new_phone) -> None:
        new_phone = Phone(new_phone)
        phone_to_remove = self.find_phone(old_phone)
        if phone_to_remove:
            self.phone.remove()
            self.phone.append(new_phone)

    def __str__(self):
        return f"Record of {self.name.value}, phones {[p.value for p in self.phone]}"


class AddressBook(UserDict):
    """All contacts data"""

    def add_record(self, record: list) -> None:
        new_record = Record(record[0], record[1:])
        self.data[new_record.name.value] = new_record

    def find_record(self, value: str) -> Optional[Record]:
        return self.data.get(value)

    def delete_record(self, value: str) -> None:
        self.data.pop(value)


def check_exit_words(message):
    # I will use it later
    # Бот завершает свою работу, если встречает слова:
    exit_words = {'close', 'exit', 'good bye'}
    return bool(exit_words & set([message]))


@input_error
def response_hello(*args, **kwars):  # I will use it later
    print("How I can help you?")


# COMMAND_HANDLERS = {
#     'phone': show_phone,
#     'show all': show_all_contacts,
#     'add': add_new_contact,
#     'change': change_phone,
#     'hello': response_hello,
# }

# I will use it later
def parser_user_input(user_input):
    """This function returns tuple with command and remaining user input"""
    user_input = user_input.split()
    if user_input[0] == 'phone':
        return 'phone', user_input[1:]
    elif user_input[0] == 'add':
        return 'add', user_input[1:]
    elif user_input[0] == 'change':
        return 'change', user_input[1:]
    elif user_input[0] == 'hello':
        return 'hello', user_input[1:]
    elif user_input[0] == 'show' and user_input[1] == 'all':
        return 'show all', user_input[2:]


def main():
    book = AddressBook()
    book.add_record(["Nazar", "666 666 666"])

    print(book)
    record = book.find_record("Nazar")
    book.delete_record("Nazar")

    print(book)
    print(record)

# This part would be modified later
    # while True:
    #     user_input = input("Please enter the task:").lower()

    #     if check_exit_words(user_input):
    #         print("Good bye!")
    #         break

    #     try:
    #         command, message = parser_user_input(user_input)
    #     except TypeError:
    #         print("Please enter a valid command")
    #         continue
    #     except IndexError:
    #         print("Please enter a full command")
    #         continue

    # command_handler = COMMAND_HANDLERS.get(command)
    # command_handler(book, message)


if __name__ == '__main__':
    main()
