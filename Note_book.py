import pickle
from datetime import datetime


def id_exist(func):
    # Декоратор для перевірки id

    def wrapper(*args):
        id_ = args[1]
        if int(id_):
            res = func(*args)
            return res
        else:
            return f"The note with ID: {id_} is absent"
    return wrapper


class Tag:
    # Клас для створення Тег

    def __init__(self, word):
        self.word = word.lower()


class RecordNote:
    # Клас для запису нотаток

    def __init__(self, note: str):
        self.note = note
        self.tags = []
        self.date = datetime.now().date()

    def edit_text(self, text_):
        self.note = text_

    def add_tags(self, tags: list[str]):
        for tg in tags:
            self.tags.append(Tag(tg))

    def __del__(self):
        return f"The Note was delete."


class Notebook:
    # Клас для створення нотаток

    counter = 0

    def __init__(self):
        self.notes = {}
        self.read_from_file()

    def add_new_note(self, note: RecordNote):
        result = []
        self.notes[self.counter+1] = note
        self.counter += 1
        self.save_to_file()

        return self.counter

    def read_from_file(self):
        try:
            with open("notes.bin", "rb") as fh:
                self.notes = pickle.load(fh)
                if self.notes:
                    self.counter = max(self.notes.keys())
        except FileNotFoundError:
            self.notes = {}
            self.counter = 0

    def save_to_file(self):
        with open("notes.bin", "wb") as fh:
            pickle.dump(self.notes, fh)

    def show_all_notes(self):
        if len(self.notes) > 0:
            result = ""
            for id_, rec in self.notes.items():
                tgs = [tg.word.lower() for tg in rec.tags]
                tags = ", ".join(tgs)
                date = rec.date
                result += f"id: {id_} \n date: {date} \n tags: {tags} \n note: \n {rec.note} \n"
            return result
        else:
            return f"Notebook is empty.\n"

    @id_exist
    def to_edit_text(self, id_, text_):
        self.notes[int(id_)].edit_text(text_)

    @id_exist
    def to_add_tags(self, id_, tags: list[str]):
        print('id_, tags - ', id_, tags)
        self.notes[int(id_)].add_tags(tags)

    @id_exist
    def to_remove_note(self, id_):
        del self.notes[int(id_)]
        return f"The note id: {id_} was delete!"

    @id_exist
    def show_note(self, id_):
        tgs = [tg.word.lower() for tg in self.notes[int(id_)].tags]
        tags = ", ".join(tgs)
        return f"id: {id_} | date: {self.notes[int(id_)].date} | {self.notes[int(id_)].note} \ tags: {tags} \n "

    def search_note(self, text_to_search: str):
        for id_, value in self.notes.items():
            if text_to_search.lower().strip() in value.note.lower():
                tgs = [tg.word for tg in value.tags]
                tags = ", ".join(tgs)
                res = f"id: {id_} | date: {value.date} | {value.note} | tags: {tags} \n"
                return res

    def search_tag(self, tag_to_search: str):
        for id_, value in self.notes.items():
            tgs = [tg.word.lower() for tg in value.tags]
            if len(tgs) == 0:
                tgs = [""]
            if tag_to_search.lower().strip() in tgs:
                tags = ", ".join(tgs)
                res = f"id: {id_} | date: {value.date} | {value.note} | tags: {tags} \n"
                return res


notebook = Notebook()
