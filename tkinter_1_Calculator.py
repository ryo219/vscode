import tkinter as tk            #GUI Applicationの1つ, 電卓を tkinterを用いて作成
                                #ただし小数点以下の計算はめんどいため, 整数のみについて2数の四則演算を行う用
                                #計算時は毎度必ず　= 押すこと　

#電卓の加算を以下のように考える
#一個目の数値入力 ⇒ current_numberに格納, +-*/キー押したら first_termに保存される
#二個目の数値入力 ⇒ current_numberに格納, =キー押したら second_termに保存, 計算実行し resultに格納, currentの初期化


current_number = 0      #各入力値
first_term = 0          #一個目の入力
second_term = 0         #二個目の入力
result = 0              #結果格納用
flag_add = False        #計算種類の判別用変数, 入力記号に応じてフラグを建て, それだけを実行させる
flag_sub = False
flag_mul = False
flag_div = False


## ---- 各演算の内容を定義 ---- ##
def do_add():
    global current_number
    global first_term
    global flag_add
    flag_add = True                 # 和算のフラグ建て
    first_term = current_number     #一つ目の数字を格納しとく
    current_number = 0              #2つ目の数字を格納するため初期化

def do_sub():
    global current_number
    global first_term
    global flag_sub
    flag_sub = True
    first_term = current_number
    current_number = 0

def do_mul():
    global current_number
    global first_term
    global flag_mul
    flag_mul = True
    first_term = current_number
    current_number = 0
    
def do_div():
    global current_number
    global first_term
    global flag_div
    flag_div = True
    first_term = current_number
    current_number = 0
## ---------------------- ##



## ---- = が押された後の演算の判定, 演算の実行 ---- ##
def all_equ():              #あとで = 押した後にまとめて呼び出すために関数化しておく
    global first_term
    global second_term
    global result
    global current_number
    global flag_add
    global flag_sub
    global flag_mul
    global flag_div

    if flag_add:                            #和の flag がTrueの場合
        second_term = current_number            # 2つ目の入力を格納
        result = first_term + second_term       # 和の実行
        first_term = result                     # 次の演算に使えるよう, 演算結果を1個目の入力にしとく
        current_number = result                 # 表示はcurrent_number つかって行うため, result を代入しとく
        flag_add = False                        # flagを残しておくと次の演算時に誤発動しうる ⇒ 初期化しとく
    elif flag_sub:                          #差の flag がTrueの場合
        second_term = current_number
        result = first_term - second_term
        first_term = result
        current_number = result
        flag_sub = False
    elif flag_mul:                          #積の flag がTrueの場合
        second_term = current_number
        result = first_term * second_term
        first_term = result
        current_number = result
        flag_mul = False
    elif flag_div:                          #商の flag がTrueの場合
        second_term = current_number
        if second_term == 0:                    # 割る数が 0 のときだけ例外として処理
            result = 'Error'
            current_number = 0
            flag_div = False
        else:
            result = first_term/second_term
            first_term = result
            current_number = result
            flag_div = False
## ---------------------------- ##



#関数の定義. 入力値とインターフェースの表示のリンク付け
def key0():
    key(0) 
def key1():
    key(1)
def key2():
    key(2)
def key3():
    key(3)
def key4():
    key(4)
def key5():
    key(5)
def key6():
    key(6)
def key7():
    key(7)
def key8():
    key(8)
def key9():
    key(9)


#二桁以上, 小数点以下の値の保存, 表示
def key(n):
    global current_number
    current_number = current_number*10+n    #前の値 currentを10倍して入力 nと加算, currentを更新
    show_number(current_number)

def key00():
    global current_number
    current_number = current_number*100
    show_number(current_number)



#Clear、AllClear動作の定義
def clear():                    #Clearキーの中身 現在の値 currentのみを初期化し表示.　前の計算結果とかはfirst_termに残してる
    global current_number
    current_number = 0
    show_number(current_number)

def Allclear():                    #AllClearキーの中身 currentも first/second_termも初期化し表示
    global current_number
    global first_term
    global second_term
    current_number = 0
    first_term = 0
    second_term = 0
    show_number(current_number)





