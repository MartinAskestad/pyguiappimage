#!/usr/bin/env python3

from tkinter import Tk, DoubleVar
from tkinter.ttk import Button, Entry, Label
from pyguiapp.convert import to_celsius

class GuiApp(Tk):
	def __init__(self):
		super().__init__()

		self.title("Unit convert")
		
		fahrenheit_label = Label(self, text="Fahrenheit")
		fahrenheit_label.grid(row=0, column=0)

		self.fahrenheit = DoubleVar(name="fahrenheit")

		fahrenheit_entry = Entry(self, textvariable=self.fahrenheit)
		fahrenheit_entry.grid(row=0, column=1)

		convert_button = Button(self, text="To Celsius",
					command=self.on_convert_click)
		convert_button.grid(row=1, column=2)

		self.celsius = DoubleVar(name="celsius")
		celsius_label = Label(self, textvariable=self.celsius)
		celsius_label.grid(row=2, column=0, columnspan=3)

	def on_convert_click(self):
		f = self.fahrenheit.get()
		c = to_celsius(f)
		self.celsius.set(c)

if __name__ == "__main__":
	app = GuiApp()
	app.mainloop()
