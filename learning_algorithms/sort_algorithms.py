import random
import sys, os, time


def bubble_sort(arr = []):
    """
    バブルソートは右から左に向けて隣同士を比較していき,
    左端まで来た時にある数が最小の数であるとしてソート済みにする.
    配列の要素数をNとした時, 
    最悪計算量:(N-1)+(N-2)+...+{N-(N-1)} = {N^2 - N)} / 2 の比較回数
    最良計算量:(N-1)+(N-2)+...+{N-(N-1)} = {N^2 - N)} / 2 の比較回数

    計算量はO(n^2)
    """
    
    N = len(arr)

    for sorted_idx in range(0, N):
        for i in range(N-1, sorted_idx, -1):    
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
            
    return arr

def selection_sort(arr = []):
    """
    選択ソートは配列の中から最小の数を線形探索し,
    左端の数と最小の数を入れ替え、左端の数をソート済みにする.
    配列の要素数をNとした時,
    最悪計算量:(N-1)+(N-2)+...+{N-(N-1)} = (N^2 - N) / 2 の比較回数
    最良計算量:(N-1)+(N-2)+...+{N-(N-1)} = (N^2 - N) / 2 の比較回数
    計算量はO(n^2)
    """

    N = len(arr)

    for sorted_idx in range(0, N):
        min_idx = -1

        for i in range(sorted_idx, N):
            if arr[i] < arr[min_idx] :
                min_idx = i
        
        arr[sorted_idx], arr[min_idx] = arr[min_idx], arr[sorted_idx]

    return arr

def insertion_sort(arr = []):
    """
    挿入ソートは初めに配列の左端をソート済にする.
    未探索領域の左端を取り出して,ソート済の数と右端から順に、
    自分より小さい数が現れるまで比較して交換する.
    最悪計算量:1 + 2 + ... + N-1 = (N^2 - N) / 2 の比較回数
    最良計算量:1 + 1 + ... + 1 = N - 1 の比較回数
    計算量はO(n^2)
    """

    N = len(arr)
    
    for sorted_idx in range(0, N-1):
        ref_idx = sorted_idx + 1 #未探索領域の左端の数字のインデックス

        for idx in range(sorted_idx, -1, -1):
            if arr[ref_idx] < arr[idx]:
                arr[ref_idx], arr[idx] = arr[idx], arr[ref_idx]
                ref_idx -= 1 #数字を入れ替えた場合参照するインデックスの更新
            else: #自分より少ない数字が現れた時比較を停止
                break

    return arr

def heap_sort(arr = []):
    """
    ヒープソート:未実装
    """
    N = len(arr)
    sorted_arr = [0 for i in range(N)] #整列済の配列
    heap_arr = [0 for i in range(N)] #入力された配列と同じ要素数の空の配列

    for i in range(N): #降順ヒープ木の構築
        max_idx = -1
        for j in range(i, N-1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        heap_arr[i] = arr[max_idx]
        arr[max_idx] = 0
    # print(heap_arr)

    sorted_arr[0] = heap_arr[0] #ルートの値をソート済

    heap_arr = heap_arr[1:] #ルートの値をヒープ木から除去
    #ルートに最後のノードを移動
    print(heap_arr)
    heap_arr = heap_arr[-1],  heap_arr[1:N]
    print(heap_arr)

    for i in range(len(heap_arr)):
        pass

    return arr

def merge_sort(arr = []):
    """
    マージソートはほぼ同じ長さの配列に分割していき,
    分割出来ない程度の要素数になったところから,
    分割した配列同士で小さい数順に並べるよう比較し統合する.
    大きさnの問題Pを解くとき,大きさn/cの小さい問題P(n/c)に分解して解き,
    その解を基にしてPの解を求める分割統治法の考え方
    T(n) = O(1) ... (n = 1)
    T(n) = a * T(n / c) + (b * n) ... (n > 1)
    から,
    T(n) = 2 * T(n/2) + (a + b) n ... (a,bは定数)
    したがって計算量はO(n * logn)
    """

    N = len(arr)
    if N > 1:

        n = len(arr)//2 #分割する数
        
        left = merge_sort(arr[:n]) #引数にした配列の要素数が1になるまで再帰
        right = merge_sort(arr[n:]) #引数にした配列の要素数が1になるまで再帰
        
        left_idx, right_idx, arr_idx = 0, 0, 0

        #left_idx, right_idxがそれぞれ参照している配列の要素数を超えない間,繰り返し実行
        #分割した2つの未整列の配列から小さい順に値を取り出して,整列済の配列に格納
        while left_idx < len(left) and right_idx < len(right): 
            if left[left_idx] < right[right_idx]:  
                arr[arr_idx] = left[left_idx]
                left_idx+=1
            else:
                arr[arr_idx] = right[right_idx]
                right_idx+=1
            arr_idx+=1

        #片方の配列が全て整列済の配列に格納された時に,残ったもう片方の配列を整列済の配列に格納
        while left_idx < len(left):
            arr[arr_idx] = left[left_idx]
            left_idx += 1
            arr_idx += 1
        while right_idx < len(right):
            arr[arr_idx] = right[right_idx]
            right_idx += 1
            arr_idx += 1

    return arr

def check_sorted(arr):
    """
    配列がソートされているか確認する.
    """

    flag = True
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                flag = False
            
    if flag:
        print("arr is sorted")
    else:
        print("arr is not sorted")
    


if __name__ == "__main__":
    # arr = [random.randint(0, 100) for _ in range(10)]
    arr = [i for i in range(4, 0, -1)]

    arr = merge_sort(arr)
    # print(arr)
    # check_sorted(arr)
    