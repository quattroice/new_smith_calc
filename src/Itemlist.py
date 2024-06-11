import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sql
import math
import sys
import os

class Itemlist(tk.Frame):
	def set_itemname_list(self):
		# データベースへ接続
		dbname = "../db/tempature.db"
		db_path = os.path.join(os.path.dirname(__file__), '..', 'db', dbname)
		conn = sql.connect(db_path)
		cur = conn.cursor()

		# アイテム一覧を取得してデータベースとのアクセスを閉じる
		res = []
		try:
			cur.execute("select ITEMNAME from ITEMLIST")
			res_from_table = cur.fetchall()
			if res_from_table:
				for tupl in res_from_table:
					res.append(tupl[0])	
		except Exception as e:
			print(f"Error: {e}")
		finally:
			cur.close()
			conn.close()
		return res
	
	def get_material_type(self):
		# データベースへ接続
		dbname = "../db/tempature.db"
		db_path = os.path.join(os.path.dirname(__file__), '..', 'db', dbname)
		conn = sql.connect(db_path)
		cur = conn.cursor()

		# アイテム一覧を取得してデータベースとのアクセスを閉じる
		res = 0
		try:
			cur.execute("select MATERIAL_TYPE from ITEMLIST where ITEMNAME = \"{}\"".format(self.master.itemname.get()))
			res_from_table = cur.fetchone()
			if res_from_table:
				res = res_from_table[0]
		except Exception as e:
			print(f"Error: {e}")
		finally:
			cur.close()
			conn.close()
		return res
	
	def itemname_list_selected(self,event):
		self.master.material_type.set(self.get_material_type())
		self.master.set_itemname()

	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.itemname_list = self.set_itemname_list()
		self.itemlist_pulldown = ttk.Combobox(self,height=10,state="readonly",values=self.itemname_list,textvariable=self.master.itemname)
		self.itemlist_pulldown.bind('<<ComboboxSelected>>',self.itemname_list_selected)
		self.itemlist_pulldown.pack(padx=4,pady=4)
			