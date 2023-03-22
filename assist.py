import pickle
from pathlib import Path
from Note_book import *


def input_error(func):
    # Декоратор помилок

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
def new_note(text):
    note_ = RecordNote(text)
    notebook.add_new_note(note_)
    notebook.save_to_file()
    return f"Note added."


@input_error    # редагування нотатки
def edit_note(value):
    id_, text = value.split(" ", 1)
    notebook.to_edit_text(id_, text)
    notebook.save_to_file()
    return f"Note with id: {id_} - changed."


@input_error     # додавання теги
def tags(value):
    id_, *tags_ = value.split()
    notebook.to_add_tags(id_, list(tags_))
    notebook.save_to_file()
    return f"Tag for note with id: {id_} - added."


@input_error   # подивитись всі нотатки
def show_notes(value):
    return notebook.show_all_notes()


@input_error   # відалення нотатки
def delete_notes(id_):
    notebook.to_remove_note(id_)
    notebook.save_to_file()
    return f'Note with id: {id_} - deleted.'


@input_error   # пошук нотатки за словом
def search_notes(text_to_search):
    return notebook.search_note(text_to_search)


@input_error   # пошук нотатки за тегом
def search_tags(tag_to_search):
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


def main():
    while True:
        command = input('Enter command: ')
        command = command.strip().lower()
        if command in ("exit", "close", "good bye", "."):
            print("Good bay!")
            break
        else:
            for key in COMMANDS:
                if key in command:
                    print(COMMANDS[key](command[len(key):].strip()))
                    break


if __name__ == "__main__":
    main()
