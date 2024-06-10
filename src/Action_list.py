import tkinter as tk
import tkinter.ttk as ttk
import sys
import math

class Action_list(tk.Frame):
	def __init__(self,master=None,**kwargs):
		super().__init__(master,**kwargs)
		self.actions = {
			"叩く":1.0,
			"半分":0.5,
			"乱れうち":0.8,
			"強く":1.2,
			"2倍の力で":2.0,
			"熱風おろし":2.5,
			"3倍撃ち":3.0
			}
		self.action_name = tk.StringVar(value="叩く")
		self.action_pulldown = ttk.Combobox(self,state="readonly",height=7,value=list(self.actions.keys()),textvariable=self.action_name)
		self.action_pulldown.pack(padx=4,pady=4)
		self.action_pulldown.bind("<<ComboboxSelected>>",self.action_selected)

	def action_selected(self,event):
		self.master.set_action(self.actions[self.action_name.get()])