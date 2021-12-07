# -*- coding: utf-8 -*-
"""longest_common_string.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wb0qBMbt68uDJAUPQ8douRAD6wWwGtyb

Longest Common Sequences(LCS) of X(length m) and Y(length n)
two approaches:(1)divide and conquer: time O(2^m*n) and space theta(1)
(2)dynamic programming: time O(m*n) space O(m*n)
"""

def LCSubStr(X, Y):
    m=len(X)#length of X
    n=len(Y)#length of Y
    # Create a table to store lengths of longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of X[0...i-1] and Y[0...j-1]. 
    #The first row and first column entries have no logical meaning, they are used only
    # for simplicity of the program.
 
    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]
 
    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
            else:
                LCSuff[i][j] = max(LCSuff[i-1][j],LCSuff[i][j-1])
    return LCSuff

X="ABCB"
Y="BDCAB"
matrixR=LCSubStr(X,Y)
print(matrixR)
print("\tYj",end="\t")
for i in Y:
  print(i,end="\t")
print()
print("Xi",end="\t")
for i in range(len(Y)+1):
  print(0,end="\t")
print()
for i in range(1,len(X)+1):
  print(X[i-1],end="\t")
  for j in matrixR[i]:
    print(j,end="\t")
  print()

print()
def LCS(matrixR,X,Y):  
  nrow=len(matrixR)-1
  ncol=len(matrixR[0])-1
  lis=[]
  while nrow>0 or ncol>0:
    if nrow==0 or ncol==0:
      break
    elif matrixR[nrow][ncol]==matrixR[nrow-1][ncol-1]+1:
      lis.append(X[nrow-1])
      nrow=nrow-1
      ncol=ncol-1
    else:
      ncol=ncol-1
  return lis[::-1]
print("LCS(longest common sequence)")
print(''.join(LCS(matrixR,X,Y)))