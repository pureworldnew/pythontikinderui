import os
import sqlite3
from tkinter import *
from tkinter import filedialog, messagebox

from helper_functions import make_add_record_window
from sql_queries import *

root = Tk()
root.title('Database')
root.geometry('500x500')
root.iconbitmap('logo.ico')
root.configure(bg="white")

DATABASE_ = None
dbfiles = (('Database Files', '*.db'),)

def _check_db():
	if DATABASE_ is None:
		messagebox.showwarning(message='Please create / connect to a database')
		return False
	else:
		return True

def create_db():
	global DATABASE_
	try:
		f = filedialog.asksaveasfile(initialdir="C:\\", title='New', filetypes = dbfiles, defaultextension=dbfiles)
		if not f: return
		conn = sqlite3.connect(f.name)
		cur = conn.cursor()
		cur.execute('select 1') # TODO: generate correct SQL to create the tables
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
		f = filedialog.askopenfilename(initialdir="C:\\", title='Connect to database', filetypes=dbfiles, defaultextension=dbfiles)
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
	cursor.execute('select 1') # TODO: generate insert
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
	res = cursor.execute('select 1').fetchall() # TODO: generate select
	# output to excel
	cursor.close()

def exit():
	message = messagebox.askquestion(message='Are you sure to exit？')
	if message == 'yes':
		DATABASE_ = None
		root.destroy()

new_db_btn = Button(root, text='Create new database', command=create_db, padx=36, pady=20, bg='grey').place(relx = 0.5, rely = 0.1, anchor = CENTER)
conn_db_btn = Button(root, text='Connect to existing Database', command=connect_db, padx=30, pady=20,bg='grey').place(relx=0.5, rely=0.3, anchor = CENTER)
create_btn = Button(root, text='Enter new record', command=create, padx=30, pady=20,bg='grey').place(relx = 0.5, rely = 0.5, anchor = CENTER)
search_btn = Button(root, text='Search in existing records', command=search, padx=24, pady=20,bg='grey').place(relx = 0.5, rely = 0.7, anchor = CENTER)
exit_btn = Button(root, text='Exit', command=exit, padx=60, pady=16,bg='grey').place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()