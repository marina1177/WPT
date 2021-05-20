import ctypes
from tkinter import *
from matplotlib.backends._backend_tk import NavigationToolbar2Tk

from matplotlib.backends.backend_tkagg import (
	FigureCanvasTkAgg)
from matplotlib.figure import Figure
from numpy.ctypeslib import ndpointer
from logic import *

# Init ctypes types
DOUBLE = ctypes.c_double
PDOUBLE = ctypes.POINTER(DOUBLE)
PPDOUBLE = ctypes.POINTER(PDOUBLE)
PPPDOUBLE = ctypes.POINTER(PPDOUBLE)


def convert_float(val):
	try:
		return float(val)
	except ValueError:
		return 0.0


def getKPD(c, r1):
	kpdArr = []
	for j in range(0, w + 1):
		kpd = 0
		for p in range(0, 2 * j + 1):
			for h in range(0, 2 * j + 1):
				kpd = (kpd + r1[p, h] * r1[p, h] / (10.5 + 12 * 1.5 * c * c))
				kpdArr.append((kpd))
	return kpdArr


fields = ctypes.CDLL("./libfields.so")
c_power_fun = fields.calculate_fields
c_kpd_fun = fields.calculate_kpd

c_power_fun.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
                        ctypes.c_float, np.ctypeslib.ndpointer(dtype=np.float64,
                                                               ndim=2,
                                                               flags='C_CONTIGUOUS')
                        ]

c_kpd_fun.argtypes = [ctypes.c_float,
                      np.ctypeslib.ndpointer(dtype=np.float64,
                                             ndim=2,
                                             flags='C_CONTIGUOUS'),
                      # POINTER(ctypes.c_double)
                      np.ctypeslib.ndpointer(dtype=np.float64,
                                             ndim=1,
                                             flags='C_CONTIGUOUS'),
                      ]

c_power_fun.restype = None
c_kpd_fun.restype = None

r1 = np.meshgrid(np.linspace(0, 1, 2 * w + 1), np.linspace(0, 1, 2 * w + 1))[0]
kpdArray = np.array(range(w + 1), dtype=np.float64)


def calculate():
	print("result")

	c_power_fun(convert_float(var1_text.get()),
	            convert_float(var2_text.get()),
	            convert_float(var3_text.get()),
	            convert_float(var4_text.get()),
	            convert_float(var5_text.get()),
	            convert_float(var6_text.get()),
	            r1)

	# r2 = np.meshgrid(np.linspace(0, 1, 2 * w + 1), np.linspace(0, 1, 2 * w + 1))[0]
	c_kpd_fun(convert_float(var3_text.get()),
	          r1, kpdArray)

	# kpd = getKPD(convert_float(var3_text.get()), r1)

	power = []
	for p in range(0, w + 1):
		power.append(r1[p, 0] * r1[p, 0])

	# Plots
	# Power
	fig = Figure(figsize=(5, 4), dpi=100)
	t = np.arange(0, 151, 1)
	fig.add_subplot(111).plot(t, power)

	canvas = FigureCanvasTkAgg(fig, master=app)
	canvas.draw()
	canvas.get_tk_widget().grid(row=4, column=0, columnspan=3, sticky=W, pady=10, padx=10)

	# KPD
	fig_kpd = Figure(figsize=(5, 4), dpi=100)

	x = list(range(0, w+1))
	fig_kpd.add_subplot(111).plot(x, kpdArray)

	canvas = FigureCanvasTkAgg(fig_kpd, master=app)
	canvas.draw()
	canvas.get_tk_widget().grid(row=4, column=3, columnspan=3, sticky=W, pady=10, padx=10)


def clear_text():
	print("Clear")


# window object
app = Tk()
# app.columnconfigure(0, minsize=250)
# app.rowconfigure([0, 1], minsize=100)
# a
var1_text = StringVar()
var1_label = Label(app,
                   text='a\nширина модуля[м]',
                   fg="white",
                   background="#34A2FE",
                   width=14,
                   height=4,
                   font=('bold', 14))
var1_label.grid(row=0, column=0, sticky=E, pady=10, padx=10)

var1_entry = Entry(app, textvariable=var1_text)
var1_entry.grid(row=0, column=1, sticky=W, padx=10)

# b
var2_text = StringVar()
var2_label = Label(app, text='b\nдлина модуля[м]',
                   fg="white",
                   background="#34A2FE",
                   width=14,
                   height=4, font=('bold', 14))
var2_label.grid(row=0, column=2, sticky=E)
var2_entry = Entry(app, textvariable=var2_text)
var2_entry.grid(row=0, column=3, sticky=E, padx=10)

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
var3_entry.grid(row=1, column=1, sticky=W, padx=10)

# e
var4_text = StringVar()
var4_label = Label(app, text='e',
                   fg="white",
                   background="#34A2FE",
                   width=4,
                   height=2,
                   font=('bold', 14))
var4_label.grid(row=1, column=2, sticky=E)
var4_entry = Entry(app, textvariable=var4_text)
var4_entry.grid(row=1, column=3, sticky=E, padx=10)

# lambda
var5_text = StringVar()
var5_label = Label(app, text='λ\nдлина волны[м]',
                   fg="white",
                   background="#34A2FE",
                   width=14,
                   height=4,
                   font=('bold', 14))
var5_label.grid(row=2, column=0, sticky=E, pady=10, padx=10)
var5_entry = Entry(app, textvariable=var5_text)
var5_entry.grid(row=2, column=1, sticky=W, padx=10)

# D
var6_text = StringVar()
var6_label = Label(app, text='D\nрасстояние до приемника[м]',
                   fg="white",
                   background="#34A2FE",
                   width=22,
                   height=4,
                   font=('bold', 14))
var6_label.grid(row=2, column=2, sticky=E)
var6_entry = Entry(app, textvariable=var6_text)
var6_entry.grid(row=2, column=3, sticky=E, padx=10)

# Add Buttons
calc_btn = Button(app, text="Calculate", width=12, command=calculate)
calc_btn.grid(row=3, column=0, sticky=W, pady=10, padx=10)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=3, column=2, pady=20)

# normalize and convert to dB
dbnorm = lambda x: 20 * np.log10(np.abs(x) / np.max(x));

# generate example data
# some angles
alpha = np.arange(-90, 90, 0.01);
x = np.deg2rad(alpha)
dir_function = dbnorm(np.sinc(x))

# plot
# ax = pp.subplot(111, polar=True)
# # set zero north
# ax.set_theta_zero_location('N')
# ax.set_theta_direction('clockwise')
# pp.plot(np.deg2rad(alpha), dir_function)
# ax.set_ylim(-20,0)
# ax.set_yticks(np.array([-20, -12, -6, 0]))
# ax.set_xticks(np.array([0, -45, -90, np.nan, np.nan, np.nan, 90, 45])/180*np.pi)
# pp.show()

app.wm_title('WPT calculator')
app.geometry('1200x800')

# start programm
app.mainloop()
