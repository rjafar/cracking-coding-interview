# Implementation of the Fibonacci sequence using memoization, prints the sequence up to nth digit where n>0
# Input: n = integer
# Output: prints Fibonacci sequence up to n
# Time Complexity: O(n)

def fib(n):
    memo = [None]*(n+1) # init memo list
    for i in range(n+1):
        result =  memoize(i, memo)
        print(result)
    return memo


def memoize(n, memo):
    if n <= 0: 
        memo[n] = 0
        return memo[n]
    elif n == 1: 
        memo[n] = 1
        return memo[n]
    elif memo[n] != None: return memo[n]

    memo[n] = memoize(n-2, memo) + memoize(n-1, memo)
    return memo[n]

fib(10)

