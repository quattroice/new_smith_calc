import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sql
import math
import sys

from Itemlist import Itemlist
from Material_state import Material_state
from Action_list import Action_list
from Tempature_table import Tempature_table
from Reset_button import Reset_button
from Temp_button import Temp_button

class App(tk.Tk):
	def __init__(self):
		# rootフレームの表
		super().__init__()
		self.title(u"鍛冶")
		self.itemname = tk.StringVar()
		self.tempature = tk.IntVar(value=1000)
		self.material_type = tk.IntVar(value=0)
		self.focus = tk.DoubleVar(value=1.0)

		# アイテムリストの表示
		self.itemlist = Itemlist(self,relief="solid",bd=1)
		self.itemlist.grid(row=0,column=0,padx=4,pady=4,sticky="w")

		# 素材状態の外枠
		self.frame_grid = tk.Frame(self,relief="solid",bd=1)
		self.frame_grid.grid(row=1,column=0,padx=4,pady=4,sticky="w")

		# 素材状態の表示4行2列
		self.msl = []
		for i in range(4):
			for j in range(2):
				ms = Material_state(self.frame_grid,relief="solid",bd=1)
				ms.grid(row=i,column=j,padx=4,pady=4)
				self.msl.append(ms)

		# 叩くリストの表示
		self.action_list = Action_list(self,relief="solid",bd=1)
		self.action_list.grid(row=2,column=0,columnspan=2,padx=4,pady=4,sticky="w")

		# 温度表の表示
		self.tempature_table = Tempature_table(self,relief="solid",bd=1)
		self.tempature_table.grid(row=3,column=0,columnspan=2,padx=4,pady=4)

		# リセットボタンの表示
		self.reset_button = Reset_button(self)
		self.reset_button.grid(row=0,column=1,padx=8,pady=4)

		# 温度操作ボタンの表示
		self.temp_button = Temp_button(self,relief="solid",bd=1)
		self.temp_button.grid(row=1,column=1,padx=8,pady=4)

	def set_itemname(self):
		for i in range(len(self.msl)):
			self.msl[i].set_num(i+1,self.itemname.get())
		self.tempature_table.set_tempature_table(focus=self.focus.get())

	def set_action(self,f):
		self.focus.set(f)
		self.tempature_table.set_tempature_table(focus=self.focus.get())

	def reset(self):
		self.tempature.set(1000)
		self.action_list.action_name.set("叩く")
		self.tempature_table.set_tempature_table(focus=1.0)
		for ms in self.msl:
			ms.ms_reset()

	def tb_pushed(self,d):
		bef = self.tempature.get()
		bef += d
		self.tempature.set(min(max(0,bef),3000))
		self.tempature_table.set_tempature_table(focus=self.focus.get())