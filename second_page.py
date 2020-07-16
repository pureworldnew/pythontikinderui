from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import json

tab2_values = {}

def ele_row(elements, second_page):
    global tab2_values

    for ele in elements:
        if ele['type'] == 'label':
            if(ele['label'] == 'Main' or ele['label'] == 'Additional' or ele['label'] == 'Prior' or ele['label'] == 'After'):
                ttk.Label(second_page, text=ele['label'], foreground='blue',
                          font=('Times', '16', 'bold italic')).grid(row=ele['row'])
            else:
                ttk.Label(second_page, text=ele['label'], foreground='blue',
                                         font=('Times', '24', 'bold italic')).grid(row=ele['row'])
        else:
            label = ttk.Label(second_page, text=ele['label']).grid(row=ele['row'], column=ele['column'], sticky=W,
                                                                  padx=20, pady=10)
            if ele['type'] == 'input':
                entry = ttk.Entry(second_page)
                entry.grid(row=ele['row'], column=ele['column']+ele['col_gap'], sticky=W, padx=20)
                tab2_values[ele['id']] = entry
            elif ele['type'] == 'select':
                OPTIONS = []
                for d in range(0, 10):
                    OPTIONS.append(d)
                variable = StringVar(second_page)
                variable.set(OPTIONS[0])  # default value
                entry = ttk.OptionMenu(second_page, variable, *OPTIONS)
                entry.grid(row=ele['row'], column=ele['column']+ele['col_gap'])
                tab2_values[ele['id']] = variable
            elif ele['type'] == 'datetime':
                entry = DateEntry(second_page)
                entry.grid(row=ele['row'], column=ele['column']+ele['col_gap'], sticky=W)
            # elif ele['type'] == 'checkbutton':
            #     var1 = IntVar()
            #     entry = Checkbutton(second_page, text="M", variable=var1)
            #     entry.grid(row=ele['row'], column=ele['column']+ele['col_gap'], sticky=W)
            #     var2 = IntVar()
            #     entry = Checkbutton(second_page, text="F", variable=var2)
            #     entry.grid(row=ele['row'], column=ele['column']+ele['col_gap'], sticky=W, columnspan=2)


def SecondPage(second_page):
    row = 1
    f = open('json/second_page.json', )
    elements = json.load(f)
    f.close()

    ele_row(second_page=second_page, elements=elements)
    row = row + 60
    return row
