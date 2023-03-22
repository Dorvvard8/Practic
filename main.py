import tkinter as tk
import re
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from AddressBook import *
from parser import Parser
from assist import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = Parser()

        self.title("HelperBob")
        self.minsize(800, 600)
        self.maxsize(800, 600)
        self.geometry(self.position(800, 600))

        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}

        self.frames = []
        self.frames2 = ['name', 'phones', 'birthday', 'address']

        self.add_frame_menu()
        self.add_frame_adressbook()
        self.add_frame_note()
        self.add_frame_file()
        self.create_radio()

        self.active_frame = 0
        self.next_frame(self.active_frame)

        print('\n\n INIT \n\n')
        self.add_frame_output()

    def add_frame_note(self):

        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.frame_sub_menu = tk.Frame(
            self, width=300, height=400, borderwidth=1, relief=SOLID)
        self.frame_sub_menu.pack_propagate(False)

        frame000 = tk.Frame(self.frame_sub_menu)
        label_name = Label(frame000,  font=12,  text='Нотатки', width=100)
        label_name.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame000.pack(fill=X)

        frame1 = tk.Frame(self.frame_sub_menu)
        button_adress_add = Button(
            frame1, text="Add", width=10, command=self.frame_add_note)
        button_adress_add.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_add = Label(frame1, text='Add to notebook', width=100)
        label_add.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame1.pack(fill=X)

        frame2 = tk.Frame(self.frame_sub_menu)
        button_adress_edit = Button(
            frame2, text="Edit", width=10, command=self.add_frame_adress_edit)
        button_adress_edit.pack(anchor=NW, side=LEFT,
                                fill=NONE, padx=10, pady=10)
        label_edit = Label(frame2, text='edit notebook', width=100)
        label_edit.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame2.pack(fill=X)

        frame3 = tk.Frame(self.frame_sub_menu)
        button_adress_del = Button(
            frame3, text="Delete", width=10, command=self.frame_delete_note)
        button_adress_del.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_del = Label(frame3, text='Delete entry from notebook', width=100)
        label_del.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame3.pack(fill=X)

        frame4 = tk.Frame(self.frame_sub_menu)
        button_adress_del = Button(
            frame4, text="Search", width=10, command=self.frame_search_note)
        button_adress_del.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_del = Label(frame4, text='Search in notebook', width=100)
        label_del.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame4.pack(fill=X)

        frame5 = tk.Frame(self.frame_sub_menu)
        button_adress_del = Button(
            frame5, text="Search(tag)", width=10, command=self.show_all)
        button_adress_del.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_del = Label(frame5, text='Search by tag in notebook', width=100)
        label_del.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame5.pack(fill=X)

        frame6 = tk.Frame(self.frame_sub_menu)
        button_adress_del = Button(
            frame6, text="Show", width=10, command=self.show_all_note)
        button_adress_del.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_del = Label(
            frame6, text='Show all entries from the notebook', width=100)
        label_del.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame6.pack(fill=X)

        self.frames.append(self.frame_sub_menu)

    def note_shab(self):
        self.frames[self.active_frame].grid_remove()

        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}

        self.frame_sub_menu = tk.Frame(
            self, width=300, height=400, borderwidth=1, relief=SOLID)
        self.frame_sub_menu.pack_propagate(False)
        self.frame_sub_menu.grid(row=1, column=0, **opts)

        frame0 = Frame(self.frame_sub_menu)
        frame0.pack(fill=X)
        self.back_frame = 1
        button_adress_return = Button(
            frame0, text="<--Назад", width=10, command=self.back)
        button_adress_return.pack(side=LEFT, fill=NONE, padx=10, pady=10)

        frame111 = Frame(self.frame_sub_menu)
        frame111.pack(fill=X)

        frame01 = Frame(self.frame_sub_menu)
        frame01.pack(fill=X)

        # frame111 = Frame(self.frame_sub_menu)
        # frame111.pack(fill=X)

        frame101 = Frame(self.frame_sub_menu)
        frame101.pack(fill=X)

        if self.button_text2 == 'Додати' or self.button_text2 == 'Search':
            if self.button_text2 == 'Search':
                button_adress_search = Button(
                    frame101, text=self.button_text2, width=10, command=self.toparser_note_search)
            else:
                lbl1 = Label(frame111, text='Enter tag:', width=15, anchor=W)
                lbl1.pack(side=LEFT, padx=10, pady=10)
                self.entry_edit = Entry(frame111)
                self.entry_edit.pack(fill=X, padx=10, expand=True)
                button_adress_search = Button(
                    frame101, text=self.button_text2, width=10, command=self.toparser_note_add)
            button_adress_search.pack(fill=NONE, padx=10, pady=10)
            lbl1 = Label(frame111, text=self.label_text2, width=15, anchor=W)
            lbl1.pack(side=LEFT, padx=10, pady=10)
            self.note_text = Text(frame01, font=11, width=33, height=12,
                                  bg="green", fg='white', wrap=WORD)
            self.note_text.grid(**opts)
        elif self.button_text2 == 'Delete':
            # lbl1 = Label(frame111, text=self.label_text2, width=15, anchor=W)

            lbl1 = Label(frame111, text=self.label_text2, width=15, anchor=W)
            lbl1.pack(side=LEFT, padx=10, pady=10)
            self.entry_edit = Entry(frame111)
            self.entry_edit.pack(fill=X, padx=10, expand=True)
            button_adress_search = Button(
                frame101, text=self.button_text2, width=10, command=self.toparser_note_delete)
            button_adress_search.pack(fill=NONE, padx=10, pady=10)

    def frame_add_note(self):
        self.button_text2 = 'Додати'
        self.label_text2 = 'Введіть нотатку:'
        self.note_shab()

    def frame_delete_note(self):
        self.button_text2 = 'Видалити'
        self.label_text2 = 'Введіть id нотатки:'
        self.note_shab()

    def frame_search_note(self):
        self.button_text2 = 'Search'
        self.label_text2 = 'Enter search string:'
        self.note_shab()

    def back(self):
        self.frame_sub_menu.grid_remove()
        self.next_frame(self.back_frame)

    def toparser_note_search(self):
        result = self.parser.search_notes(self.note_text.get(1.0, END))
        result = '\n Знайдено запис(и):' + result + "_" * 52 + '\n'
        self.text.insert(1.0, result)

    def toparser_note_add(self):

        result = self.parser.new_note(self.note_text.get(1.0, END))
        print(result)
        print(self.entry_edit.get())
        self.parser.tags(str(result) + ' ' + self.entry_edit.get())

    def toparser_note_delete(self):
        result = self.parser.delete_notes(self.entry_edit.get())
        self.text.insert(1.0, result)

    def show_all_note(self):
        result = self.parser.show_notes(1)
        self.text.insert(1.0, result)
        print(result)

    def search_note(self):
        self.button_text = "Search"
        self.add_frame_shab()

    def to_remove_note(self):
        self.button_text2 = 'Видалити'

        result = self.parser.to_remove_note()
        self.text.insert(1.0, result)

    def position(self, width_root, height_root):
        width_root = int(width_root)
        height_root = int(height_root)
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - width_root // 2
        h = h - height_root // 2
        return '+{}+{}'.format(w, h)

    def show_all(self):
        self.text.delete("1.0", "end")
        result = self.parser.show_all('show all')
        self.text.insert(1.0, result)

    def text_breakdown(self, input_txt):
        self.txt = []
        self.txt = input_txt.strip('/n')
        for i in self.txt:
            print(i)

    def add_frame_menu(self):
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.frame_menu = tk.Frame(
            self, width=300, height=50, borderwidth=1, relief=SOLID)
        self.frame_menu.pack_propagate(False)
        self.frame_menu.grid(row=0, column=0, **opts)

    def add_frame_output(self):
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.frame_output = tk.Frame(
            self, width=500, height=300, borderwidth=1, relief=SOLID)
        self.frame_output.pack_propagate(False)
        self.text = Text(self.frame_output, font=11, width=52, height=40,
                         bg="black", fg='white', wrap=WORD)
        self.text.grid(**opts)
        self.frame_output.grid(row=0, column=1, rowspan=2, **opts)

    def add_frame_0(self):
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.frame_sub_menu = tk.Frame(
            self, width=300, height=400, borderwidth=1, relief=SOLID)
        self.frame_sub_menu.pack_propagate(False)

        frame1 = tk.Frame(self.frame_sub_menu)
        button_adress_add = Button(
            frame1, text="Додати", width=10, command=self.add_frame_adress_add)
        button_adress_add.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_add = Label(frame1, text='adressBook', width=100)
        label_add.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame1.pack(fill=X)

        self.frames.append(self.frame_sub_menu)

    def add_frame_adressbook(self):
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.frame_sub_menu = tk.Frame(
            self, width=300, height=400, borderwidth=1, relief=SOLID)
        self.frame_sub_menu.pack_propagate(False)

        frame000 = tk.Frame(self.frame_sub_menu)
        label_name = Label(frame000, font=12, text='Address book', width=100)
        label_name.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame000.pack(fill=X)

        frame1 = tk.Frame(self.frame_sub_menu)
        button_adress_add = Button(
            frame1, text="Add", width=10, command=self.add_frame_adress_add)
        button_adress_add.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_add = Label(frame1, justify=LEFT,
                          text='Add to address book', width=100)
        label_add.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame1.pack(fill=X)

        frame2 = tk.Frame(self.frame_sub_menu)
        button_adress_edit = Button(
            frame2, text="Edit", width=10, command=self.add_frame_adress_edit)
        button_adress_edit.pack(anchor=NW, side=LEFT,
                                fill=NONE, padx=10, pady=10)
        label_edit = Label(frame2, justify=LEFT,
                           text='Edit adress book', width=100)
        label_edit.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame2.pack(fill=X)

        frame3 = tk.Frame(self.frame_sub_menu)
        button_adress_del = Button(
            frame3, text="Delete", width=10, command=self.add_frame_adress_delete)
        button_adress_del.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_del = Label(frame3, justify=LEFT,
                          text='Delete from address book', width=100)
        label_del.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame3.pack(fill=X)

        frame4 = tk.Frame(self.frame_sub_menu)
        button_adress_del = Button(
            frame4, text="Search", justify=LEFT, width=10, command=self.add_frame_adress_search)
        button_adress_del.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_del = Label(frame4, justify=LEFT,
                          text='Search in address book', width=100)
        label_del.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame4.pack(fill=X)

        frame5 = tk.Frame(self.frame_sub_menu)
        button_adress_del = Button(
            frame5, text="Congratulation", width=10, command=self.show_all)
        button_adress_del.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_del = Label(frame5, justify=LEFT,
                          text='Happy Birthday', width=100)
        label_del.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame5.pack(fill=X)

        frame6 = tk.Frame(self.frame_sub_menu)
        button_adress_del = Button(
            frame6, text="Show", width=10, command=self.show_all)
        button_adress_del.pack(anchor=NW, side=LEFT,
                               fill=NONE, padx=10, pady=10)
        label_del = Label(
            frame6, justify=LEFT, text='Show entries from the address book', width=100)
        label_del.pack(anchor=NE, side=RIGHT, fill=NONE, padx=10, pady=10)
        frame6.pack(fill=X)

        self.frames.append(self.frame_sub_menu)

    def add_frame_adress_delete(self):
        self.button_text = "Видалити"
        self.add_frame_shab()

    def add_frame_adress_search(self):
        self.button_text = 'Search'
        self.add_frame_shab()
        self.create_radio2()

    def add_frame_adress_edit(self):
        self.button_text = "Редагувати"
        self.add_frame_shab()

    def add_frame_shab(self):

        self.frames[self.active_frame].grid_remove()

        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}

        self.frame_sub_menu = tk.Frame(
            self, width=300, height=400, borderwidth=1, relief=SOLID)
        self.frame_sub_menu.pack_propagate(False)
        self.frame_sub_menu.grid(row=1, column=0, **opts)

        frame0 = Frame(self.frame_sub_menu)
        frame0.pack(fill=X)
        button_adress_return = Button(
            frame0, text="<--Назад", width=10, command=self.remove_frame_adress_add)
        button_adress_return.pack(side=LEFT, fill=NONE, padx=10, pady=10)

        frame111 = Frame(self.frame_sub_menu)
        frame111.pack(fill=X)
        lbl1 = Label(frame111, text="Введіть ім'я запису:", width=15, anchor=W)
        lbl1.pack(side=LEFT, padx=10, pady=10)
        self.entry_edit = Entry(frame111)
        self.entry_edit.pack(fill=X, padx=10, expand=True)

        frame101 = Frame(self.frame_sub_menu)
        frame101.pack(fill=X)
        if self.button_text == 'Видалити':
            button_adress_search = Button(
                frame101, text="Видалити", width=10, command=self.search_with_name)
        elif self.button_text == 'Search':
            button_adress_search = Button(
                frame101, text="OK", width=10, command=self.search)
        else:
            button_adress_search = Button(
                frame101, text="OK", width=10, command=self.search_with_name)
        button_adress_search.pack(fill=NONE, padx=10, pady=10)

    def search(self):
        field_pattern = self.entry_edit.get()
        category = self.select
        result = self.parser.search(field_pattern, category)
        self.text.insert(1.0, result)
        # print('search ----', result)

    def search_with_name(self):
        name = self.entry_edit.get()
        self.field_name = name
        result = self.parser.search_with_name(name)
        print('result ----', result)
        if self.button_text == 'Видалити':
            if result != 'Not found!\n':
                self.remove()
            else:
                self.text.insert(1.0, result)
        else:
            if result != 'Not found!\n':

                self.text.insert(1.0, result[0])
                self.frame_sub_menu.grid_remove()
                self.add_frame_adress_add()
                self.entry1.insert(0, result[1])
                self.entry2.insert(0, result[2])
                self.entry3.insert(0, result[3])
                self.entry4.insert(0, result[4])
                self.entry5.insert(0, result[5])
                self.button_adress_add.destroy()
                self.button_adress_add = Button(
                    self.frame10, text=self.button_text, width=10, command=self.remove_add)
                self.button_adress_add.pack(fill=NONE, padx=10, pady=10)

            else:
                self.text.insert(1.0, result)

    def remove_add(self):
        self.parser.delete(self.field_name)
        self.add()
        self.remove_frame_adress_add()

    def remove(self):
        self.parser.delete(self.field_name)
        self.remove_frame_adress_add()

    def add_frame_adress_add(self):
        self.frames[self.active_frame].grid_remove()
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}

        self.frame_sub_menu = tk.Frame(
            self, width=300, height=400, borderwidth=1, relief=SOLID)
        self.frame_sub_menu.pack_propagate(False)
        self.frame_sub_menu.grid(row=1, column=0, **opts)

        frame0 = Frame(self.frame_sub_menu)
        frame0.pack(fill=X)
        button_adress_return = Button(
            frame0, text="<--Назад", width=10, command=self.remove_frame_adress_add)
        button_adress_return.pack(side=LEFT, fill=NONE, padx=10, pady=10)

        frame1 = Frame(self.frame_sub_menu)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Name:", width=15, anchor=W)
        lbl1.pack(side=LEFT, padx=10, pady=10)
        self.entry1 = Entry(frame1)
        self.entry1.pack(fill=X, padx=10, expand=True)

        frame2 = Frame(self.frame_sub_menu)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Phone:", width=15, anchor=W)
        lbl2.pack(side=LEFT, padx=10, pady=10)
        self.entry2 = Entry(frame2)
        self.entry2.pack(fill=X, padx=10, expand=True)

        frame3 = Frame(self.frame_sub_menu)
        frame3.pack(fill=X)
        lbl3 = Label(frame3, text="Birthday:", width=15, anchor=W)
        lbl3.pack(side=LEFT, padx=10, pady=10)
        self.entry3 = Entry(frame3)
        self.entry3.pack(fill=X, padx=10, expand=True)

        frame4 = Frame(self.frame_sub_menu)
        frame4.pack(fill=X)
        lbl4 = Label(frame4, text="Address:", width=15, anchor=W)
        lbl4.pack(side=LEFT, padx=10, pady=10)
        self.entry4 = Entry(frame4)
        self.entry4.pack(fill=X, padx=10, expand=True)

        self.frame10 = Frame(self.frame_sub_menu)
        self.frame10.pack(fill=X)
        self.button_adress_add = Button(
            self.frame10, text="Add", width=10, command=self.add)
        self.button_adress_add.pack(fill=NONE, padx=10, pady=10)

    def remove_frame_adress_add(self):
        self.frame_sub_menu.grid_remove()
        self.next_frame(0)

        self.frames.append(self.frame_sub_menu)

    def add_frame_file(self):
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.frame_sub_menu = tk.Frame(
            self, width=300, height=400, bg='red')
        self.frame_sub_menu.pack_propagate(False)
        tk.Label(self.frame_sub_menu, text='File').pack()
        self.frames.append(self.frame_sub_menu)

    def next_frame(self, active_frame):
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.frames[self.active_frame].grid_remove()
        self.frames[active_frame].grid(row=1, column=0, **opts)
        self.active_frame = active_frame

    def next_frame2(self, active_frame):
        self.select = self.frames2[active_frame]
        print(self.select)

    def dialog_adress_add(self):
        dialog = Dialog_adress_add(self)
        dialog.grab_set()

    def create_radio(self):
        var = IntVar()
        var.set(3)
        radio('Address book', 0, var, self)
        radio('Note', 1, var, self)
        radio('Folders sorter', 2, var, self)
        radio('0', 3, var, self)

    def create_radio2(self):
        var2 = IntVar()
        var2.set(0)
        radio2("Name", 0, var2, self)
        radio2('Phone', 1, var2, self)
        radio2('Birthday', 2, var2, self)
        radio2('Address', 3, var2, self)
        self.next_frame2(0)

    def add(self):
        self.answer = []
        self.answer.append(self.entry1.get())
        self.answer.append(self.entry2.get())
        self.answer.append(self.entry3.get())

        if self.entry4.get():
            address = self.entry4.get()
        else:
            address = '*'

        kkk = self.parser.add(
            f'add {self.entry1.get()} {self.entry2.get()} {self.entry3.get()} {address}')


class radio2:
    def __init__(self, text, val, var, obj):
        self.var2 = var
        self.obj2 = obj
        ttk.Radiobutton(
            self.obj2.frame_sub_menu,
            text=text,
            variable=self.var2,
            value=val,
            command=self.select).pack(anchor=SW, fill=NONE, padx=10, pady=10)

    def select(self):
        self.obj2.next_frame2(self.var2.get())


class radio:
    def __init__(self, text, val, var, obj):
        self.var = var
        self.obj = obj
        if val != 3:
            ttk.Radiobutton(
                self.obj.frame_menu,
                text=text,
                variable=self.var,
                value=val,
                command=self.change).pack(anchor=SW, fill=NONE, padx=10, pady=10)
        else:
            ttk.Radiobutton(
                self.obj.frame_menu,
                text=text,
                variable=self.var,
                value=val,
                command=self.change)

    def change(self):
        self.obj.next_frame(self.var.get())

    # def find_with_name(self, name):
    #     self.parser.find_with_name('show all')


if __name__ == "__main__":
    app = App()

    app.mainloop()
