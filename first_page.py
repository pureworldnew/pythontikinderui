from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import json

tab1_values = {}


def ele_row(elements, front_page):
    global tab1_values

    for ele in elements:
        if ele['type'] == 'label':
            if (ele['label'] == 'Main' or ele['label'] == 'Additional' or ele['label'] == 'Prior' or "After" == ele['label']):
                ttk.Label(front_page, text=ele['label'], foreground='blue',
                          font=('Times', '16', 'bold italic')).grid(row=ele['row'])
            else:
                ttk.Label(front_page, text=ele['label'], foreground='blue',
                          font=('Times', '24', 'bold italic')).grid(row=ele['row'])
        else:
            label = ttk.Label(front_page, text=ele['label']).grid(row=ele['row'], column=ele['column'], sticky=W,
                                                                  padx=20, pady=10)
            if ele['type'] == 'input':
                entry = ttk.Entry(front_page)
                entry.grid(row=ele['row'], column=ele['column'] + ele['col_gap'], sticky=W, padx=20)
                tab1_values[ele['id']] = entry
            elif ele['type'] == 'select':
                OPTIONS = []
                for d in range(0, 10):
                    OPTIONS.append(d)
                variable = StringVar(front_page)
                variable.set(OPTIONS[0])  # default value
                entry = ttk.OptionMenu(front_page, variable, *OPTIONS)
                entry.grid(row=ele['row'], column=ele['column'] + ele['col_gap'])
                tab1_values[ele['id']] = variable
            elif ele['type'] == 'datetime':
                entry = DateEntry(front_page)
                entry.grid(row=ele['row'], column=ele['column'] + ele['col_gap'], sticky=W)
            # elif ele['type'] == 'checkbutton':
            #     var1 = IntVar()
            #     entry = Checkbutton(front_page, text="M", variable=var1)
            #     entry.grid(row=ele['row'], column=ele['column']+ele['col_gap'], sticky=W)
            #     var2 = IntVar()
            #     entry = Checkbutton(front_page, text="F", variable=var2)
            #     entry.grid(row=ele['row'], column=ele['column']+ele['col_gap'], sticky=W, columnspan=2)



def FirstPage(front_page):
    row = 1
    f = open('json/first_page.json', )
    elements = json.load(f)
    f.close()

    ele_row(front_page=front_page, elements=elements)
    row = row + 60
    return row
