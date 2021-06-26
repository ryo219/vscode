print("Input the list of real numbers\r\nMake sure to press 'space button' between each number")
list = [float(x) for x in input().split(" ")]           # 文字列でなく数値として読み込むため
                                                        # こうしないと 一桁と二桁のソートがされない

## ---------- merge ---------- ##
def mergesort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    list_1 = list[:mid]
    list_2 = list[mid:]
    list_1 = mergesort(list_1)
    list_2 = mergesort(list_2)
    return merge(list_1, list_2)
## ---------- 　　 ---------- ##

## ---------- sort ---------- ##
def merge(list_1, list_2):
    sorted_list = []
    i, j = 0, 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:               # ここでは降順.　＞で昇順
            sorted_list.append(list_1[i])
            i += 1
        else:
            sorted_list.append(list_2[j])
            j += 1
    if i < len(list_1):                         # list_1/2 の片方が残存してた場合
            sorted_list.extend(list_1[i:])
    if j < len(list_2):
            sorted_list.extend(list_2[j:])
    return sorted_list
## ---------- 　　 ---------- ##

print("\r\nThe input  list : {0}".format(list))
print("The sorted list : {0}".format(mergesort(list)))