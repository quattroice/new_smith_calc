import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sql
import math
import sys
import os

class Material_state(tk.Frame):
    def __init__(self,master=None,**kwargs):
        super().__init__(master, **kwargs)
        # 数値の設定
        self.damage = tk.StringVar(value=0)
        self.min_damage = tk.IntVar(value=0)
        self.max_damage = tk.IntVar(value=0)
        self.delta_damage = tk.IntVar(value=0)
        # 入力バーの作成
        self.entry = tk.Entry(self,width=8,state="disable",textvariable=self.damage)
        self.entry.grid(row=0,column=0,sticky="nsew",columnspan=2)
        self.entry.bind("<KeyRelease>",self.entry_bg)
        self.entry.insert(0,0)
        # 最大値との差分ラベルの作成
        self.delta_label = tk.Label(self,width=8,text=self.delta_damage.get(),anchor="center",relief="solid",bd=1)
        self.delta_label.grid(row=1,column=0,sticky="nsew",columnspan=2)
        # 数値ラベルの作成
        self.label_min = tk.Label(self,width=4,text=self.min_damage.get(),anchor="center",relief="solid",bd=1)
        self.label_min.grid(row=2,column=0,sticky="nsew")
        self.label_max = tk.Label(self,width=4,text=self.max_damage.get(),anchor="center",relief="solid",bd=1)
        self.label_max.grid(row=2,column=1,sticky="nsew")

    def ms_reset(self):
        self.damage.set(0)
        self.delta_damage.set(self.max_damage.get())
        self.configures()

    def entry_bg(self,event):
        dm = self.get_damage()
        self.delta_damage.set(self.max_damage.get() - self.get_damage())
        self.delta_label.configure(text=self.delta_damage.get())    
        if((self.min_damage.get() <= dm)&(self.max_damage.get() >= dm)):
            self.entry.config(background="lightskyblue")
        elif(self.max_damage.get() <= dm):
            self.entry.config(background="red")
        else:
            self.entry.config(background="white")

    def set_num(self,number,iname):
        # データベースへ接続
        dbname = "../db/tempature.db"
        db_path = os.path.join(os.path.dirname(__file__), '..', 'db', dbname)
        conn = sql.connect(db_path)
        cur = conn.cursor()
        try:
            query = f"select MIN{number}, MAX{number} from ITEMLIST where ITEMNAME = ?"
            cur.execute(query, (iname,))
            res_from_table = cur.fetchone()
            if res_from_table:
                self.min_damage.set(res_from_table[0])
                self.max_damage.set(res_from_table[1])
                self.delta_damage.set(self.max_damage.get() - self.get_damage())
                self.configures()
                if self.max_damage.get() != 0:
                    self.entry.configure(state="normal")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            conn.close()

    def get_damage(self):
        try:
            dm = int(self.damage.get())
        except ValueError:
            dm = 0
        return dm
    
    def configures(self):
        self.label_min.configure(text=self.min_damage.get())
        self.label_max.configure(text=self.max_damage.get())
        self.delta_label.configure(text=self.delta_damage.get())