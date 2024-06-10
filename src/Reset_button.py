import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sql
import math
import sys

class Reset_button(tk.Frame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.button = tk.Button(self,text="最初から",command=self.reset_button_pushed)
		self.button.pack(padx=4,pady=4)

	def reset_button_pushed(self):
		self.master.reset()