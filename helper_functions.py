from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import first_page
import second_page
from first_page import entry_array
import tkinter as tk


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


def add_record_to_db():
    global entry_array
    organization_entry = entry_array['organization']
    organization_entry_value = organization_entry.get()
    print(organization_entry_value)


def make_add_record_window(root):
    global organization_entry
    root.geometry('1400x1600')
    root.iconbitmap('logo.ico')
    notebook = Notebook(root,
                        ['病案首页', '患者基本信息', '脑电图', '监护室临床数据、血流动力学、NIRS和TCD - 1', '监护室临床数据、血流动力学、NIRS和TCD - 2', '听诱发电位',
                         'MRI检查', '粪便样本化验', '神经发育评估', '问卷', '神经科复查追踪'])
    notebook.pack(expand=1, fill='both')
    # notebook.grid(row=0, column=0, sticky='nsew')
    # tabControl = ttk.Notebook(root)

    # 1.病案首页
    page_1 = notebook.tab('病案首页')
    row = first_page.FirstPage(page_1)
    button_save = Button(page_1, text="Save Record", command=add_record_to_db, padx=36, pady=20, bg='grey').grid(
        row=row + 1)

    # #2.患者基本信息
    page_2 = notebook.tab('患者基本信息')
    row = second_page.SecondPage(page_2)



#
# #3.脑电图
# eeg = ttk.Frame(tabControl)
# tabControl.add(eeg, text='脑电图')
# tabControl.pack(expand=1, fill='both')
#
# #4.监护室临床数据、血流动力学、NIRS和TCD(1)
# icu1 = ttk.Frame(tabControl)
# tabControl.add(icu1, text='监护室临床数据、血流动力学、NIRS和TCD - 1')
# tabControl.pack(expand=1, fill='both')
#
# #5.监护室临床数据、血流动力学、NIRS和TCD(2)
# icu2 = ttk.Frame(tabControl)
# tabControl.add(icu2, text='监护室临床数据、血流动力学、NIRS和TCD - 2')
# tabControl.pack(expand=1, fill='both')
#
# #6.听诱发电位
# eps = ttk.Frame(tabControl)
# tabControl.add(eps, text='听诱发电位')
# tabControl.pack(expand=1, fill='both')
#
# #7.MRI检查
# mri = ttk.Frame(tabControl)
# tabControl.add(mri, text='MRI检查')
# tabControl.pack(expand=1, fill='both')
#
# #8.粪便样本化验
# sample = ttk.Frame(tabControl)
# tabControl.add(sample, text='粪便样本化验')
# tabControl.pack(expand=1, fill='both')
#
# #9.神经发育评估
# nerve = ttk.Frame(tabControl)
# tabControl.add(nerve, text='神经发育评估')
# tabControl.pack(expand=1, fill='both')
#
# #10.问卷
# questionaire = ttk.Frame(tabControl)
# tabControl.add(questionaire, text='问卷')
# tabControl.pack(expand=1, fill='both')
#
# #11.神经科复查追踪
# nerve_tracing = ttk.Frame(tabControl)
# tabControl.add(nerve_tracing, text='神经科复查追踪')
# tabControl.pack(expand=1, fill='both')