## ---- 各演算の呼出. 押されたボタンに応じて演算を行う ---- ##
def add():                     # + キーの処理. 最初に決めた add関数を呼び出し, show関数も呼出　　あとでキー押したときに呼び出すように関数化
    do_add()
    show_number(first_term)
def sub():                     # - キーの処理. 最初に決めた sub関数を呼び出し, show関数も呼出　　あとでキー押したときに呼び出すように関数化
    do_sub()
    show_number(first_term)
def mul():                     # × キーの処理. 最初に決めた mul関数を呼び出し, show関数も呼出　　あとでキー押したときに呼び出すように関数化
    do_mul()
    show_number(first_term)
def div():                     # ÷ キーの処理. 最初に決めた div関数を呼び出し, show関数も呼出　　あとでキー押したときに呼び出すように関数化
    do_div()
    show_number(first_term)


def equ():                      # = キーの処理. 最初に決めた all_equ関数を呼び出し, show関数も呼出　　　　あとでキー押したときに呼び出すように関数化
    global current_number
    all_equ()
    current_number = result     # 次の演算での一つ目の数字にする為, 演算結果を格納しとく
    show_number(result)

def show_number(num):           # show関数の中身
    e.delete(0,tk.END)          #エントリー(ディスプレイ欄)の文字列を消去
    e.insert(0,str(num))        #エントリー(ディスプレイ欄)に解答の文字列を表示
## ---------------------------- ##





## ---- ここからUIとかの設定　各ボタンの機能割当も ---- ##
root = tk.Tk()                  #ウィンドウの作成
root.title("電卓")
#root.geometry('600x400')        #ウィンドウのサイズサイズ
f = tk.Frame(root)              #中身にFrame(ボタン等を配置する枠)を作成し, 
f.grid()                        #grid()で割り付けする

b00 = tk.Button(f,text='00', command=key00, font=("",20), width=5)      #ボタンごとの機能割当　
b0 = tk.Button(f,text='0', command=key0, font=("",20), width=5)
b1 = tk.Button(f,text='1', command=key1, font=("",20), width=5)
b2 = tk.Button(f,text='2', command=key2, font=("",20), width=5)
b3 = tk.Button(f,text='3', command=key3, font=("",20), width=5)
b4 = tk.Button(f,text='4', command=key4, font=("",20), width=5)
b5 = tk.Button(f,text='5', command=key5, font=("",20), width=5)
b6 = tk.Button(f,text='6', command=key6, font=("",20), width=5)
b7 = tk.Button(f,text='7', command=key7, font=("",20), width=5)
b8 = tk.Button(f,text='8', command=key8, font=("",20), width=5)
b9 = tk.Button(f,text='9', command=key9, font=("",20), width=5)
bc = tk.Button(f,text='C', command=clear, font=("",20), width=5, bg = '#fffffb')
bac = tk.Button(f,text='AC', command=Allclear, font=("",20), width=5, bg = '#fffffb')
ba = tk.Button(f,text='+', command=add, font=("",20), width=7,  bg = '#fffffb')
bs = tk.Button(f,text='-', command=sub, font=("",20), width=7,  bg = '#fffffb')
bm = tk.Button(f,text='×', command=mul, font=("",20), width=7,  bg = '#fffffb')
bd = tk.Button(f,text='÷', command=div, font=("",20), width=7,  bg = '#fffffb')
be = tk.Button(f,text='=', command=equ, font=("",20), width=7,  bg = '#fffffb')
bg = '#000000'


bac.grid(row=1,column=0)
bc.grid(row=1,column=1)
b00.grid(row=5,column=0)
b0.grid(row=5,column=1)
b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
be.grid(row=5,column=4)
ba.grid(row=4,column=4)
bs.grid(row=3,column=4)
bm.grid(row=2,column=4)
bd.grid(row=1,column=4)


e = tk.Entry(f, font=("",25))
e.grid(row=0, column=0, columnspan=5, sticky=tk.W+tk.E+tk.N+tk.S)

clear()

root.mainloop()         #ここからGUIスタート