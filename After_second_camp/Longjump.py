from collections import defaultdict, deque, Counter
from functools import lru_cache
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
from random import randint
from fractions import Fraction as frac
import math
hpop = heappop
hpush = heappush
MOD = 10**9 + 7
 
def solution():
    _ = int(input())
    arr = list(map(int, input().split()))
    dp = [None]*len(arr)
    for i in range(len(arr))[::-1]:
        dp[i] = arr[i]
        next_index = arr[i] + i
        if next_index < len(arr):
            dp[i] += dp[next_index]
 
    return print(max(dp))
 
 
 
 
 
def main():
    #test()
    t = 1
    t = int(input())
    for _ in range(t):
        solution() 
 
#import sys
#import threading
#sys.setrecursionlimit(10**6)
#threading.stack_size(1 << 27)
#thread = threading.Thread(target=main)
#thread.start(); thread.join()
main()
 
