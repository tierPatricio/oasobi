import random
import sys, os, time




def bubble_sort(arr = []):
    """
    バブルソートは配列の要素数をNとした時,
    1回目の外側のループでN-1回の比較を行う.
    2回目の外側のループでN-2回の比較を行う.
    N-1回目の外側の最後のループでN-(N-1)回の比較を行う.
    したがって、(N-1)+(N-2)+...+{N-(N-1)} = {N*(N-1)}/2の比較回数
    計算量はO(n^2)
    """
    
    N = len(arr)
    print((N**2)/2)
    num = 0
    num_l = 0
    for sorted_idx in range(0, N):
        num += 1
        for i in range(N-1, sorted_idx, -1):
            num_l += 1
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]

        print(N,num, num_l)
            
    return arr


if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(10)]

    ret = bubble_sort(arr)
    print(ret)