from tkinter import *
from tkinter import ttk

def make_add_record_window(root):
	tabControl = ttk.Notebook(root)
	root.geometry('1100x1100')
	root.iconbitmap('logo.ico')
	#1.病案首页
	front_page = ttk.Frame(tabControl)
	tabControl.add(front_page, text='病案首页')
	tabControl.pack(expand=1, fill='both')
	scroll = ttk.Scrollbar(front_page)
	scroll.grid(sticky="nse")

	#2.患者基本信息
	basic_info = ttk.Frame(tabControl)
	tabControl.add(basic_info, text='患者基本信息')
	tabControl.pack(expand=1, fill='both')
	
	#3.脑电图
	eeg = ttk.Frame(tabControl)
	tabControl.add(eeg, text='脑电图')
	tabControl.pack(expand=1, fill='both')
	
	#4.监护室临床数据、血流动力学、NIRS和TCD(1)
	icu1 = ttk.Frame(tabControl)
	tabControl.add(icu1, text='监护室临床数据、血流动力学、NIRS和TCD - 1')
	tabControl.pack(expand=1, fill='both')
	
	#5.监护室临床数据、血流动力学、NIRS和TCD(2)
	icu2 = ttk.Frame(tabControl)
	tabControl.add(icu2, text='监护室临床数据、血流动力学、NIRS和TCD - 2')
	tabControl.pack(expand=1, fill='both')
	
	#6.听诱发电位
	eps = ttk.Frame(tabControl)
	tabControl.add(eps, text='听诱发电位')
	tabControl.pack(expand=1, fill='both')
	
	#7.MRI检查
	mri = ttk.Frame(tabControl)
	tabControl.add(mri, text='MRI检查')
	tabControl.pack(expand=1, fill='both')
	
	#8.粪便样本化验
	sample = ttk.Frame(tabControl)
	tabControl.add(sample, text='粪便样本化验')
	tabControl.pack(expand=1, fill='both')
	
	#9.神经发育评估
	nerve = ttk.Frame(tabControl)
	tabControl.add(nerve, text='神经发育评估')
	tabControl.pack(expand=1, fill='both')
	
	#10.问卷
	questionaire = ttk.Frame(tabControl)
	tabControl.add(questionaire, text='问卷')
	tabControl.pack(expand=1, fill='both')
	
	#11.神经科复查追踪
	nerve_tracing = ttk.Frame(tabControl)
	tabControl.add(nerve_tracing, text='神经科复查追踪')
	tabControl.pack(expand=1, fill='both')