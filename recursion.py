# -*- coding: utf-8 -*-
"""recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZmfsAbokzlJRVA7cZ7cusaRy0VzSY99W
"""

def mult(a,b):
  if b==1:
    return a
  else:
    return a+mult(a,b-1)

mult(2,5)

def factorial(n):
  if n==1:
    return n
  else:
    return n*factorial(n-1)

factorial(3)

def printMove(fr, to):
  print('move from ' + str(fr) + ' to ' + str(to))
def Towers(n, fr, to, spare):
  if n == 1:
    printMove(fr, to)
  else:
    Towers(n-1, fr, spare, to)
    Towers(1, fr, to, spare)
    Towers(n-1, spare, to, fr)

def fib(n):
  if n==0 or n==1:
    return 1
  else:
    return fib(n-1)+fib(n-2)

for i in range(0,5):
  print(fib(i))

def isPalindrome(s):
  def toChars(s):
    s = s.lower()
    ans = ''
    for c in s:
      if c in 'abcdefghijklmnopqrstuvwxyz':
        ans = ans + c
    return ans
  
  def isPal(s):
    if len(s) <= 1:
      return True
    else:
      return s[0] == s[-1] and isPal(s[1:-1])

  return isPal(toChars(s))

s="Are we not drawn onward, we few, drawn onward to new era?"
if isPalindrome(s):
  print("yes,{string} is a palindrome".format(string=s))
else:
  print("not a palindrome")

s1="radar"
if isPalindrome(s1):
  print("yes,{string} is a palindrome".format(string=s1))
else:
  print("not a palindrome")