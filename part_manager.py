from tkinter import *
import ctypes
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from logic import *

fields = ctypes.CDLL("./libfields.so")
fields.calculate_kpd.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                 ctypes.c_float, ctypes.POINTER(ctypes.POINTER(ctypes.c_double))]
fields.calculate_kpd.restype = None #ctypes.POINTER(ctypes.c_double)


# array_2d_double = npct.ndpointer(dtype=np.double,ndim=2, flags='CONTIGUOUS')
# fields = npct.load_library("libfields.so", "./")
fields.calculate_kpd.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                 ctypes.c_float]
fields.calculate_kpd.restype = None

r1 = np.zeros(shape=(2*w+1,2*w+1)).astype(np.double)

def getKPD(c, r1):
	for j in range(0, 2 * w + 1):
		kpd = 0
		for p in range(0, 2 * j + 1):
			for h in range(0, 2 * j + 1):
				kpd = (kpd + r1[p, h] * r1[p, h] / (10.5 + 12 * 1.5 * c * c))


def calculate():
	print("result")
	if len(var1_text.get()) != 0 or len(var2_text.get()) != 0 or len(var3_text.get()) != 0 or len(
			var4_text.get()) != 0 or len(var5_text.get()) != 0 or len(var6_text.get()) != 0:
				r1= fields.calculate_kpd(float(var1_text.get()), float(var2_text.get()), float(var3_text.get()),
		                           float(var4_text.get()), float(var5_text.get()), float(var6_text.get()))

				for i in range(len(r1)):
					print('r1_')
				# kpd = getKPD(float(var3_text.get()),r1)
				# print("from manager: " + str(kpd))

		# kpd = fields.calculate_kpd(float(var1_text.get()), float(var2_text.get()), float(var3_text.get()),
		#                            float(var4_text.get()), float(var5_text.get()), float(var6_text.get()))
		# r1 = WPT(float(var1_text.get()), float(var2_text.get()), float(var3_text.get()),
		#                    float(var4_text.get()), float(var5_text.get()), float(var6_text.get())).calc_fields()


def clear_text():
	print("Clear")


# window object
app = Tk()
# app.columnconfigure(0, minsize=250)
# app.rowconfigure([0, 1], minsize=100)
# a
var1_text = StringVar()
var1_label = Label(app,
                   text='a',
                   fg="white",
                   background="#34A2FE",
                   width=4,
                   height=2,
font = ('bold', 14))
var1_label.grid(row=0, column=0, sticky=E, pady=10, padx=10)

var1_entry = Entry(app, textvariable=var1_text)
var1_entry.grid(row=0, column=1, sticky=W, padx=10)

# b
var2_text = StringVar()
var2_label = Label(app, text='b',
                   fg="white",
                   background="#34A2FE",
                   width=4,
                   height=2, font=('bold', 14))
var2_label.grid(row=0, column=2, sticky=E)
var2_entry = Entry(app, textvariable=var2_text)
var2_entry.grid(row=0, column=3,sticky=E, padx=10)

# c
var3_text = StringVar()
var3_label = Label(app, text='c',
                   fg="white",
                   background="#34A2FE",
                   width=4,
                   height=2,
                   font=('bold', 14))
var3_label.grid(row=1, column=0, sticky=E, pady=10, padx=10)
var3_entry = Entry(app, textvariable=var3_text)
var3_entry.grid(row=1, column=1,sticky=W, padx=10)

# e
var4_text = StringVar()
var4_label = Label(app, text='e',
                   fg="white",
                   background="#34A2FE",
                   width=4,
                   height=2,
                   font=('bold', 14))
var4_label.grid(row=1, column=2, sticky=E)
var4_entry = Entry(app,textvariable=var4_text)
var4_entry.grid(row=1, column=3,sticky=E, padx=10)

# lambda
var5_text = StringVar()
var5_label = Label(app, text='λ',
                   fg="white",
                   background="#34A2FE",
                   width=4,
                   height=2,
                   font=('bold', 14))
var5_label.grid(row=2, column=0, sticky=E, pady=10, padx=10)
var5_entry = Entry(app, textvariable=var5_text)
var5_entry.grid(row=2, column=1,sticky=W,padx=10)

# D
var6_text = StringVar()
var6_label = Label(app, text='D',
                   fg="white",
                   background="#34A2FE",
                   width=4,
                   height=2,
                   font=('bold', 14))
var6_label.grid(row=2, column=2, sticky=E)
var6_entry = Entry(app, textvariable=var6_text)
var6_entry.grid(row=2, column=3, sticky=E, padx=10)

# Add Buttons
calc_btn = Button(app, text="Calculate", width=12, command=calculate)
calc_btn.grid(row=3, column=0, sticky=W, pady=10, padx=10)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=3, column=2, pady=20)


# Plot
fig = Figure(figsize=(5, 4))

t = np.arange(0, 3, .01)
fig.add_subplot(111)
	#.plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg( master=app)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().grid(row=4, column=0,columnspan=3, sticky=W, pady=10, padx=10)


app.wm_title('WPT calculator')
app.geometry('1000x800')


# start programm
app.mainloop()
