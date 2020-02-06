# Implementation of the Fibonacci sequence using memoization, prints the sequence up to nth digit where n>0
# Input: int n
# Output: prints Fibonacci sequence up to n in list
# Time Complexity: O(n)

def fib(n):
    memo = [None]*(n+1) # init memo list to hold computed fib
    memoize(n, memo) # call helper func
    print(memo)
    return memo # return populated list at the end

def memoize(n, memo):
    if n <= 0: # base case
        memo[n] = 0
    elif n == 1: # base case
        memo[n] = 1
    elif memo[n] != None: return memo[n] # calculated before so lookup in list
    else: memo[n] = memoize(n-2, memo) + memoize(n-1, memo) # recursive call
    
    return memo[n]

fib(10) # call the function with example n > 0


