from tkinter import ttk
from first_page import FirstPage
from second_page import SecondPage
from first_page import tab1_values
from second_page import tab2_values
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from db_utils import *

root = Tk()
root.title('Database')
root.geometry('500x500')
root.iconbitmap('logo.ico')
root.configure(bg="white")

DATABASE_ = None
db_files = (('Database Files', '*.db'),)


def _check_db():
    if DATABASE_ is None:
        messagebox.showwarning(message='Please create / connect to a database')
        return False
    else:
        return True


def create_db():
    global DATABASE_
    try:
        f = filedialog.asksaveasfile(initialdir="C:\\", title='New', filetypes=db_files, defaultextension=db_files)
        if not f: return
        conn = sqlite3.connect(f.name)
        cur = conn.cursor()
        cur.execute('select 1')  # TODO: generate correct SQL to create the tables
        conn.commit()
        conn.close()
        DATABASE_ = f.name
        messagebox.showinfo(message='Database has been created and connected')
    except Exception as e:
        DATABASE_ = None
        raise e


def connect_db():
    global DATABASE_
    try:
        f = filedialog.askopenfilename(initialdir="C:\\", title='Connect to database', filetypes=db_files,
                                       defaultextension=db_files)
        if not f: return
        conn = sqlite3.connect(f)
        cur = conn.cursor()
        cur.execute('select 1')
        conn.close()
        DATABASE_ = f
        messagebox.showinfo(message='Connection success')
    except Exception as e:
        DATABASE_ = None
        raise e


def create():
    if not _check_db(): return
    # open a new window with tabs for entering new data
    new_record_win = Toplevel(root)
    new_record_win.title('New record')
    make_add_record_window(new_record_win)
    # insert record into db after use completes input
    conn = sqlite3.connect(DATABASE_)
    cursor = conn.cursor()
    cursor.execute('select 1')  # TODO: generate insert
    conn.commit()
    cursor.close()


def search():
    if not _check_db(): return
    new_record_win = Toplevel(root)
    new_record_win.title('Search a record')
    make_add_record_window(new_record_win)
    # based on input from user, search for existing records and output results to excel
    conn = sqlite3.connect(DATABASE_)
    cursor = conn.cursor()
    res = cursor.execute('select 1').fetchall()  # TODO: generate select
    # output to excel
    cursor.close()


def exit():
    message = messagebox.askquestion(message='Are you sure to exit？')
    if message == 'yes':
        DATABASE_ = None
        root.destroy()


class YScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.canvas = canvas = tk.Canvas(self, relief='raised')
        canvas.grid(row=0, column=0, sticky='nsew')

        scroll = tk.Scrollbar(self, command=canvas.yview, orient=tk.VERTICAL)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky='nsew')

        self.content = tk.Frame(canvas)
        self.canvas.create_window(0, 0, window=self.content, anchor="nw")

        self.bind('<Configure>', self.on_configure)

    def on_configure(self, event):
        bbox = self.content.bbox('ALL')
        self.canvas.config(scrollregion=bbox)


class Notebook(ttk.Notebook):
    def __init__(self, parent, tab_labels):
        super().__init__(parent)

        self._tab = {}
        for text in tab_labels:
            self._tab[text] = YScrolledFrame(self)
            # layout by .add defaults to fill=tk.BOTH, expand=True
            self.add(self._tab[text], text=text, compound=tk.TOP)

    def tab(self, key):
        return self._tab[key].content


def parse_values(tab_values):
    tab_keys = tab_values.keys()
    tab_values_array = []
    tab_keys_array = []
    tab_question_mark_str = ''
    tab_sub_sql = ''
    for idx, key in enumerate(tab_keys):
        value = tab_values[key].get()
        tab_values_array.append(value)
        tab_keys_array.append(key)
        if idx == len(tab_keys) - 1:
            tab_sub_sql = tab_sub_sql + key + ' text '
            tab_question_mark_str = tab_question_mark_str + '?'
        else:
            tab_sub_sql = tab_sub_sql + key + ' text, '
            tab_question_mark_str = tab_question_mark_str + '?,'
    return tab_sub_sql, tab_values_array, tab_keys_array, tab_question_mark_str


def add_record_to_db():

    tab1_sub_sql, tab1_values_array, tab1_keys_array, tab1_question_mark_str = parse_values(tab1_values)
    tab2_sub_sql, tab2_values_array, tab2_keys_array, tab2_question_mark_str = parse_values(tab2_values)

    sql_tab1_create_table = """CREATE TABLE IF NOT EXISTS """ + """ tab1 (
                                            id integer PRIMARY KEY, """ + tab1_sub_sql + """
                                        );"""

    sql_tab2_create_table = """CREATE TABLE IF NOT EXISTS """ + """ tab2 (
                                                id integer PRIMARY KEY, """ + tab2_sub_sql + """
                                            );"""
    database = DATABASE_
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_tab1_create_table)
        create_table(conn, sql_tab2_create_table)

    else:
        print("Error! cannot create the database connection.")

    with conn:
        tab1_val = tuple(tab1_values_array)
        tab1_sql = ''' INSERT INTO ''' + '''tab1''' + str(tuple(tab1_keys_array)) + '''
                      VALUES(''' + tab1_question_mark_str + ''') '''
        insert_id = insert_db(conn, tab1_val, tab1_sql)

        tab2_val = tuple(tab2_values_array)
        tab2_sql = ''' INSERT INTO ''' + '''tab2''' + str(tuple(tab2_keys_array)) + '''
                              VALUES(''' + tab2_question_mark_str + ''') '''
        insert_id = insert_db(conn, tab2_val, tab2_sql)
        messagebox.showinfo(message='DB Successfully Inserted')

def make_add_record_window(root):
    root.geometry('1400x1600')
    root.iconbitmap('logo.ico')
    notebook = Notebook(root,
                        ['病案首页', '患者基本信息', '脑电图', '监护室临床数据、血流动力学、NIRS和TCD - 1', '监护室临床数据、血流动力学、NIRS和TCD - 2', '听诱发电位',
                         'MRI检查', '粪便样本化验', '神经发育评估', '问卷', '神经科复查追踪'])
    notebook.pack(expand=1, fill='both')

    # 1.病案首页
    page_1 = notebook.tab('病案首页')
    row = FirstPage(page_1)
    button_save = Button(page_1, text="Save Record", command=add_record_to_db, padx=36, pady=20, bg='grey').grid(
        row=row + 1)

    # #2.患者基本信息
    page_2 = notebook.tab('患者基本信息')
    row = SecondPage(page_2)


def main():
    new_db_btn = Button(root, text='Create new database', command=create_db, padx=36, pady=20, bg='grey').place(
        relx=0.5, rely=0.1, anchor=CENTER)
    conn_db_btn = Button(root, text='Connect to existing Database', command=connect_db, padx=30, pady=20,
                         bg='grey').place(relx=0.5, rely=0.3, anchor=CENTER)
    create_btn = Button(root, text='Enter new record', command=create, padx=30, pady=20, bg='grey').place(relx=0.5,
                                                                                                          rely=0.5,
                                                                                                          anchor=CENTER)
    search_btn = Button(root, text='Search in existing records', command=search, padx=24, pady=20, bg='grey').place(
        relx=0.5, rely=0.7, anchor=CENTER)
    exit_btn = Button(root, text='Exit', command=exit, padx=60, pady=16, bg='grey').place(relx=0.5, rely=0.9,
                                                                                          anchor=CENTER)
    root.mainloop()


if __name__ == '__main__':
    main()
