##　ニュートン法による正の平方根の算出　##
print('\r\nCalculate the square root of input number\r\n')
x = int(input())
x_new = x
flag = x_new
count = 0               ## 計算回数

                        ## 計算結果が同じになるまでニュートン法の計算実行
while flag > 0:         ## 判定には flag を使用
    x1=x_new
    x2=x/x1
    x_new=(x1+x2)/2
    if flag-x_new == 0:     # 計算結果が同じになった場合,, flagをにして終了
        flag = 0
    elif flag-x_new > 0:    # 計算結果が同じでない場合, flagを更新して再度計算
        flag = x_new
        print(x_new)
        count += 1

print('The square root of {0} is {1}'.format(x, x_new))
print('Calculation : {0} times\r\n'.format(count))