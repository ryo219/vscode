import tkinter as tk
import math             #三角等の数式を用いる際に要る module　　針の位置算出に使う
import time             #時間情報扱うのに要る module　　現在の時間取得に使う



class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)



## キャンバスの作成
        self.size = 500
        self.clock = tk.Canvas(self,width=self.size, height=self.size, background="white")
        self.clock.grid(row=0, column=0)
        self.clock.create_oval(5,5,495,495, width=5)


## キャンバス上に文字盤の描写
        for number in range(1,12+1):
            x = self.size/2 + math.cos(math.radians(number*360/12-90))*self.size/2*0.85
            y = self.size/2 + math.sin(math.radians(number*360/12-90))*self.size/2*0.85
                # 第一項　: キャンバスの左端⇒中央に中心を移動
                # 第二項　: 文字ごとに角度をずらしてる. (size/2)*0.85が半径, 0.85はキャンバス端に乗らないための調整.　右手方向が θ=0, 時計周り方向が θ>0 なため,「1」は θ=-60 #
            self.clock.create_text(x,y,text=str(number), fill="black", font=("",20))
                # 文字盤の描写

## 日付表示on/off, 秒針表示/非表示のボタン作成
        self.b = tk.Button(self,text="Show Date", font=("",20), command=self.dateflag)
                # ボタンの描写　　ボタン押すと dateflag関数 が呼び出される
        self.b.grid(row=1, column=0)
        self.c = tk.Button(self,text="Clear Second Hand", font=("",20), command=self.secflag)
                # ボタンの描写　　ボタン押すと secflag関数 が呼び出される
        self.c.grid(row=2, column=0)


## 経時確認などの動作用にインスタンス変数を用意
        self.sec = time.localtime().tm_sec      # localtime() : 現在の時刻を返す関数
        self.sec2 = time.localtime().tm_sec     # 時間の基準 (epoc) は UTC 時間で1970/01/01/00/00/00, 　time.gmtime(sec) は epocからsecだけ経過した時刻を出力
        self.min = time.localtime().tm_min      # time.localtime(sec) でepocからsecだけ経過した時刻をローカル時間に変換して出力,　()にすれば現在のローカル時刻
        self.hour = time.localtime().tm_hour    # ローカル時間 : 日本では Japan Standard Time,　local入れないと UTC で出力
        self.start = True
        self.show_date = False
        self.show_sec = False                        # 秒針表示のフラグ


## ボタンが押されたときの CallBack を用意
    def dateflag(self):                               #日付ボタン押されたとき
        if self.show_date:
            self.b.configure(text="show date")      #configure : テキストボックスの出力, 編集ができるコマンド
        else:
            self.b.configure(text="hide date")
        self.show_date = not self.show_date         # flagを反転

    def secflag(self):                                #秒針ボタン押されたとき
        if self.show_sec:
            self.c.configure(text="hide Second Hand")
        else:
            self.c.configure(text="show Second Hand")
        self.show_sec = not self.show_sec         # flagを反転



## 針の回転を描写
    def display(self):
        # 秒針の描写. 　最初(start==True)か秒が変わったときに作動
        if self.sec != time.localtime().tm_sec or self.start:
            self.sec = time.localtime().tm_sec
            angle = math.radians(self.sec*360/60-90)
            x0 = self.size/2                                        # 秒針の端点を時計中心に設定
            y0 = self.size/2
            x = self.size/2 + math.cos(angle)*self.size/2*0.9      #秒針先端の位置を算出
            y = self.size/2 + math.sin(angle)*self.size/2*0.9
            # 前の描写を tag で検索, deleteしてから描写
            self.clock.delete("SEC")
            self.clock.create_line(x0,y0,x,y, width=2, fill="red", tag="SEC")
                                                                    # cleate_line関数 : 端点(x0,y0), (x,y) を red 線でつなぐ
        # 秒針表示の判定
            if not self.show_sec:                                     #flagがたってるとき
                self.clock.create_line(x0,y0,x,y, width=2, fill="red", tag="SEC")   # flagがFalseのとき秒針表示
            if self.show_sec:
                self.clock.delete("SEC")                                            # flag が Trueのとき秒針削除




        # 分針, 時計の描写. 　1分毎
        if self.min != time.localtime().tm_min or self.start:
            self.min = time.localtime().tm_min
            angle = math.radians(self.min*360/60-90)
            x0 = self.size/2 - math.cos(angle)*self.size/2*0.1
            y0 = self.size/2 - math.sin(angle)*self.size/2*0.1
            x = self.size/2 + math.cos(angle)*self.size/2*0.85
            y = self.size/2 + math.sin(angle)*self.size/2*0.85
            # 前の描写を tag で検索, deleteしてから描写
            self.clock.delete("MIN")
            self.clock.create_line(x0,y0,x,y, width=6, fill="blue", tag="MIN")
    
            self.hour = time.localtime().tm_hour
            angle = math.radians((self.hour%12 + self.min/60)*360/12-90)
            x0 = self.size/2 - math.cos(angle)*self.size/2*0.1
            y0 = self.size/2 - math.sin(angle)*self.size/2*0.1
            x = self.size/2 + math.cos(angle)*self.size/2*0.60
            y = self.size/2 + math.sin(angle)*self.size/2*0.60
            self.clock.delete("HOUR")
            self.clock.create_line(x0,y0,x,y, width=6, fill="green", tag="HOUR")

        self.start = False
        # 日付の描写.　　秒が変わるかボタンが押されたとき
        if self.sec2 != time.localtime().tm_sec or not self.show_date:
            self.sec2 = time.localtime().tm_sec
            x = self.size/2
            y = self.size/2 + 50
            text = time.strftime('%Y/%m/%d %H:%M:%S')
            # 前の描写を tag で検索, deleteしてから描写
            self.clock.delete("TIME")
            if self.show_date:
                self.clock.create_text(x,y, text=text, font=("",20), fill="black", tag="TIME")

        # 以上の操作を 100 ms後に再度呼び出す
        self.after(100, self.display)


root = tk.Tk()
root.title("Analog Watch")
f = MyFrame(root)
f.pack()
f.display()
root.mainloop()
