import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sql
import math
import sys
import os

class Tempature_table(tk.Frame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		# self.tempature = tk.IntVar(value=1000)
		title_rows = (u"温度",u"数値１",u"数値２",u"数値３",u"数値４",u"数値５",u"数値６",u"数値７")
		clm = ["title","value1","value2","value3","value4","value5","value6","value7"]
		self.table_name_list = {
			0.5:"TEMPATURE05",
			0.8:"TEMPATURE08",
			1.0:"TEMPATURE",
			1.2:"TEMPATURE12",
			2.0:"TEMPATURE20",
			2.5:"TEMPATURE25",
			3.0:"TEMPATURE30"
		}
		self.current_tempature_table = ttk.Treeview(
			self,
			columns=clm,
			height=2,
			show="headings",
			selectmode="none"
			)
		for i in range(8):
			self.current_tempature_table.heading(clm[i],text=title_rows[i])
			
		self.current_tempature_table.column("#0",width=0)
		for cl in clm:
			self.current_tempature_table.column(cl,anchor="center",width=48)
		self.current_tempature_table.pack(padx=4,pady=4)
		self.iid1 = self.current_tempature_table.insert(parent="",index="end",values=self.get_value_fromdb())
		self.iid2 = self.current_tempature_table.insert(parent="",index="end",values=self.get_value_fromdb(tmp=0))

	def get_value_fromdb(self,tp="",tmp=1000,focus=1.0,m_focus=1.0):
		table_name = self.table_name_list[focus]
		# データベースへ接続
		dbname = "../db/tempature.db"
		db_path = os.path.join(os.path.dirname(__file__), '..', 'db', dbname)
		conn = sql.connect(db_path)
		cur = conn.cursor()
		if tp == "":
			tp = str(tmp)
		top = (tp,)
		cur.execute("select V1,V2,V3,V4,V5,V6,V7 from {} where TMP = {}".format(table_name,tmp))
		res_from_table = cur.fetchone()
		smith_damage = tuple(math.floor(m_focus * num)for num in res_from_table)
		result = top + smith_damage
		cur.close()
		conn.close()
		return result
	
	def set_tempature_table(self,focus=1.0):
		mtype = self.master.material_type.get()
		tm = self.master.tempature.get()

		# 倍半（material_type = 1)なら倍半処理、そうでないなら通常倍率を１列目に
		if((mtype == 1)&(tm % 200 == 0)):
			if(tm % 400 == 0):
				self.current_tempature_table.item(self.iid1,values=self.get_value_fromdb(tmp=tm,focus=focus,m_focus=2.0))
			elif(tm % 400 == 200):
				self.current_tempature_table.item(self.iid1,values=self.get_value_fromdb(tmp=tm,focus=focus,m_focus=0.5))
		else:	
			self.current_tempature_table.item(self.iid1,values=self.get_value_fromdb(tmp=tm,focus=focus))

		# 光地金で200の倍数のみ二列目に値を挿入
		if((mtype == 2)&(tm % 200 == 0)):
			self.current_tempature_table.item(self.iid2,values=self.get_value_fromdb(tp="光部分",tmp=tm,focus=focus,m_focus=2.0))
		elif((mtype == 1)&(tm == 1000)):
			self.current_tempature_table.item(self.iid2,values=self.get_value_fromdb(tp="1T目",tmp=tm,focus=1.0))
		else:
			self.current_tempature_table.item(self.iid2,values=self.get_value_fromdb(tmp=0))