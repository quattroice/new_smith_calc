import tkinter as tk
import tkinter.ttk as ttk
import math
import sys

class Temp_button(tk.Frame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.button_minus_50 = tk.Button(self,text="たたく",command=lambda:self.temp_button_pushed(-50))
		self.button_minus_50.pack(side="top",anchor="nw",padx=4,pady=4)
		self.button_plus_300 = tk.Button(self,text="火力上げ",command=lambda:self.temp_button_pushed(300))
		self.button_plus_300.pack(side="top",anchor="nw",padx=4,pady=4)
		self.button_minus_300 = tk.Button(self,text="冷やし込み",command=lambda:self.temp_button_pushed(-300))
		self.button_minus_300.pack(side="top",anchor="nw",padx=4,pady=4)
		self.button_minus_150 = tk.Button(self,text="熱風おろし",command=lambda:self.temp_button_pushed(-150))
		self.button_minus_150.pack(side="top",anchor="nw",padx=4,pady=4)

	def temp_button_pushed(self,delta):
		self.master.tb_pushed(delta)