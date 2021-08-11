import random
import sys, os, time




def bubble_sort(arr = []):
    """
    バブルソートは右から左に向けて隣同士を比較していき,
    左端まで来た時にある数が最小の数であるとしてソート済みにする.
    配列の要素数をNとした時,
    1回目の外側のループでN-1回の比較を行う.
    2回目の外側のループでN-2回の比較を行う.
    N-1回目の外側の最後のループでN-(N-1)回の比較を行う.
    したがって、(N-1)+(N-2)+...+{N-(N-1)} = {N*(N-1)}/2の比較回数
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
    1回目の外側のループでNー1回の線形探索を行う.
    2回目の外側のループでNー2回の線形探索を行う.
    N-1回目の外側の最後のループでN-(N-1)回の線形探索を行う.
    したがって、(N-1)+(N-2)+...+{N-(N-1)} = {N*(N-1)}/2の比較回数
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
    arr = [random.randint(0, 100) for _ in range(10)]
    # arr = [i for i in range(4, -1, -1)]

    arr = selection_sort(arr)
    check_sorted(arr)
    